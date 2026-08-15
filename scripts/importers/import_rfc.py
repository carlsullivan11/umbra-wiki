#!/usr/bin/env python3
"""Import a curated list of RFCs into umbra-wiki markdown pages.

Usage:
  python scripts/importers/import_rfc.py --list lists/core-rfcs.txt --out imports/ietf-rfc
  python scripts/importers/import_rfc.py --list lists/core-rfcs.txt --out imports/ietf-rfc \
      --fixture scripts/fixtures/rfc-index-sample.xml

Design notes (docs/CLAUDE-NEXT-STAGES.md#S7):

- **Curated list, not a mirror.** There are ~9,800 RFCs; importing all of them
  would drown the corpus. `lists/core-rfcs.txt` is a human-edited file of the
  RFCs an operator actually meets doing this work — the protocols Umbra's
  collectors touch and the email-auth standards it reports on.
- **Obsolescence is surfaced, loudly.** Several core RFCs are superseded —
  RFC 7489 (DMARC) by 9989/9990/9991, RFC 8446 (TLS 1.3) by 9846, RFC 6844
  (CAA) by 8659. Publishing "RFC 8446 — TLS 1.3" with no indication it has been
  obsoleted would actively mislead, the same failure mode as importing retired
  CWE/ATT&CK entries. Obsoleted pages carry a banner and a link to the successor.
- **Abstract + links only, never full text.** The corpus rule is metadata and
  pointers, not reproduced documents.
- Doc ids in the index are **unpadded** (`RFC826`, not `RFC0826`), so ids are
  normalised before lookup — "826", "rfc 826", "RFC0826" all resolve.

Source: https://www.rfc-editor.org/rfc-index.xml
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from datetime import date
from pathlib import Path

RFC_INDEX_URL = "https://www.rfc-editor.org/rfc-index.xml"
RFC_NUM_RE = re.compile(r"(?:RFC[\s-]*)?0*(\d{1,5})", re.I)


def normalize_rfc_id(value: str) -> str | None:
    """'826' | 'rfc 826' | 'RFC0826' -> 'RFC826' (index ids are unpadded)."""
    m = RFC_NUM_RE.fullmatch((value or "").strip())
    if not m:
        return None
    return f"RFC{int(m.group(1))}"


def read_list(path: Path) -> list[str]:
    """Parse the curated list: one RFC per line, '#' comments, blanks ignored."""
    out: list[str] = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.split("#", 1)[0].strip()
        if not line:
            continue
        rid = normalize_rfc_id(line)
        if rid and rid not in out:
            out.append(rid)
    return out


def _ns(root: ET.Element) -> str:
    return root.tag.split("}")[0].strip("{") if "}" in root.tag else ""


def _text(el: ET.Element | None) -> str:
    if el is None:
        return ""
    return re.sub(r"\s+", " ", "".join(el.itertext())).strip()


def _multi(entry: ET.Element, ns: str, tag: str) -> list[str]:
    """`obsoleted-by` etc. pack several ids into one whitespace-separated node."""
    tokens: list[str] = []
    q = f"{{{ns}}}{tag}" if ns else tag
    for el in entry.findall(q):
        tokens.extend(_text(el).split())
    return [t for t in tokens if t]


def index_entries(root: ET.Element) -> dict[str, ET.Element]:
    ns = _ns(root)
    q = f"{{{ns}}}rfc-entry" if ns else "rfc-entry"
    did = f"{{{ns}}}doc-id" if ns else "doc-id"
    out: dict[str, ET.Element] = {}
    for e in root.findall(q):
        key = normalize_rfc_id(_text(e.find(did)))
        if key:
            out[key] = e
    return out


def page_for(rfc_id: str, entry: ET.Element, ns: str) -> str:
    def field(tag: str) -> str:
        return _text(entry.find(f"{{{ns}}}{tag}" if ns else tag))

    num = rfc_id[3:]
    title = field("title") or rfc_id
    abstract = field("abstract")
    status = field("current-status")
    pub_status = field("publication-status")
    published = field("date")
    stream = field("stream")
    obsoleted_by = _multi(entry, ns, "obsoleted-by")
    updated_by = _multi(entry, ns, "updated-by")
    obsoletes = _multi(entry, ns, "obsoletes")
    keywords = [k for k in (_text(k) for k in entry.findall(f"{{{ns}}}keyword" if ns else "keyword")) if k]

    today = date.today().isoformat()
    safe_title = title.replace('"', "'")
    summary = (abstract or title)[:200].replace('"', "'")

    # An obsoleted standard presented as current is worse than no page at all.
    banner = ""
    if obsoleted_by:
        succ = ", ".join(f"[{o}](rfc/{o})" for o in obsoleted_by)
        banner = (
            f"> ⚠️ **Obsoleted.** This RFC has been superseded by {succ}. "
            f"Read the successor before relying on this document.\n\n"
        )

    related = ["concept/cve-anatomy"] if False else []
    related += [f"rfc/{o}" for o in obsoleted_by + obsoletes][:6]

    body = f"""# {rfc_id}: {title}

