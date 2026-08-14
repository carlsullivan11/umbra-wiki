#!/usr/bin/env python3
"""Import NVD CVE records into umbra-wiki markdown pages.

Usage:
  # incremental: CVEs modified in the last 7 days, capped
  python scripts/importers/import_nvd.py --out imports/nvd-cve

  # explicit window / cap
  python scripts/importers/import_nvd.py --out imports/nvd-cve --days 30 --limit 500

  # offline (tests / CI without network)
  python scripts/importers/import_nvd.py --out imports/nvd-cve --fixture scripts/fixtures/nvd-sample.json

Design constraints (docs/CLAUDE-NEXT-STAGES.md#S3):

- **Capped and incremental, never the whole history.** NVD holds ~377k CVEs;
  dumping them would bloat the repo and be useless to read. Default is "CVEs
  modified in the last N days", hard-capped by --limit.
- **Never collides with an existing page.** KEV already emits `cve/<ID>` slugs
  for 1600+ CVEs. Two pages with one slug used to abort the entire index
  rebuild (IntegrityError) and leave every lookup empty; the indexer now
  tolerates it, but a duplicate page is still wrong. KEV wins on purpose — an
  actively-exploited CVE with a required action is higher signal than the raw
  NVD record — so this importer SKIPS any CVE already present in the corpus.
- Polite to NVD: paged with a delay between requests (the public rate limit is
  5 requests / 30s without an API key). Set NVD_API_KEY to go faster.

Data source: https://services.nvd.nist.gov/rest/json/cves/2.0
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

NVD_URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"
CVE_RE = re.compile(r"^CVE-\d{4}-\d{4,}$", re.I)
# Public limit is 5 requests / 30s; with a key it is 50 / 30s.
SLEEP_NO_KEY = 6.5
SLEEP_WITH_KEY = 0.8
PAGE_SIZE = 200


def existing_cve_ids(corpus_root: Path) -> set[str]:
    """CVE ids that already have a page anywhere in the corpus.

    Cheap and importer-agnostic: read the `import_id`/`slug` of every markdown
    file under imports/ and curated/ rather than assuming only KEV exists.
    """
    found: set[str] = set()
    for base in ("imports", "curated"):
        root = corpus_root / base
        if not root.is_dir():
            continue
        for path in root.rglob("*.md"):
            m = CVE_RE.match(path.stem.upper())
            if m:
                found.add(path.stem.upper())
    return found


def _first_english(descriptions: list[dict]) -> str:
    for d in descriptions or []:
        if (d.get("lang") or "").lower().startswith("en"):
            return (d.get("value") or "").strip()
    return ""


def _best_cvss(metrics: dict) -> tuple[str, str, str]:
    """Return (version, score, vector) preferring the newest CVSS available."""
    for key, label in (
        ("cvssMetricV40", "4.0"),
        ("cvssMetricV31", "3.1"),
        ("cvssMetricV30", "3.0"),
        ("cvssMetricV2", "2.0"),
    ):
        entries = (metrics or {}).get(key) or []
        if entries:
            data = entries[0].get("cvssData") or {}
            score = data.get("baseScore")
            sev = data.get("baseSeverity") or entries[0].get("baseSeverity") or ""
            vector = data.get("vectorString") or ""
            if score is not None:
                return label, f"{score} {sev}".strip(), vector
    return "", "", ""


def _cwes(weaknesses: list[dict]) -> list[str]:
    out: list[str] = []
    for w in weaknesses or []:
        for desc in w.get("description") or []:
            val = (desc.get("value") or "").strip()
            if val.upper().startswith("CWE-") and val not in out:
                out.append(val)
    return out


def page_for(cve: dict) -> str:
    cve_id = (cve.get("id") or "").upper()
    desc = _first_english(cve.get("descriptions") or [])
    published = (cve.get("published") or "")[:10]
    modified = (cve.get("lastModified") or "")[:10]
    status = cve.get("vulnStatus") or ""
    version, score, vector = _best_cvss(cve.get("metrics") or {})
    cwes = _cwes(cve.get("weaknesses") or [])
    refs = [r.get("url") for r in (cve.get("references") or []) if r.get("url")][:8]
    today = date.today().isoformat()

    title = f"{cve_id} — NVD record".replace('"', "'")
    summary_line = desc.split(". ")[0][:200] if desc else cve_id

    ref_block = "\n".join(f"- {u}" for u in refs) or "- (none listed)"
    cwe_block = ", ".join(cwes) if cwes else "—"
    cwe_related = "".join(f", weakness/{c.upper()}" for c in cwes)

    body = f"""# {cve_id}

**NVD vulnerability record**

| | |
|--|--|
| Published | {published} |
| Last modified | {modified} |
| Status | {status} |
| CVSS v{version or '—'} | {score or '—'} |
| Vector | `{vector or '—'}` |
| CWE | {cwe_block} |

## Description

{desc or '(no English description published)'}

## References

{ref_block}

## Sources

