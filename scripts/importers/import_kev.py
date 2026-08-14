#!/usr/bin/env python3
"""Import CISA KEV catalog into umbra-wiki markdown pages.

Usage:
  python scripts/importers/import_kev.py --out imports/cisa-kev
  python scripts/importers/import_kev.py --out imports/cisa-kev --fixture path/to/kev.json

Data source: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.request
from datetime import date
from pathlib import Path

KEV_URL = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"


def slugify_cve(cve_id: str) -> str:
    return f"cve/{cve_id.upper()}"


def page_for(vuln: dict) -> str:
    cve = vuln.get("cveID") or vuln.get("cveId") or ""
    name = vuln.get("vulnerabilityName") or cve
    vendor = vuln.get("vendorProject") or ""
    product = vuln.get("product") or ""
    desc = (vuln.get("shortDescription") or "").strip()
    required = vuln.get("requiredAction") or ""
    due = vuln.get("dueDate") or ""
    notes = vuln.get("notes") or ""
    date_added = vuln.get("dateAdded") or ""
    ransomware = vuln.get("knownRansomwareCampaignUse") or "Unknown"
    today = date.today().isoformat()
    slug = slugify_cve(cve)
    body = f"""# {cve}: {name}

**CISA Known Exploited Vulnerability (KEV)**

| | |
|--|--|
| Vendor / project | {vendor} |
| Product | {product} |
| Date added | {date_added} |
| Due date | {due} |
| Ransomware campaign use | {ransomware} |

## Description

{desc}

## Required action (CISA)

{required}

## Notes

{notes}

## References

- NVD: https://nvd.nist.gov/vuln/detail/{cve}
- KEV catalog: https://www.cisa.gov/known-exploited-vulnerabilities-catalog
"""
    # YAML-safe title quotes
    title = f"{cve} — {name}".replace('"', "'")
    fm = f"""---
slug: {slug}
title: "{title}"
page_type: cve
tags: [cve, kev, cisa]
cve_ids: [{cve}]
related: [concept/cve-anatomy]
provenance: imported
import_source: kev
import_id: {cve}
updated_at: {today}
sources:
  - name: CISA KEV
    url: https://www.cisa.gov/known-exploited-vulnerabilities-catalog
---

"""
    return fm + body


def load_catalog(fixture: Path | None) -> dict:
    if fixture:
        return json.loads(fixture.read_text(encoding="utf-8"))
    req = urllib.request.Request(KEV_URL, headers={"User-Agent": "umbra-wiki-importer/0.1"})
    with urllib.request.urlopen(req, timeout=120) as resp:  # noqa: S310
        return json.loads(resp.read().decode("utf-8"))


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", type=Path, required=True, help="Output directory (imports/cisa-kev)")
    ap.add_argument("--fixture", type=Path, default=None, help="Local KEV JSON (skip network)")
    ap.add_argument("--limit", type=int, default=0, help="Max vulnerabilities (0=all)")
    args = ap.parse_args(argv)

    data = load_catalog(args.fixture)
    vulns = data.get("vulnerabilities") or []
    if args.limit:
        vulns = vulns[: args.limit]
    args.out.mkdir(parents=True, exist_ok=True)
    count = 0
    for v in vulns:
        cve = v.get("cveID") or v.get("cveId")
        if not cve or not re.match(r"CVE-\d{4}-\d+", cve, re.I):
            continue
        year = cve.split("-")[1]
        dest_dir = args.out / year
        dest_dir.mkdir(parents=True, exist_ok=True)
        path = dest_dir / f"{cve.upper()}.md"
        path.write_text(page_for(v), encoding="utf-8")
        count += 1

    manifest = {
        "source": "cisa-kev",
        "url": KEV_URL if not args.fixture else str(args.fixture),
        "count": count,
        "catalogVersion": data.get("catalogVersion"),
        "dateReleased": data.get("dateReleased"),
        "fetched_at": date.today().isoformat(),
    }
    (args.out / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    attr = args.out.parent.parent / "meta" / "attribution" / "cisa-kev.md"
    if attr.parent.is_dir():
        attr.write_text(
            f"""# CISA KEV attribution

- Source: CISA Known Exploited Vulnerabilities Catalog
- URL: {KEV_URL}
- Imported pages: `{count}` (see imports/cisa-kev/manifest.json)
- Terms: U.S. government work; verify current CISA usage guidelines
- Last importer run date: {date.today().isoformat()}
""",
            encoding="utf-8",
        )
    print(f"wrote {count} KEV pages → {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
