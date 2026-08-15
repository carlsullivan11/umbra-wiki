#!/usr/bin/env python3
"""Import MITRE CWE weaknesses into umbra-wiki markdown pages.

Usage:
  python scripts/importers/import_cwe.py --out imports/mitre-cwe
  python scripts/importers/import_cwe.py --out imports/mitre-cwe \
      --fixture scripts/fixtures/cwe-sample.xml

Why this stage exists (docs/CLAUDE-NEXT-STAGES.md#S5): the NVD importer already
emits `related: [..., weakness/CWE-79]` on every CVE page that declares a CWE.
Until those pages exist those links dangle, so a reader following "what class of
bug is this?" hits nothing. This importer creates the target pages in the
`weakness/<CWE-ID>` namespace.

Design notes:

- **Both Weaknesses and Categories are imported.** Legacy CVEs (especially
  pre-2010) are classified against CWE *categories* such as CWE-399 "Resource
  Management Errors", which are separate XML elements from Weaknesses. Importing
  only Weaknesses left those NVD links dangling.
- **Deprecated/obsolete entries are skipped** in both kinds. CWE retires entries;
  publishing them would put dead classifications in front of someone triaging a
  real CVE. A link to a retired id therefore stays unresolved *on purpose* —
  that is a signal the source CVE uses an outdated taxonomy, not a bug.
- Only generated pages are committed. The source is a 2 MB zip that expands to a
  ~20 MB XML catalogue; it is fetched, parsed and discarded.
- The namespace `weakness/<ID>` is distinct from `cve/` and `technique/`, so
  three importers coexist without slug collisions.

Source: https://cwe.mitre.org/data/xml/cwec_latest.xml.zip
"""

from __future__ import annotations

import argparse
import io
import json
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
import zipfile
from datetime import date
from pathlib import Path

CWE_URL = "https://cwe.mitre.org/data/xml/cwec_latest.xml.zip"
RETIRED_STATUSES = {"deprecated", "obsolete"}


def _ns(root: ET.Element) -> str:
    return root.tag.split("}")[0].strip("{") + "}" if "}" in root.tag else ""


def _text(el: ET.Element | None) -> str:
    """Flatten an element's text, including nested markup like <xhtml:p>."""
    if el is None:
        return ""
    return re.sub(r"\s+", " ", "".join(el.itertext())).strip()


def _child(parent: ET.Element, ns: str, tag: str) -> ET.Element | None:
    return parent.find(f"{{{ns.rstrip('}')}}}{tag}" if ns else tag)


def _findall(parent: ET.Element, ns: str, path: str) -> list[ET.Element]:
    if ns:
        path = "/".join(f"{{{ns.rstrip('}')}}}{p}" for p in path.split("/"))
    return parent.findall(f".//{path}")


def is_retired(weakness: ET.Element) -> bool:
    return (weakness.get("Status") or "").strip().lower() in RETIRED_STATUSES


def consequences(weakness: ET.Element, ns: str) -> list[str]:
    out: list[str] = []
    for cons in _findall(weakness, ns, "Consequence"):
        scopes = [_text(s) for s in _findall(cons, ns, "Scope")]
        impacts = [_text(i) for i in _findall(cons, ns, "Impact")]
        if scopes or impacts:
            line = f"{', '.join(scopes) or '—'}: {', '.join(impacts) or '—'}"
            if line not in out:
                out.append(line)
    return out[:6]


def mitigations(weakness: ET.Element, ns: str) -> list[str]:
    out: list[str] = []
    for mit in _findall(weakness, ns, "Mitigation"):
        desc = _text(_child(mit, ns, "Description"))
        phase = _text(_child(mit, ns, "Phase"))
        if desc:
            out.append(f"**{phase or 'General'}** — {desc}")
    return out[:5]


