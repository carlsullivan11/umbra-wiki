# IEEE OUI / MAC prefix data

Machine-readable lookup table for MAC address → vendor resolution. Feeds the
planned MAC collector (vault: `Umbra-MAC-Lookup`, stage S13).

**This is data, not wiki pages** — ~53k registrations would bury the readable
corpus, and the consumer wants a table.

## Files

| File | Contents |
|------|----------|
| `data/oui.csv` | `prefix,bits,registry,vendor` — sorted longest prefix first |
| `data/manifest.json` | counts per registry, source URLs, lookup rule, fetch date |

## Lookup rule — read this before using the file

**Longest prefix wins: 36 → 28 → 24 bits.**

IEEE issues three block sizes and the smaller ones are carved out of the 24-bit
space. On the live registries, **7,132 of 7,133 MA-S** and **6,420 of 6,548
MA-M** prefixes belong to a different vendor than their 24-bit parent — the
parent is usually the umbrella "IEEE Registration Authority". A 24-bit-only
lookup is therefore **wrong for ~13,500 prefixes**.

`scripts/importers/import_oui.py` exposes `lookup_vendor(mac, table)` and
`load_table(path)` implementing this correctly; reuse them rather than
reimplementing the match.

```python
import sys; sys.path.insert(0, "scripts/importers")
import import_oui
table = import_oui.load_table("imports/ieee-oui/data/oui.csv")
import_oui.lookup_vendor("8C:1F:64:AF:A1:23", table)
# {'prefix': '8C1F64AFA', 'bits': 36, 'registry': 'MA-S', 'vendor': 'DATA ELECTRONIC DEVICES, INC'}
```

## Shared prefixes

A couple of prefixes are registered to more than one organisation in IEEE's own
listings — the legacy `080030` is shared by Network Research Corp, RMIT and
CERN. Those rows list every claimant separated by ` | ` rather than silently
keeping one.

## Refresh

```bash
python scripts/importers/import_oui.py --out imports/ieee-oui/data
python scripts/validate_corpus.py
```

Automated weekly by `.github/workflows/import-oui.yml`.
Attribution: `meta/attribution/ieee-oui.md`.
