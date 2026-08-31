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


def cwe_ids(vuln: dict) -> list[str]:
    """CWE ids CISA records for this vulnerability.

    KEV grew a `cwes` field, and it carries one for 1,512 of 1,687 entries. That
    is the cheapest possible source for the CVE→CWE hop: no second API, no rate
    limit, already in the feed this importer downloads. NVD would mean 1,687
    requests at 5 per 30 seconds without a key — nearly three hours to fetch
    something CISA is already handing us.
    """
    out = []
    for raw in vuln.get("cwes") or []:
        text = str(raw).strip().upper()
        if re.fullmatch(r"CWE-\d{1,4}", text):
            out.append(text)
    return sorted(set(out), key=lambda c: int(c.split("-")[1]))


def page_for(vuln: dict, known_slugs: set[str] | None = None) -> str:
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

    cwes = cwe_ids(vuln)
    # Only links that resolve — a cross-reference that dead-ends looks like a
    # traversal and is not one. Same rule as the CAPEC importer.
    cwe_slugs = [f"weakness/{c}" for c in cwes]
    if known_slugs is not None:
        cwe_slugs = [s for s in cwe_slugs if s in known_slugs]

    # This is the first hop of the chain, and the only one a reader previously
    # had to make by hand: CVE → CWE → CAPEC → ATT&CK. The other three already
    # resolve inside this corpus.
    if cwes:
        chain = (
            "\n## Weakness behind it\n\n"
            "CISA records this vulnerability as an instance of "
            + ", ".join(f"[{c}](/wiki/p/weakness/{c})" for c in cwes)
            + ". From there the chain continues into CAPEC attack patterns and "
            "ATT&CK techniques, all inside this corpus.\n"
        )
    else:
        # 175 KEV entries carry no CWE. Saying so beats an absent section that
        # reads as "there is no weakness class", which would be false.
        chain = (
            "\n## Weakness behind it\n\n"
            "CISA has not recorded a CWE for this entry, so the CVE → CWE → "
            "CAPEC → ATT&CK chain cannot be walked from here. That is a gap in "
            "the catalogue, not evidence the vulnerability has no weakness "
            "class — check the NVD record below.\n"
        )

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

{chain}
## References

- NVD: https://nvd.nist.gov/vuln/detail/{cve}
- KEV catalog: https://www.cisa.gov/known-exploited-vulnerabilities-catalog
"""
    # YAML-safe title quotes
    title = f"{cve} — {name}".replace('"', "'")
    cwe_line = f"cwe_ids: [{', '.join(cwes)}]\n" if cwes else ""
    related = ", ".join(["concept/cve-anatomy"] + cwe_slugs)
    fm = f"""---
slug: {slug}
title: "{title}"
page_type: cve
tags: [cve, kev, cisa]
cve_ids: [{cve}]
{cwe_line}related: [{related}]
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


def existing_slugs(root: Path) -> set[str]:
    """Every slug already in the corpus, so CWE links can be checked."""
    slugs = set()
    for path in root.rglob("*.md"):
        try:
            head = path.read_text(encoding="utf-8")[:400]
        except OSError:
            continue
        m = re.search(r"^slug:\s*(\S+)", head, re.M)
        if m:
            slugs.add(m.group(1).strip())
    return slugs


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
    ap.add_argument("--corpus", type=Path, default=None,
                    help="Corpus root for CWE link checking (default: --out's grandparent)")
    args = ap.parse_args(argv)

    data = load_catalog(args.fixture)
    vulns = data.get("vulnerabilities") or []
    if args.limit:
        vulns = vulns[: args.limit]
    corpus_root = args.corpus or args.out.parent.parent
    known = existing_slugs(corpus_root) if corpus_root.is_dir() else None

    args.out.mkdir(parents=True, exist_ok=True)
    count = 0
    with_cwe = 0
    cwe_links = 0
    for v in vulns:
        cve = v.get("cveID") or v.get("cveId")
        if not cve or not re.match(r"CVE-\d{4}-\d+", cve, re.I):
            continue
        year = cve.split("-")[1]
        dest_dir = args.out / year
        dest_dir.mkdir(parents=True, exist_ok=True)
        path = dest_dir / f"{cve.upper()}.md"
        path.write_text(page_for(v, known), encoding="utf-8")
        count += 1
        cwes = cwe_ids(v)
        if cwes:
            with_cwe += 1
            cwe_links += len(cwes)

    manifest = {
        "source": "cisa-kev",
        "url": KEV_URL if not args.fixture else str(args.fixture),
        "count": count,
        "catalogVersion": data.get("catalogVersion"),
        "dateReleased": data.get("dateReleased"),
        # Never a silent gap: 175 of 1,687 KEV entries carry no CWE, and the
        # chain cannot be walked from those. The number belongs in the record.
        "entries_with_cwe": with_cwe,
        "entries_without_cwe": count - with_cwe,
        "cwe_links": cwe_links,
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
