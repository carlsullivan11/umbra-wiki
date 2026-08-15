#!/usr/bin/env python3
"""Validate umbra-wiki corpus frontmatter basics."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FM = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)

# Documentation files that live beside content but are NOT wiki pages. This must
# match the engine's own exclusion list (umbra/wiki/parse.py load_corpus) —
# otherwise the validator rejects files the engine deliberately never indexes,
# which is exactly what a per-importer README triggered.
NON_PAGES = {"README.MD", "SCHEMA.MD", "CONTRIBUTING.MD", "LICENSE"}


def main() -> int:
    errors = 0
    pages = [
        p
        for p in list(ROOT.joinpath("curated").rglob("*.md"))
        + list(ROOT.joinpath("imports").rglob("*.md"))
        if p.name.upper() not in NON_PAGES
    ]
    for path in pages:
        text = path.read_text(encoding="utf-8")
        m = FM.match(text)
        if not m:
            print(f"FAIL {path}: missing frontmatter")
            errors += 1
            continue
        block = m.group(1)
        if "slug:" not in block or "title:" not in block or "page_type:" not in block:
            print(f"FAIL {path}: slug/title/page_type required")
            errors += 1
    if errors:
        print(f"{errors} error(s)")
        return 1
    print(f"ok · {len(pages)} pages")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
