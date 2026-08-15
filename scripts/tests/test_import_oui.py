"""Tests for the IEEE OUI importer (stage S6).

The property that matters is **longest-prefix match**. MA-M/MA-S blocks are
carved out of MA-L space, so a 24-bit-only lookup returns the umbrella holder
("IEEE Registration Authority") instead of the real vendor for ~13,500 prefixes.
The fixture uses real registrations that exhibit exactly that.
"""
from __future__ import annotations

import csv
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
IMPORTER = ROOT / "scripts" / "importers" / "import_oui.py"
FIXTURE = ROOT / "scripts" / "fixtures" / "oui-sample.csv"

sys.path.insert(0, str(ROOT / "scripts" / "importers"))
import import_oui  # noqa: E402


def _table() -> dict[str, dict]:
    return import_oui.load_table(FIXTURE)


# --- normalisation --------------------------------------------------------

def test_normalize_mac_strips_separators():
    for form in ("8C:1F:64:AF:A1:23", "8c-1f-64-af-a1-23", "8c1f64afa123", "8c1f.64af.a123"):
        assert import_oui.normalize_mac(form) == "8C1F64AFA123"


def test_normalize_mac_handles_junk():
    assert import_oui.normalize_mac("") == ""
    assert import_oui.normalize_mac("not-a-mac") == "AAC"  # hex chars only


# --- the core property: longest prefix wins -------------------------------

def test_ma_s_beats_its_24bit_parent():
    """8C1F64AFA is an MA-S block inside 8C1F64, which belongs to the umbrella
    'IEEE Registration Authority'. The specific vendor must win."""
    hit = import_oui.lookup_vendor("8C:1F:64:AF:A1:23", _table())
    assert hit is not None
    assert hit["registry"] == "MA-S"
    assert hit["bits"] == 36
    assert "IEEE Registration Authority" not in hit["vendor"]


def test_ma_l_still_resolves_when_no_smaller_block_matches():
    hit = import_oui.lookup_vendor("28:6F:B9:11:22:33", _table())
    assert hit is not None
    assert hit["registry"] == "MA-L" and hit["bits"] == 24


def test_bare_prefix_query_works():
    """Operators paste a bare OUI, not always a full MAC."""
    hit = import_oui.lookup_vendor("286FB9", _table())
    assert hit and hit["registry"] == "MA-L"


def test_unknown_prefix_returns_none():
    assert import_oui.lookup_vendor("00:00:00:00:00:00", _table()) is None


def test_too_short_input_returns_none():
    assert import_oui.lookup_vendor("8C1F", _table()) is None
    assert import_oui.lookup_vendor("", _table()) is None


# --- generated file shape -------------------------------------------------

def test_import_writes_sorted_csv(tmp_path):
    out = tmp_path / "data"
    proc = subprocess.run(
        [sys.executable, str(IMPORTER), "--out", str(out), "--fixture", str(FIXTURE)],
        capture_output=True, text=True, cwd=str(ROOT),
    )
    assert proc.returncode == 0, proc.stderr

    rows = list(csv.DictReader((out / "oui.csv").open(newline="", encoding="utf-8")))
    assert rows and set(rows[0]) == {"prefix", "bits", "registry", "vendor"}
    bits = [int(r["bits"]) for r in rows]
    assert bits == sorted(bits, reverse=True), "longest prefixes must sort first"


def test_manifest_documents_the_lookup_rule(tmp_path):
    """A consumer reading only the manifest must learn that a naive 24-bit
    lookup is wrong."""
    out = tmp_path / "data"
    subprocess.run(
        [sys.executable, str(IMPORTER), "--out", str(out), "--fixture", str(FIXTURE)],
        capture_output=True, text=True, cwd=str(ROOT),
    )
    m = json.loads((out / "manifest.json").read_text())
    assert m["source"] == "ieee-oui"
    assert "longest prefix" in m["lookup_rule"].lower()
    assert m["count"] >= 3


def test_no_markdown_pages_emitted(tmp_path):
    """S6 is data, not 53k wiki pages."""
    out = tmp_path / "data"
    subprocess.run(
        [sys.executable, str(IMPORTER), "--out", str(out), "--fixture", str(FIXTURE)],
        capture_output=True, text=True, cwd=str(ROOT),
    )
    assert not list(out.rglob("*.md"))


# --- parser ---------------------------------------------------------------

def test_parse_registry_skips_malformed_and_keeps_private():
    text = (
        "Registry,Assignment,Organization Name,Organization Address\n"
        "MA-L,286FB9,Nokia,Somewhere\n"
        "MA-L,NOTHEX,Bogus,X\n"
        "MA-L,AABBCC,,NoName\n"
    )
    rows = import_oui.parse_registry(text, "MA-L", 24)
    prefixes = {r[0] for r in rows}
    assert "286FB9" in prefixes
    assert "NOTHEX" not in prefixes, "non-hex assignment must be dropped"
    assert any(r[0] == "AABBCC" and r[3] == "Private" for r in rows)


def test_prefixes_shared_by_multiple_orgs_keep_every_claimant(tmp_path):
    """IEEE really does register some prefixes twice — 080030 is shared by
    Network Research Corp, RMIT and CERN. Loading into a dict silently kept the
    last one, so a lookup confidently reported one org and hid the others."""
    src = tmp_path / "in.csv"
    src.write_text(
        "prefix,bits,registry,vendor\n"
        "080030,24,MA-L,NETWORK RESEARCH CORPORATION\n"
        "080030,24,MA-L,ROYAL MELBOURNE INST OF TECH\n"
        "080030,24,MA-L,CERN\n",
        encoding="utf-8",
    )
    out = tmp_path / "data"
    proc = subprocess.run(
        [sys.executable, str(IMPORTER), "--out", str(out), "--fixture", str(src)],
        capture_output=True, text=True, cwd=str(ROOT),
    )
    assert proc.returncode == 0, proc.stderr

    rows = list(csv.DictReader((out / "oui.csv").open(newline="", encoding="utf-8")))
    assert len(rows) == 1, "one row per prefix"
    vendor = rows[0]["vendor"]
    for org in ("NETWORK RESEARCH CORPORATION", "ROYAL MELBOURNE INST OF TECH", "CERN"):
        assert org in vendor, f"{org} was dropped"

    m = json.loads((out / "manifest.json").read_text())
    assert m["shared_prefixes"] == 1
