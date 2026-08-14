"""Tests for the NVD importer (stage S3).

No network: everything runs from scripts/fixtures/nvd-sample.json, which was
captured from the live NVD API 2.0 so the shape is real rather than invented.
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
IMPORTER = ROOT / "scripts" / "importers" / "import_nvd.py"
FIXTURE = ROOT / "scripts" / "fixtures" / "nvd-sample.json"

sys.path.insert(0, str(ROOT / "scripts" / "importers"))
import import_nvd  # noqa: E402


def _corpus(tmp_path: Path) -> Path:
    (tmp_path / "imports").mkdir()
    (tmp_path / "curated").mkdir()
    (tmp_path / "meta" / "attribution").mkdir(parents=True)
    return tmp_path


def _run(out: Path, *extra: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(IMPORTER), "--out", str(out), "--fixture", str(FIXTURE), *extra],
        capture_output=True, text=True, cwd=str(ROOT),
    )


def test_fixture_import_writes_pages(tmp_path):
    root = _corpus(tmp_path)
    proc = _run(root / "imports" / "nvd-cve")
    assert proc.returncode == 0, proc.stderr
    pages = list((root / "imports" / "nvd-cve").rglob("*.md"))
    assert len(pages) == 3
    assert all(p.parent.name.isdigit() for p in pages), "pages are filed by year"


def test_pages_have_required_frontmatter(tmp_path):
    root = _corpus(tmp_path)
    _run(root / "imports" / "nvd-cve")
    page = next((root / "imports" / "nvd-cve").rglob("*.md")).read_text()
    for key in ("slug:", "title:", "page_type:", "provenance: imported", "import_source: nvd"):
        assert key in page, f"missing {key}"
    assert page.startswith("---\n")


def test_skips_cves_already_in_the_corpus(tmp_path):
    """The collision guard. KEV already publishes cve/<ID> slugs; two pages for
    one slug used to abort the whole index rebuild. KEV wins — an actively
    exploited CVE with a required action outranks the raw NVD record."""
    root = _corpus(tmp_path)
    kev_dir = root / "imports" / "cisa-kev" / "1999"
    kev_dir.mkdir(parents=True)
    (kev_dir / "CVE-1999-0095.md").write_text("---\nslug: cve/CVE-1999-0095\n---\n")

    proc = _run(root / "imports" / "nvd-cve")
    assert proc.returncode == 0, proc.stderr

    written = {p.stem for p in (root / "imports" / "nvd-cve").rglob("*.md")}
    assert "CVE-1999-0095" not in written, "must not duplicate a CVE KEV already has"
    assert len(written) == 2
    assert "skipped 1" in proc.stdout


def test_allow_duplicates_overrides_the_skip(tmp_path):
    root = _corpus(tmp_path)
    kev_dir = root / "imports" / "cisa-kev" / "1999"
    kev_dir.mkdir(parents=True)
    (kev_dir / "CVE-1999-0095.md").write_text("---\nslug: cve/CVE-1999-0095\n---\n")

    _run(root / "imports" / "nvd-cve", "--allow-duplicates")
    written = {p.stem for p in (root / "imports" / "nvd-cve").rglob("*.md")}
    assert "CVE-1999-0095" in written


def test_limit_caps_output(tmp_path):
    root = _corpus(tmp_path)
    _run(root / "imports" / "nvd-cve", "--limit", "1")
    assert len(list((root / "imports" / "nvd-cve").rglob("*.md"))) == 1


def test_manifest_records_incremental_mode(tmp_path):
    """The manifest must make it obvious this is capped/incremental, so nobody
    later assumes the corpus mirrors all of NVD."""
    root = _corpus(tmp_path)
    _run(root / "imports" / "nvd-cve")
    m = json.loads((root / "imports" / "nvd-cve" / "manifest.json").read_text())
    assert m["incremental"] is True
    assert m["source"] == "nvd-cve"
    assert m["limit"] >= 1 and m["window_days"] >= 1


def test_attribution_written(tmp_path):
    root = _corpus(tmp_path)
    _run(root / "imports" / "nvd-cve")
    attr = (root / "meta" / "attribution" / "nvd-cve.md").read_text()
    assert "National Vulnerability Database" in attr
    assert "incremental" in attr.lower()


# --- pure helpers ---------------------------------------------------------

def test_best_cvss_prefers_newest_version():
    metrics = {
        "cvssMetricV2": [{"cvssData": {"baseScore": 5.0, "vectorString": "AV:N"}}],
        "cvssMetricV31": [{"cvssData": {"baseScore": 9.8, "baseSeverity": "CRITICAL",
                                        "vectorString": "CVSS:3.1/AV:N"}}],
    }
    version, score, vector = import_nvd._best_cvss(metrics)
    assert version == "3.1" and "9.8" in score and "CRITICAL" in score


def test_best_cvss_handles_missing_metrics():
    assert import_nvd._best_cvss({}) == ("", "", "")


def test_cwes_extracted():
    w = [{"description": [{"value": "CWE-79"}, {"value": "NVD-CWE-noinfo"}]}]
    assert import_nvd._cwes(w) == ["CWE-79"]


def test_existing_cve_ids_scans_all_importers(tmp_path):
    root = _corpus(tmp_path)
    (root / "imports" / "cisa-kev" / "2021").mkdir(parents=True)
    (root / "imports" / "cisa-kev" / "2021" / "CVE-2021-44228.md").write_text("x")
    (root / "curated" / "CVE-2020-0001.md").write_text("x")
    found = import_nvd.existing_cve_ids(root)
    assert "CVE-2021-44228" in found and "CVE-2020-0001" in found
