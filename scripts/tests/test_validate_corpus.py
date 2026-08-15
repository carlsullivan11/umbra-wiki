"""Tests for the corpus validator.

The validator must agree with the engine about what counts as a page. It did
not: the engine skips README/SCHEMA/CONTRIBUTING anywhere in the tree, while the
validator flagged them — so adding a per-importer README (S6) failed validation
for a file the engine never indexes.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VALIDATOR = ROOT / "scripts" / "validate_corpus.py"

sys.path.insert(0, str(ROOT / "scripts"))
import validate_corpus  # noqa: E402


def test_non_page_docs_match_the_engine_exclusions():
    """Keep this list in step with umbra/wiki/parse.py load_corpus()."""
    assert {"README.MD", "SCHEMA.MD", "CONTRIBUTING.MD"} <= validate_corpus.NON_PAGES


def test_readme_inside_imports_is_not_treated_as_a_page():
    assert "README.MD" in validate_corpus.NON_PAGES


def test_live_corpus_validates():
    """The real corpus must pass — this is what CI gates on."""
    proc = subprocess.run([sys.executable, str(VALIDATOR)], capture_output=True, text=True, cwd=str(ROOT))
    assert proc.returncode == 0, proc.stdout + proc.stderr
    assert "ok ·" in proc.stdout
