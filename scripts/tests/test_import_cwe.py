"""Tests for the CWE importer (stage S5).

Offline: the fixture is a real slice of the CWE catalogue — XSS (79), SQLi (89),
out-of-bounds write (787), plus one Deprecated entry to prove retired
classifications are filtered.
"""
from __future__ import annotations

import json
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
IMPORTER = ROOT / "scripts" / "importers" / "import_cwe.py"
FIXTURE = ROOT / "scripts" / "fixtures" / "cwe-sample.xml"

sys.path.insert(0, str(ROOT / "scripts" / "importers"))
import import_cwe  # noqa: E402


def _corpus(tmp_path: Path) -> Path:
    (tmp_path / "imports").mkdir()
    (tmp_path / "meta" / "attribution").mkdir(parents=True)
    return tmp_path


def _run(out: Path, *extra: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(IMPORTER), "--out", str(out), "--fixture", str(FIXTURE), *extra],
        capture_output=True, text=True, cwd=str(ROOT),
    )


def test_imports_weaknesses(tmp_path):
    root = _corpus(tmp_path)
    proc = _run(root / "imports" / "mitre-cwe")
    assert proc.returncode == 0, proc.stderr
    ids = {p.stem for p in (root / "imports" / "mitre-cwe").glob("*.md")}
    assert {"CWE-79", "CWE-89", "CWE-787"} <= ids


def test_deprecated_weaknesses_are_skipped(tmp_path):
    """A retired classification must not be served to someone triaging a CVE."""
    root = _corpus(tmp_path)
    proc = _run(root / "imports" / "mitre-cwe")
    ids = {p.stem for p in (root / "imports" / "mitre-cwe").glob("*.md")}
    assert "CWE-1187" not in ids
    assert "skipped 1 retired" in proc.stdout


def test_include_retired_override(tmp_path):
    root = _corpus(tmp_path)
    _run(root / "imports" / "mitre-cwe", "--include-retired")
    ids = {p.stem for p in (root / "imports" / "mitre-cwe").glob("*.md")}
    assert "CWE-1187" in ids


def test_page_uses_weakness_namespace_and_has_content(tmp_path):
    """`weakness/` must not collide with the cve/ or technique/ namespaces, and
    the page has to carry the substance a reader followed the link for."""
    root = _corpus(tmp_path)
    _run(root / "imports" / "mitre-cwe")
    page = (root / "imports" / "mitre-cwe" / "CWE-79.md").read_text()
    assert "slug: weakness/CWE-79" in page
    assert "page_type: weakness" in page
    assert "slug: cve/" not in page and "slug: technique/" not in page
    assert "Cross-site Scripting" in page
    assert "## Common consequences" in page
    assert "## Mitigations" in page


def test_manifest_and_attribution(tmp_path):
    root = _corpus(tmp_path)
    _run(root / "imports" / "mitre-cwe")
    m = json.loads((root / "imports" / "mitre-cwe" / "manifest.json").read_text())
    assert m["source"] == "mitre-cwe"
    assert m["count"] >= 3 and m["skipped_retired"] >= 1
    assert m["catalog_version"]

    attr = (root / "meta" / "attribution" / "mitre-cwe.md").read_text()
    assert "CWE" in attr and "trademark" in attr.lower()
    assert "does not endorse" in attr.lower()


def test_limit_caps_output(tmp_path):
    root = _corpus(tmp_path)
    _run(root / "imports" / "mitre-cwe", "--limit", "1")
    assert len(list((root / "imports" / "mitre-cwe").glob("*.md"))) == 1


# --- pure helpers ---------------------------------------------------------

def _fixture_root():
    return ET.parse(FIXTURE).getroot()


def test_is_retired_detects_status():
    assert import_cwe.is_retired(ET.Element("W", {"Status": "Deprecated"}))
    assert import_cwe.is_retired(ET.Element("W", {"Status": "Obsolete"}))
    assert not import_cwe.is_retired(ET.Element("W", {"Status": "Stable"}))


def test_text_flattens_nested_markup():
    """CWE descriptions embed xhtml; naive .text would drop most of the prose."""
    el = ET.fromstring("<d>outer <p>inner</p> tail</d>")
    assert import_cwe._text(el) == "outer inner tail"


def test_text_handles_none():
    assert import_cwe._text(None) == ""


def test_consequences_extracted_from_real_fixture():
    root = _fixture_root()
    ns = import_cwe._ns(root)
    w = next(x for x in import_cwe._findall(root, ns, "Weakness") if x.get("ID") == "79")
    cons = import_cwe.consequences(w, ns)
    assert cons and any(":" in c for c in cons)