- NVD detail: https://nvd.nist.gov/vuln/detail/{cve_id}
- NVD API 2.0: {NVD_URL}?cveId={cve_id}
"""
    fm = f"""---
slug: cve/{cve_id}
title: "{title}"
page_type: cve
tags: [cve, nvd]
cve_ids: [{cve_id}]
related: [concept/cve-anatomy{cwe_related}]
provenance: imported
import_source: nvd
import_id: {cve_id}
updated_at: {today}
summary: "{summary_line.replace('"', "'")}"
sources:
  - name: NVD
    url: https://nvd.nist.gov/vuln/detail/{cve_id}
---

"""
    return fm + body


def fetch_page(params: dict, api_key: str | None) -> dict:
    url = f"{NVD_URL}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"User-Agent": "umbra-wiki-importer/0.1"})
    if api_key:
        req.add_header("apiKey", api_key)
    with urllib.request.urlopen(req, timeout=120) as resp:  # noqa: S310
        return json.loads(resp.read().decode("utf-8"))


def collect_cves(days: int, limit: int, api_key: str | None) -> list[dict]:
    """Page through recently-modified CVEs up to `limit`."""
    end = datetime.now(timezone.utc)
    start = end - timedelta(days=days)
    fmt = "%Y-%m-%dT%H:%M:%S.000"
    sleep_s = SLEEP_WITH_KEY if api_key else SLEEP_NO_KEY

    out: list[dict] = []
    start_index = 0
    while len(out) < limit:
        params = {
            "lastModStartDate": start.strftime(fmt),
            "lastModEndDate": end.strftime(fmt),
            "resultsPerPage": min(PAGE_SIZE, limit - len(out)),
            "startIndex": start_index,
        }
        data = fetch_page(params, api_key)
        vulns = data.get("vulnerabilities") or []
        if not vulns:
            break
        out.extend(v.get("cve") or {} for v in vulns)
        start_index += len(vulns)
        total = int(data.get("totalResults") or 0)
        print(f"  fetched {len(out)}/{min(limit, total)} (of {total} modified in {days}d)")
        if start_index >= total:
            break
        if len(out) < limit:
            time.sleep(sleep_s)
    return out[:limit]


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", type=Path, required=True, help="Output dir (imports/nvd-cve)")
    ap.add_argument("--fixture", type=Path, default=None, help="Local NVD JSON (skip network)")
    ap.add_argument("--days", type=int, default=7, help="Look back N days by lastModified")
    ap.add_argument("--limit", type=int, default=200, help="Hard cap on pages written")
    ap.add_argument(
        "--allow-duplicates",
        action="store_true",
        help="Write pages even if the CVE already exists (default: skip, KEV wins)",
    )
    args = ap.parse_args(argv)

    api_key = os.environ.get("NVD_API_KEY") or None
    corpus_root = args.out.parent.parent if args.out.parent.name == "imports" else Path(".")

    if args.fixture:
        data = json.loads(args.fixture.read_text(encoding="utf-8"))
        cves = [v.get("cve") or {} for v in (data.get("vulnerabilities") or [])][: args.limit]
        print(f"  fixture: {len(cves)} CVE(s)")
    else:
        cves = collect_cves(args.days, args.limit, api_key)

    already = set() if args.allow_duplicates else existing_cve_ids(corpus_root)
    if already:
        print(f"  corpus already covers {len(already)} CVE(s); those will be skipped")

    args.out.mkdir(parents=True, exist_ok=True)
    written = skipped = 0
    for cve in cves:
        cve_id = (cve.get("id") or "").upper()
        if not CVE_RE.match(cve_id):
            continue
        if cve_id in already:
            skipped += 1
            continue
        year = cve_id.split("-")[1]
        dest = args.out / year
        dest.mkdir(parents=True, exist_ok=True)
        (dest / f"{cve_id}.md").write_text(page_for(cve), encoding="utf-8")
        written += 1

    manifest = {
        "source": "nvd-cve",
        "url": NVD_URL,
        "count": written,
        "skipped_existing": skipped,
        "window_days": args.days,
        "limit": args.limit,
        "incremental": True,
        "fetched_at": date.today().isoformat(),
    }
    (args.out / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    attr = corpus_root / "meta" / "attribution" / "nvd-cve.md"
    if attr.parent.is_dir():
        attr.write_text(
            f"""# NVD CVE attribution

- Source: NIST National Vulnerability Database (NVD), API 2.0
- URL: {NVD_URL}
- Imported pages: `{written}` (see imports/nvd-cve/manifest.json)
- Import mode: **incremental** — CVEs modified in the last {args.days} day(s),
  capped at {args.limit} per run. The full catalogue (~377k CVEs) is
  deliberately never dumped.
- CVEs already covered by another importer (e.g. CISA KEV) are skipped so one
  CVE has exactly one page.
- Terms: NVD data is public domain (U.S. government work); NVD requests
  attribution and does not endorse derived products.
- Last importer run date: {date.today().isoformat()}
""",
            encoding="utf-8",
        )

    print(f"wrote {written} NVD pages → {args.out} (skipped {skipped} already covered)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