def page_for(weakness: ET.Element, ns: str, kind: str = "Weakness") -> str | None:
    cwe_num = (weakness.get("ID") or "").strip()
    if not cwe_num.isdigit():
        return None
    cwe_id = f"CWE-{cwe_num}"
    name = (weakness.get("Name") or cwe_id).strip()
    abstraction = weakness.get("Abstraction") or ""
    status = weakness.get("Status") or ""
    desc = _text(_child(weakness, ns, "Description"))
    extended = _text(_child(weakness, ns, "Extended_Description"))
    likelihood = _text(_child(weakness, ns, "Likelihood_Of_Exploit"))
    cons = consequences(weakness, ns)
    mits = mitigations(weakness, ns)
    today = date.today().isoformat()

    title = f"{cwe_id} — {name}".replace('"', "'")
    summary = (desc or name)[:200].replace('"', "'")

    cons_block = "\n".join(f"- {c}" for c in cons) or "- (none listed)"
    mit_block = "\n\n".join(mits) or "(none listed)"

    kind_label = "weakness" if kind == "Weakness" else "category"
    body = f"""# {cwe_id}: {name}

**MITRE CWE {kind_label}**

| | |
|--|--|
| Kind | {kind} |
| Abstraction | {abstraction or "—"} |
| Status | {status or "—"} |
| Likelihood of exploit | {likelihood or "—"} |

## Description

{desc or "(no description published)"}

{extended}

## Common consequences

{cons_block}

## Mitigations

{mit_block}

## References

- CWE page: https://cwe.mitre.org/data/definitions/{cwe_num}.html
- CWE list: https://cwe.mitre.org/data/index.html
"""

    fm = f"""---
slug: weakness/{cwe_id}
title: "{title}"
page_type: weakness
tags: [cwe, weakness, mitre]
cwe_ids: [{cwe_id}]
related: [concept/cve-anatomy]
provenance: imported
import_source: mitre-cwe
import_id: {cwe_id}
updated_at: {today}
summary: "{summary}"
sources:
  - name: MITRE CWE
    url: https://cwe.mitre.org/data/definitions/{cwe_num}.html
---

"""
    return fm + body


def load_catalog(fixture: Path | None) -> ET.Element:
    if fixture:
        return ET.fromstring(fixture.read_text(encoding="utf-8"))
    req = urllib.request.Request(CWE_URL, headers={"User-Agent": "umbra-wiki-importer/0.1"})
    with urllib.request.urlopen(req, timeout=300) as resp:  # noqa: S310
        blob = resp.read()
    with zipfile.ZipFile(io.BytesIO(blob)) as z:
        return ET.fromstring(z.read(z.namelist()[0]))


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", type=Path, required=True, help="Output dir (imports/mitre-cwe)")
    ap.add_argument("--fixture", type=Path, default=None, help="Local CWE XML (skip network)")
    ap.add_argument("--limit", type=int, default=0, help="Max pages (0 = all)")
    ap.add_argument(
        "--include-retired",
        action="store_true",
        help="Also import deprecated/obsolete weaknesses (default: skip)",
    )
    args = ap.parse_args(argv)

    root = load_catalog(args.fixture)
    ns = _ns(root)
    # Categories too: legacy CVEs reference them (e.g. CWE-399), and importing
    # only Weaknesses leaves those cross-links dangling.
    entries = [(w, "Weakness") for w in _findall(root, ns, "Weakness")]
    entries += [(c, "Category") for c in _findall(root, ns, "Category")]

    args.out.mkdir(parents=True, exist_ok=True)
    written = skipped_retired = 0
    counts = {"Weakness": 0, "Category": 0}
    for el, kind in entries:
        if is_retired(el) and not args.include_retired:
            skipped_retired += 1
            continue
        page = page_for(el, ns, kind)
        if not page:
            continue
        cwe_id = f"CWE-{el.get('ID')}"
        (args.out / f"{cwe_id}.md").write_text(page, encoding="utf-8")
        written += 1
        counts[kind] += 1
        if args.limit and written >= args.limit:
            break

    manifest = {
        "source": "mitre-cwe",
        "url": CWE_URL if not args.fixture else str(args.fixture),
        "count": written,
        "weaknesses": counts["Weakness"],
        "categories": counts["Category"],
        "skipped_retired": skipped_retired,
        "catalog_version": root.get("Version"),
        "catalog_date": root.get("Date"),
        "fetched_at": date.today().isoformat(),
    }
    (args.out / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    corpus_root = args.out.parent.parent if args.out.parent.name == "imports" else Path(".")
    attr = corpus_root / "meta" / "attribution" / "mitre-cwe.md"
    if attr.parent.is_dir():
        attr.write_text(
            f"""# MITRE CWE attribution

- Source: MITRE Common Weakness Enumeration (CWE™), version {root.get("Version")}
- URL: {CWE_URL}
- Imported pages: `{written}` (`{counts["Weakness"]}` weaknesses + `{counts["Category"]}` categories; see imports/mitre-cwe/manifest.json)
- Skipped: `{skipped_retired}` deprecated/obsolete entries — retired
  classifications are deliberately not published.
- Only generated pages are committed; the source catalogue is not.
- Terms: CWE™ is a trademark of The MITRE Corporation. CWE is free to use and
  redistribute with attribution; MITRE does not endorse this project.
- Last importer run date: {date.today().isoformat()}
""",
            encoding="utf-8",
        )

    print(f"wrote {written} CWE pages → {args.out} (skipped {skipped_retired} retired)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