{banner}**IETF Request for Comments**

| | |
|--|--|
| Status | {status or "—"} |
| Publication status | {pub_status or "—"} |
| Published | {published or "—"} |
| Stream | {stream or "—"} |
| Obsoletes | {", ".join(obsoletes) or "—"} |
| Obsoleted by | {", ".join(obsoleted_by) or "—"} |
| Updated by | {", ".join(updated_by) or "—"} |

## Abstract

{abstract or "(no abstract published in the RFC index)"}

## Official sources

- Info page: https://www.rfc-editor.org/info/rfc{num}
- Full text: https://www.rfc-editor.org/rfc/rfc{num}.txt
- HTML: https://www.rfc-editor.org/rfc/rfc{num}.html

_Abstract and metadata are reproduced from the public RFC index; the full text
is linked, not copied._
"""

    rel = ", ".join(dict.fromkeys(related))
    fm = f"""---
slug: rfc/{rfc_id}
title: "{rfc_id} — {safe_title}"
page_type: rfc
tags: [rfc, ietf, standard{"".join(f", {k.lower().replace(' ', '-')}" for k in keywords[:4])}]
standards: [{rfc_id}]
related: [{rel}]
provenance: imported
import_source: ietf-rfc
import_id: {rfc_id}
updated_at: {today}
summary: "{summary}"
sources:
  - name: RFC Editor
    url: https://www.rfc-editor.org/info/rfc{num}
---

"""
    return fm + body


def load_index(fixture: Path | None) -> ET.Element:
    if fixture:
        return ET.fromstring(fixture.read_text(encoding="utf-8"))
    req = urllib.request.Request(RFC_INDEX_URL, headers={"User-Agent": "umbra-wiki-importer/0.1"})
    with urllib.request.urlopen(req, timeout=300) as resp:  # noqa: S310
        return ET.fromstring(resp.read())


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", type=Path, required=True, help="Output dir (imports/ietf-rfc)")
    ap.add_argument("--list", dest="list_path", type=Path, required=True,
                    help="Curated RFC list (lists/core-rfcs.txt)")
    ap.add_argument("--fixture", type=Path, default=None, help="Local rfc-index.xml (skip network)")
    args = ap.parse_args(argv)

    wanted = read_list(args.list_path)
    root = load_index(args.fixture)
    ns = _ns(root)
    entries = index_entries(root)

    args.out.mkdir(parents=True, exist_ok=True)
    written, missing, obsoleted = 0, [], []
    for rid in wanted:
        entry = entries.get(rid)
        if entry is None:
            missing.append(rid)
            continue
        (args.out / f"{rid}.md").write_text(page_for(rid, entry, ns), encoding="utf-8")
        written += 1
        if _multi(entry, ns, "obsoleted-by"):
            obsoleted.append(rid)

    manifest = {
        "source": "ietf-rfc",
        "url": RFC_INDEX_URL if not args.fixture else str(args.fixture),
        "list": str(args.list_path),
        "requested": len(wanted),
        "count": written,
        "missing": missing,
        "obsoleted_pages": obsoleted,
        "curated": True,
        "fetched_at": date.today().isoformat(),
    }
    (args.out / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    corpus_root = args.out.parent.parent if args.out.parent.name == "imports" else Path(".")
    attr = corpus_root / "meta" / "attribution" / "ietf-rfc.md"
    if attr.parent.is_dir():
        attr.write_text(
            f"""# IETF RFC attribution

- Source: RFC Editor public index ({RFC_INDEX_URL})
- Imported pages: `{written}` of `{len(wanted)}` requested (curated list:
  `{args.list_path}`) — **not** a mirror of the ~9,800 published RFCs.
- `{len(obsoleted)}` imported RFC(s) are obsoleted by a later document; those
  pages carry a warning banner and link the successor.
- **Abstracts and metadata only.** Full text is linked to rfc-editor.org, never
  copied into this corpus.
- Terms: RFCs are published by the IETF/RFC Editor and are freely
  redistributable; see the IETF Trust legal provisions (BCP 78/79).
- Last importer run date: {date.today().isoformat()}
""",
            encoding="utf-8",
        )

    print(f"wrote {written}/{len(wanted)} RFC pages → {args.out}"
          f" ({len(obsoleted)} obsoleted, {len(missing)} missing)")
    if missing:
        print(f"  missing from index: {', '.join(missing)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
