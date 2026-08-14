"""Tests for the MITRE ATT&CK importer (stage S4).

Offline: the fixture is a real slice of the enterprise STIX bundle containing a
parent technique (T1557), a sub-technique (T1557.002 — the stage's acceptance
target), a standalone technique (T1046), and one revoked technique.
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
IMPORTER = ROOT / "scripts" / "importers" / "import_attack.py"
FIXTURE = ROOT / "scripts" / "fixtures" / "attack-sample.json"

sys.path.insert(0, str(ROOT / "scripts" / "importers"))
import import_attack  # noqa: E402


def _corpus(tmp_path: Path) -> Path:
    (tmp_path / "imports").mkdir()
    (tmp_path / "meta" / "attribution").mkdir(parents=True)
    return tmp_path


def _run(out: Path, *extra: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(IMPORTER), "--out", str(out), "--fixture", str(FIXTURE), *extra],
        capture_output=True, text=True, cwd=str(ROOT),
    )


def test_imports_techniques(tmp_path):
    root = _corpus(tmp_path)
    proc = _run(root / "imports" / "mitre-attack")
    assert proc.returncode == 0, proc.stderr
    ids = {p.stem for p in (root / "imports" / "mitre-attack").rglob("*.md")}
    assert {"T1557", "T1557.002", "T1046"} <= ids


def test_subtechnique_gets_its_own_page(tmp_path):
    """`lookup T1557.002` must land on ARP Cache Poisoning, not the parent —
    that is how operators actually search."""
    root = _corpus(tmp_path)
    _run(root / "imports" / "mitre-attack")
    page = (root / "imports" / "mitre-attack" / "T1557" / "T1557.002.md").read_text()
    assert "slug: technique/T1557.002" in page
    assert "ARP Cache Poisoning" in page
    assert "technique/T1557" in page, "sub-technique must link back to its parent"


def test_revoked_techniques_are_skipped(tmp_path):
    """Retired guidance must not be served to someone searching a technique id."""
    root = _corpus(tmp_path)
    proc = _run(root / "imports" / "mitre-attack")
    ids = {p.stem for p in (root / "imports" / "mitre-attack").rglob("*.md")}
    assert "T1066" not in ids, "revoked technique must not be published"
    assert "skipped 1 retired" in proc.stdout


def test_include_retired_override(tmp_path):
    root = _corpus(tmp_path)
    _run(root / "imports" / "mitre-attack", "--include-retired")
    ids = {p.stem for p in (root / "imports" / "mitre-attack").rglob("*.md")}
    assert "T1066" in ids


def test_frontmatter_is_valid_and_namespaced(tmp_path):
    root = _corpus(tmp_path)
    _run(root / "imports" / "mitre-attack")
    page = (root / "imports" / "mitre-attack" / "T1046" / "T1046.md").read_text()
    assert page.startswith("---\n")
    for key in ("slug: technique/T1046", "page_type: technique",
                "provenance: imported", "import_source: mitre-attack"):
        assert key in page, f"missing {key}"
    # must not collide with the cve/ namespace used by KEV and NVD
    assert "slug: cve/" not in page


def test_manifest_and_attribution(tmp_path):
    root = _corpus(tmp_path)
    _run(root / "imports" / "mitre-attack")
    m = json.loads((root / "imports" / "mitre-attack" / "manifest.json").read_text())
    assert m["source"] == "mitre-attack" and m["attack_domain"] == "enterprise"
    assert m["count"] >= 3 and m["skipped_retired"] >= 1

    attr = (root / "meta" / "attribution" / "mitre-attack.md").read_text()
    assert "MITRE" in attr and "trademark" in attr.lower()
    assert "does not endorse" in attr.lower(), "MITRE terms require no-endorsement notice"


def test_limit_caps_output(tmp_path):
    root = _corpus(tmp_path)
    _run(root / "imports" / "mitre-attack", "--limit", "1")
    assert len(list((root / "imports" / "mitre-attack").rglob("*.md"))) == 1


# --- pure helpers ---------------------------------------------------------

def test_attack_id_extraction():
    obj = {"external_references": [
        {"source_name": "capec", "external_id": "CAPEC-94"},
        {"source_name": "mitre-attack", "external_id": "T1557.002"},
    ]}
    assert import_attack.attack_id(obj) == "T1557.002"


def test_attack_id_missing():
    assert import_attack.attack_id({"external_references": []}) is None


def test_is_retired_detects_both_flags():
    assert import_attack.is_retired({"revoked": True})
    assert import_attack.is_retired({"x_mitre_deprecated": True})
    assert not import_attack.is_retired({"name": "live"})


def test_tactics_ignore_non_attack_kill_chains():
    obj = {"kill_chain_phases": [
        {"kill_chain_name": "mitre-attack", "phase_name": "credential-access"},
        {"kill_chain_name": "lockheed", "phase_name": "exploitation"},
    ]}
    assert import_attack.tactics_of(obj) == ["Credential Access"]
