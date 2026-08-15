"""Tests for the RFC importer (stage S7).

Fixture is a real slice of the RFC index: RFC 826 (ARP), RFC 1035 (DNS), and two
that are genuinely obsoleted — RFC 7489 (DMARC → 9989/9990/9991) and RFC 8446
(TLS 1.3 → 9846).
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
IMPORTER = ROOT / "scripts" / "importers" / "import_rfc.py"
FIXTURE = ROOT / "scripts" / "fixtures" / "rfc-index-sample.xml"

sys.path.insert(0, str(ROOT / "scripts" / "importers"))
import import_rfc  # noqa: E402


def _corpus(tmp_path: Path) -> Path:
    (tmp_path / "imports").mkdir()
    (tmp_path / "meta" / "attribution").mkdir(parents=True)
    return tmp_path


def _list(tmp_path: Path, body: str) -> Path:
    p = tmp_path / "rfcs.txt"
    p.write_text(body, encoding="utf-8")
    return p


def _run(out: Path, list_path: Path) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(IMPORTER), "--out", str(out), "--list", str(list_path),
         "--fixture", str(FIXTURE)],
        capture_output=True, text=True, cwd=str(ROOT),
    )


# --- id normalisation (the index uses UNPADDED ids) -----------------------

def test_normalize_handles_every_form_operators_type():
    for form in ("826", "RFC826", "rfc826", "RFC 826", "rfc-826", "RFC0826", "RFC00826"):
        assert import_rfc.normalize_rfc_id(form) == "RFC826", form


def test_normalize_rejects_nonsense():
    assert import_rfc.normalize_rfc_id("") is None
    assert import_rfc.normalize_rfc_id("banana") is None
    assert import_rfc.normalize_rfc_id("RFC") is None


def test_curated_list_parsing_ignores_comments_and_dupes(tmp_path):
    p = _list(tmp_path, "# header\nRFC826   # ARP\n\n1035\nRFC826\n   \n")
    assert import_rfc.read_list(p) == ["RFC826", "RFC1035"]


# --- import behaviour -----------------------------------------------------

def test_imports_listed_rfcs(tmp_path):
    root = _corpus(tmp_path)
    proc = _run(root / "imports" / "ietf-rfc", _list(tmp_path, "RFC826\nRFC1035\n"))
    assert proc.returncode == 0, proc.stderr
    ids = {p.stem for p in (root / "imports" / "ietf-rfc").glob("*.md")}
    assert ids == {"RFC826", "RFC1035"}


def test_obsoleted_rfc_gets_a_warning_and_successor_link(tmp_path):
    """Publishing 'RFC 8446 — TLS 1.3' with no hint it has been superseded would
    actively mislead — same failure mode as importing retired CWE/ATT&CK."""
    root = _corpus(tmp_path)
    _run(root / "imports" / "ietf-rfc", _list(tmp_path, "RFC8446\n"))
    page = (root / "imports" / "ietf-rfc" / "RFC8446.md").read_text()
    assert "Obsoleted" in page
    assert "RFC9846" in page, "must name the successor"
    assert "Obsoleted by" in page, "metadata table must state it too"


def test_current_rfc_has_no_obsolete_banner(tmp_path):
    root = _corpus(tmp_path)
    _run(root / "imports" / "ietf-rfc", _list(tmp_path, "RFC1035\n"))
    page = (root / "imports" / "ietf-rfc" / "RFC1035.md").read_text()
    assert "⚠️ **Obsoleted.**" not in page


def test_abstract_present_but_full_text_only_linked(tmp_path):
    """Corpus rule: metadata and pointers, never reproduced documents."""
    root = _corpus(tmp_path)
    _run(root / "imports" / "ietf-rfc", _list(tmp_path, "RFC826\n"))
    page = (root / "imports" / "ietf-rfc" / "RFC826.md").read_text()
    assert "## Abstract" in page
    assert "rfc-editor.org/rfc/rfc826.txt" in page
    assert "is linked, not copied" in page
    assert len(page) < 12000, "a page this large suggests full text was copied in"


def test_frontmatter_namespace_and_ids(tmp_path):
    root = _corpus(tmp_path)
    _run(root / "imports" / "ietf-rfc", _list(tmp_path, "RFC826\n"))
    page = (root / "imports" / "ietf-rfc" / "RFC826.md").read_text()
    assert page.startswith("---\n")
    for key in ("slug: rfc/RFC826", "page_type: rfc", "import_source: ietf-rfc",
                "standards: [RFC826]"):
        assert key in page, f"missing {key}"
    # must not collide with the other importers' namespaces
    for other in ("slug: cve/", "slug: technique/", "slug: weakness/"):
        assert other not in page


def test_rfc_absent_from_index_is_reported_not_silent(tmp_path):
    """A typo'd list entry must surface, not vanish."""
    root = _corpus(tmp_path)
    proc = _run(root / "imports" / "ietf-rfc", _list(tmp_path, "RFC826\nRFC9999\n"))
    m = json.loads((root / "imports" / "ietf-rfc" / "manifest.json").read_text())
    assert m["missing"] == ["RFC9999"]
    assert m["count"] == 1 and m["requested"] == 2
    assert "missing from index" in proc.stdout


def test_manifest_and_attribution_state_curation(tmp_path):
    root = _corpus(tmp_path)
    _run(root / "imports" / "ietf-rfc", _list(tmp_path, "RFC826\nRFC8446\n"))
    m = json.loads((root / "imports" / "ietf-rfc" / "manifest.json").read_text())
    assert m["curated"] is True
    assert "RFC8446" in m["obsoleted_pages"]

    attr = (root / "meta" / "attribution" / "ietf-rfc.md").read_text()
    assert "not** a mirror" in attr or "not a mirror" in attr
    assert "never" in attr.lower() and "full text" in attr.lower()


# --- helpers --------------------------------------------------------------

def test_multi_splits_packed_ids():
    import xml.etree.ElementTree as ET

    e = ET.fromstring("<rfc-entry><obsoleted-by>RFC9989\n  RFC9990</obsoleted-by></rfc-entry>")
    assert import_rfc._multi(e, "", "obsoleted-by") == ["RFC9989", "RFC9990"]
