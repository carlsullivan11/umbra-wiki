#!/usr/bin/env python3
"""Import MITRE D3FEND defensive techniques, mapped to the ATT&CK corpus.

Usage:
  python scripts/importers/import_d3fend.py --out imports/mitre-d3fend
  python scripts/importers/import_d3fend.py --out imports/mitre-d3fend --offline

**The hop after ATT&CK.** The corpus already walks

    CVE → CWE → CAPEC → ATT&CK technique

which ends at *what the adversary does*. For a tool whose whole framing is
defensive, stopping there is the wrong place. D3FEND is MITRE's countermeasure
knowledge base: 272 defensive techniques, each countering specific ATT&CK
techniques. It turns the chain's last hop into **"and here is what stops it"**.

**Getting the mapping is the awkward part, and worth writing down.** The public
`d3fend.json` ontology carries the 272 defensive techniques with definitions,
and 1,547 offensive technique classes — but *not* the `counters` edges between
them. Those are inferred by D3FEND's reasoner and only materialise through the
per-technique API the site's own UI calls:

    https://d3fend.mitre.org/api/offensive-technique/attack/T1190.json

So the mapping is fetched one technique at a time, for the techniques this
corpus actually holds (697, not all 1,547), at one request per second, and
cached to disk. A re-run costs nothing. This is the same "own the data" trade
the CT and abuse.ch lakes make: pay the fetch once, never depend on the source
at lookup time.

**Only links that resolve**, same rule as the CAPEC and KEV importers. A
countermeasure claiming to counter a technique this corpus does not carry would
look like a traversal and dead-end.

Sources:
  https://d3fend.mitre.org/ontologies/d3fend.json
  https://d3fend.mitre.org/api/offensive-technique/attack/<ID>.json
"""

from __future__ import annotations

import argparse
import json
import re
import time
import urllib.request
from datetime import date
from pathlib import Path

ONTOLOGY_URL = "https://d3fend.mitre.org/ontologies/d3fend.json"
API_TEMPLATE = "https://d3fend.mitre.org/api/offensive-technique/attack/{tid}.json"

#: One request per second. MITRE serves this endpoint for their own UI; 697
#: sequential calls is a courtesy pace, not a crawl.
POLITE_DELAY_S = 1.0

_WS = re.compile(r"\s+")


def _clean(text: str) -> str:
    return _WS.sub(" ", (text or "").strip())


