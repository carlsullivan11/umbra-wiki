#!/usr/bin/env python3
"""Import IEEE OUI / MAC-prefix registries into a machine-readable data file.

Usage:
  python scripts/importers/import_oui.py --out imports/ieee-oui/data
  python scripts/importers/import_oui.py --out imports/ieee-oui/data \
      --fixture scripts/fixtures/oui-sample.csv

Deliberately **data, not wiki pages** (docs/CLAUDE-NEXT-STAGES.md#S6): there are
~53,000 registrations. Emitting a markdown page per vendor prefix would bury the
readable corpus and help nobody; the MAC collector wants a lookup table.

## The correctness point: longest-prefix match

IEEE issues three block sizes, and the smaller ones are **carved out of** the
24-bit space:

| Registry | Prefix | Bits | Entries (2026-08) |
|---|---|---|---|
| MA-L | 6 hex | 24 | ~39,900 |
| MA-M | 7 hex | 28 | ~6,500 |
| MA-S | 9 hex | 36 | ~7,100 |

Measured on the live registries: **7,132 of 7,133 MA-S** and **6,420 of 6,548
MA-M** prefixes resolve to a *different* vendor than their 24-bit parent — the
parent is usually the umbrella "IEEE Registration Authority" block. So a
24-bit-only lookup returns the wrong vendor for ~13,500 prefixes.

`lookup_vendor()` therefore matches **longest prefix first** (36 → 28 → 24).
Any consumer of this file must do the same.

Sources:
  https://standards-oui.ieee.org/oui/oui.csv      (MA-L)
  https://standards-oui.ieee.org/oui28/mam.csv    (MA-M)
  https://standards-oui.ieee.org/oui36/oui36.csv  (MA-S)
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
import urllib.request
from datetime import date
from pathlib import Path

REGISTRIES = [
    ("MA-L", 24, "https://standards-oui.ieee.org/oui/oui.csv"),
    ("MA-M", 28, "https://standards-oui.ieee.org/oui28/mam.csv"),
    ("MA-S", 36, "https://standards-oui.ieee.org/oui36/oui36.csv"),
]
HEX_RE = re.compile(r"^[0-9A-F]+$")
# Prefix lengths in hex chars, longest first — the match order that matters.
PREFIX_LENS = (9, 7, 6)


def normalize_mac(value: str) -> str:
    """Strip separators and upper-case: 'a4:83:e7:...' -> 'A483E7...'."""
    return re.sub(r"[^0-9A-Fa-f]", "", value or "").upper()


def lookup_vendor(mac: str, table: dict[str, dict]) -> dict | None:
    """Resolve a MAC (or bare prefix) to its most specific registration.

    Longest prefix wins: an address inside an MA-S block must resolve to that
    vendor, not to the umbrella MA-L holder it sits under.
    """
    clean = normalize_mac(mac)
    if not clean:
        return None
    for n in PREFIX_LENS:
        if len(clean) >= n:
            hit = table.get(clean[:n])
            if hit:
                return hit
    return None


def load_table(csv_path: Path) -> dict[str, dict]:
    """Read a generated oui.csv back into a lookup dict."""
    table: dict[str, dict] = {}
    with csv_path.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            table[row["prefix"]] = {
                "prefix": row["prefix"],
                "bits": int(row["bits"]),
                "registry": row["registry"],
                "vendor": row["vendor"],
            }
    return table


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "umbra-wiki-importer/0.1"})
    with urllib.request.urlopen(req, timeout=300) as resp:  # noqa: S310
        return resp.read().decode("utf-8", "replace")


def parse_registry(text: str, registry: str, bits: int) -> list[tuple[str, int, str, str]]:
    out: list[tuple[str, int, str, str]] = []
    for row in csv.DictReader(text.splitlines()):
        prefix = (row.get("Assignment") or "").strip().upper()
        vendor = (row.get("Organization Name") or "").strip()
        if not prefix or not HEX_RE.match(prefix):
            continue
        # Registrations with no public org name are still useful signal —
        # "this prefix is registered but private" beats "unknown".
        out.append((prefix, bits, registry, vendor or "Private"))
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", type=Path, required=True, help="Output dir (imports/ieee-oui/data)")
    ap.add_argument("--fixture", type=Path, default=None,
                    help="Local generated oui.csv to re-emit (offline tests)")
    args = ap.parse_args(argv)

    rows: list[tuple[str, int, str, str]] = []
    counts: dict[str, int] = {}

    if args.fixture:
        with args.fixture.open(newline="", encoding="utf-8") as f:
            for r in csv.DictReader(f):
                rows.append((r["prefix"], int(r["bits"]), r["registry"], r["vendor"]))
                counts[r["registry"]] = counts.get(r["registry"], 0) + 1
    else:
        for registry, bits, url in REGISTRIES:
            parsed = parse_registry(fetch(url), registry, bits)
            counts[registry] = len(parsed)
            rows.extend(parsed)
            print(f"  {registry}: {len(parsed)} registrations")

    # IEEE's own listings contain a few prefixes registered to more than one
    # organisation — 080030 is a well-known legacy block shared by Network
    # Research Corp, RMIT and CERN, and 0001C8 appears twice after a rename.
    # Loading straight into a dict silently kept whichever sorted last, so a
    # lookup would confidently report one org and hide the others. Merge them
    # instead, so the table stays one-row-per-prefix without losing claimants.
    merged: dict[str, tuple[str, int, str, list[str]]] = {}
    for prefix, bits, registry, vendor in rows:
        if prefix in merged:
            vendors = merged[prefix][3]
            if vendor not in vendors:
                vendors.append(vendor)
        else:
            merged[prefix] = (prefix, bits, registry, [vendor])
    multi = sum(1 for v in merged.values() if len(v[3]) > 1)
    rows = [(p_, b, reg, " | ".join(vs)) for p_, b, reg, vs in merged.values()]

    # Sort longest prefix first so the file itself reflects match precedence,
    # then alphabetically for a stable diff between refreshes.
    rows.sort(key=lambda r: (-r[1], r[0]))

    args.out.mkdir(parents=True, exist_ok=True)
    csv_path = args.out / "oui.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["prefix", "bits", "registry", "vendor"])
        w.writerows(rows)

    manifest = {
        "source": "ieee-oui",
        "urls": {r: u for r, _b, u in REGISTRIES},
        "count": len(rows),
        "by_registry": counts,
        "shared_prefixes": multi,
        "format": "csv: prefix,bits,registry,vendor (sorted longest-prefix first)",
        "lookup_rule": "longest prefix wins (36 -> 28 -> 24 bits)",
        "fetched_at": date.today().isoformat(),
    }
    (args.out / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    corpus_root = args.out.parent.parent.parent
    attr = corpus_root / "meta" / "attribution" / "ieee-oui.md"
    if attr.parent.is_dir():
        attr.write_text(
            f"""# IEEE OUI / MAC prefix attribution

