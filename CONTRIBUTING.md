# Contributing to umbra-wiki

## Quick start

1. Fork + branch
2. Add or edit a page under `curated/` following [SCHEMA.md](SCHEMA.md)
3. Open a PR

## Rules

1. **Cite sources** in frontmatter `sources` or body footnotes.
2. **No paywalled full-text** (IEEE PDF dumps, paid books).
3. **No PII** or doxxing content.
4. Prefer **defensive context** when describing attacks.
5. **imports/** is bot territory — fix the importer if sync will clobber you.
6. Keep pages focused; use `related` instead of mega-pages.

## Local validation

```bash
python scripts/validate_corpus.py
```

## Code of conduct

Be respectful. Security research is welcome; harassment and illegal how-to for harming systems you do not own is not.