def fetch_json(url: str, timeout: float = 120.0):
    req = urllib.request.Request(url, headers={"User-Agent": "umbra-wiki-importer/0.1"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:  # noqa: S310
        return json.loads(resp.read().decode("utf-8"))


def load_ontology(cache: Path, offline: bool):
    """Definitions and labels for the D3-* techniques."""
    if cache.is_file():
        return json.loads(cache.read_text(encoding="utf-8"))
    if offline:
        raise SystemExit(f"--offline but no cached ontology at {cache}")
    data = fetch_json(ONTOLOGY_URL)
    cache.parent.mkdir(parents=True, exist_ok=True)
    cache.write_text(json.dumps(data), encoding="utf-8")
    return data


def defensive_techniques(ontology: dict) -> dict[str, dict]:
    """D3-id → {label, definition}."""
    out: dict[str, dict] = {}
    for node in ontology.get("@graph", []):
        d3id = node.get("d3f:d3fend-id")
        if not isinstance(d3id, str) or not d3id.startswith("D3-"):
            continue
        label = node.get("rdfs:label") or node.get("skos:prefLabel") or d3id
        if isinstance(label, dict):
            label = label.get("@value", d3id)
        definition = node.get("d3f:definition") or ""
        if isinstance(definition, dict):
            definition = definition.get("@value", "")
        out[d3id] = {"label": _clean(str(label)), "definition": _clean(str(definition))}
    return out


def corpus_techniques(corpus_root: Path) -> list[str]:
    """ATT&CK ids this corpus holds — the only ones worth asking about."""
    ids = set()
    attack_dir = corpus_root / "imports" / "mitre-attack"
    for path in attack_dir.rglob("T*.md"):
        m = re.fullmatch(r"T\d{4}(\.\d{3})?", path.stem)
        if m:
            ids.add(path.stem)
    return sorted(ids)


def countermeasures_for(tid: str, cache_dir: Path, offline: bool) -> dict[str, str]:
    """D3-id → label for one ATT&CK technique. Cached on disk."""
    cache = cache_dir / f"{tid}.json"
    if cache.is_file():
        data = json.loads(cache.read_text(encoding="utf-8"))
    elif offline:
        return {}
    else:
        try:
            data = fetch_json(API_TEMPLATE.format(tid=tid), timeout=60)
        except Exception:  # noqa: BLE001 — a technique with no entry 404s
            data = {}
        cache.parent.mkdir(parents=True, exist_ok=True)
        cache.write_text(json.dumps(data), encoding="utf-8")
        time.sleep(POLITE_DELAY_S)

    out: dict[str, str] = {}
    bindings = (
        data.get("off_to_def", {}).get("results", {}).get("bindings", [])
        if isinstance(data, dict) else []
    )
    for row in bindings:
        d3id = (row.get("def_tech_id") or {}).get("value")
        label = (row.get("def_tech_label") or {}).get("value")
        if d3id and d3id.startswith("D3-"):
            out[d3id] = label or d3id
    return out


def page_for(d3id: str, info: dict, counters: list[str], known: set[str]) -> tuple[str, int]:
    """Render one defensive technique. Returns (markdown, resolved link count)."""
    label = info.get("label") or d3id
    definition = info.get("definition") or ""

    linked = [t for t in counters if f"technique/{t}" in known]
    related = [f"technique/{t}" for t in linked]

    summary = definition[:260] + "…" if len(definition) > 260 else definition
    summary = summary.replace('"', "'")

    lines = [
        "---",
        f"slug: defense/{d3id}",
        f'title: "{d3id} — {label}"',
        "page_type: defense",
        "tags: [d3fend, defense, countermeasure, mitre]",
        f"d3fend_ids: [{d3id}]",
    ]
    if linked:
        lines.append(f"mitre_ids: [{', '.join(linked)}]")
    lines += [
        f"related: [{', '.join(related)}]" if related else "related: []",
        "provenance: imported",
        "import_source: mitre-d3fend",
        f"import_id: {d3id}",
        f"updated_at: {date.today().isoformat()}",
        f'summary: "{summary}"',
        "sources:",
        "  - name: MITRE D3FEND",
        f"    url: https://d3fend.mitre.org/technique/{d3id}/",
        "---",
        "",
        f"# {d3id}: {label}",
        "",
        "**MITRE D3FEND countermeasure**",
        "",
    ]
    if definition:
        lines += ["## What it does", "", definition, ""]

    if linked:
        lines += [
            "## Attacks this counters",
            "",
            "The chain in this corpus runs CVE → CWE → CAPEC → ATT&CK technique, "
            "which ends at what an adversary does. This is the hop after: what "
            "stops it.",
            "",
        ]
        lines += [f"- [{t}](/wiki/p/technique/{t})" for t in linked]
        lines.append("")
    else:
        # An isolated countermeasure page is still worth having, but it must not
        # imply a mapping exists when none reached this corpus.
        lines += [
            "## Attacks this counters",
            "",
            "No ATT&CK technique in this corpus maps to this countermeasure. "
            "D3FEND may map it to techniques outside the Enterprise matrix, or "
            "to ones MITRE has since revoked — absence here is about this "
            "corpus, not about the countermeasure.",
            "",
        ]

    lines += [
        "## Source",
        "",
        f"- [MITRE D3FEND {d3id}](https://d3fend.mitre.org/technique/{d3id}/)",
        "",
    ]
    return "\n".join(lines), len(linked)


def existing_slugs(root: Path) -> set[str]:
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


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--corpus", type=Path, default=None)
    ap.add_argument("--cache", type=Path, default=Path(".d3fend-cache"))
    ap.add_argument("--offline", action="store_true",
                    help="Use only cached responses; never fetch")
    ap.add_argument("--limit", type=int, default=0, help="Max techniques to query (0=all)")
    args = ap.parse_args(argv)

    corpus_root = args.corpus or args.out.parent.parent
    known = existing_slugs(corpus_root)

    ontology = load_ontology(args.cache / "d3fend.json", args.offline)
    defs = defensive_techniques(ontology)
    print(f"ontology: {len(defs)} defensive techniques")

    techniques = corpus_techniques(corpus_root)
    if args.limit:
        techniques = techniques[: args.limit]
    print(f"querying countermeasures for {len(techniques)} ATT&CK techniques in the corpus")

    # D3-id → the techniques it counters
    inverted: dict[str, list[str]] = {}
    queried = missing = 0
    for i, tid in enumerate(techniques, 1):
        found = countermeasures_for(tid, args.cache / "attack", args.offline)
        if not found:
            missing += 1
        for d3id in found:
            inverted.setdefault(d3id, []).append(tid)
        queried += 1
        if i % 100 == 0:
            print(f"  {i}/{len(techniques)}…")

    args.out.mkdir(parents=True, exist_ok=True)
    written = mapped = links = 0
    for d3id, info in sorted(defs.items()):
        counters = sorted(set(inverted.get(d3id, [])))
        markdown, resolved = page_for(d3id, info, counters, known)
        (args.out / f"{d3id}.md").write_text(markdown, encoding="utf-8")
        written += 1
        if resolved:
            mapped += 1
            links += resolved

    manifest = {
        "source": "mitre-d3fend",
        "ontology_url": ONTOLOGY_URL,
        "pages": written,
        "pages_with_attack_mapping": mapped,
        # Never a silent gap: an unmapped countermeasure page is honest only if
        # the count of them is visible.
        "pages_without_attack_mapping": written - mapped,
        "attack_links": links,
        "techniques_queried": queried,
        "techniques_with_no_countermeasure": missing,
        "imported_at": date.today().isoformat(),
    }
    (args.out / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    print(f"wrote {written} pages")
    print(f"  {mapped} map to ATT&CK techniques in this corpus ({links} links)")
    print(f"  {written - mapped} have no mapping that reaches this corpus")
    print(f"  {missing}/{queried} queried techniques had no countermeasure at all")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