- Source: IEEE Registration Authority public listings (MA-L, MA-M, MA-S)
- URLs:
{chr(10).join(f"  - {u}" for _r, _b, u in REGISTRIES)}
- Entries: `{len(rows)}` ({", ".join(f"{k} {v}" for k, v in sorted(counts.items()))})
- `{multi}` prefix(es) are registered to more than one organisation in IEEE's
  own listings (e.g. the legacy `080030` shared by Network Research Corp, RMIT
  and CERN). Those rows list every claimant separated by ` | ` rather than
  silently keeping one.
- Stored as a single CSV lookup table, **not** as wiki pages — ~53k
  registrations would bury the readable corpus.
- **Lookup rule:** longest prefix wins (36 → 28 → 24 bits). MA-M/MA-S blocks are
  carved out of MA-L space, and on the live data 7,132/7,133 MA-S and
  6,420/6,548 MA-M prefixes have a different vendor than their 24-bit parent
  (usually the umbrella "IEEE Registration Authority"). A 24-bit-only lookup is
  therefore wrong for ~13,500 prefixes.
- Terms: IEEE publishes these listings publicly for identification purposes.
  Attribute IEEE; do not imply IEEE endorsement.
- Last importer run date: {date.today().isoformat()}
""",
            encoding="utf-8",
        )

    print(f"wrote {len(rows)} OUI entries → {csv_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
