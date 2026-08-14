# umbra-wiki

**MIT-licensed** cyber knowledge corpus for [Umbra](https://github.com/carlsullivan11/umbra).

Used by:
- `umbra lookup "ARP poisoning"`
- `umbra lookup CVE-2024-3400`
- Umbra web `/wiki` (product UI)

## Layout

```text
curated/     # human-written pages (PRs welcome; CODEOWNERS review)
imports/     # machine-generated from NVD, KEV, ATT&CK, CWE, OUI, RFCs…
meta/        # attribution + allowlists
scripts/     # importers run in CI
```

## Page format

See [SCHEMA.md](SCHEMA.md). YAML frontmatter + Markdown body.

## Update local CLI index

```bash
umbra wiki update --path /path/to/umbra-wiki
# or set UMBRA_WIKI_REPO / clone to ~/.umbra/wiki
umbra lookup "DNS spoofing"
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

- **curated/** — fix typos, add concepts, link techniques (human PRs)
- **imports/** — prefer improving importers; one-off edits get overwritten on next sync
- No paywalled standard full-text, no PII dumps, no exploit-only weaponization without defensive context

## Automation

GitHub Actions (see `.github/workflows/`) periodically import:

| Source | Path |
|--------|------|
| CISA KEV | `imports/cisa-kev/` |
| NVD CVE | `imports/nvd-cve/` (incremental) |
| MITRE ATT&CK | `imports/mitre-attack/` (planned) |
| CWE / OUI / RFC | planned |

Every import must update `meta/attribution/`.

## License

MIT — see [LICENSE](LICENSE). Upstream data retains its own terms; see `meta/attribution/`.
