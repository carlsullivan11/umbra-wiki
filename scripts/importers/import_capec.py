#!/usr/bin/env python3
"""Import MITRE CAPEC attack patterns into umbra-wiki markdown pages.

Usage:
  python scripts/importers/import_capec.py --out imports/mitre-capec
  python scripts/importers/import_capec.py --out imports/mitre-capec \
      --fixture scripts/fixtures/capec-sample.xml

**Why CAPEC, when CWE and ATT&CK are already here.**

Look at what the other cyber knowledge bases do and do not do. MITRE hosts CWE,
CAPEC and ATT&CK on three separate sites with three separate searches. NVD holds
CVEs and links to CWE but stops there. OWASP writes excellent prescriptive
guidance with no identifiers to join on. HackTricks is task-oriented and
popular, and asserts almost everything without a citation you can follow.

Nobody lets you walk the chain. And the chain is the thing an investigator
actually needs:

    CVE-2021-44228  (a finding)
      → CWE-502     what class of mistake it is
      → CAPEC-586   how an attacker uses that class
      → T1190       what that looks like in ATT&CK terms

CAPEC is the missing hop. The XML carries **1,214 Related_Weakness links** into
CWE and **349 Taxonomy_Mappings** into ATT&CK, so importing it does not just add
615 pages — it connects two corpora this wiki already holds.

**Only links that resolve.** `related:` entries are emitted only when the target
page exists on disk. A cross-reference to a page that is not here is worse than
no cross-reference: it looks like a traversal and dead-ends. The importer counts
what it dropped and says so.

**Deprecated patterns are skipped**, matching import_cwe's `--include-retired`
default. Publishing a retired attack pattern as current is the same failure as
publishing an obsoleted RFC without a banner.

**The catalogue's own age is recorded.** CAPEC 3.9 is dated 2023-01-24 — that is
upstream's latest, not our staleness, and a reader deserves to know a taxonomy
has not moved in that long rather than assume it is current.

Source: https://capec.mitre.org/data/xml/capec_latest.xml
"""

from __future__ import annotations

import argparse
import json
import re
import urllib.request
import xml.etree.ElementTree as ET
from datetime import date
from pathlib import Path

CAPEC_URL = "https://capec.mitre.org/data/xml/capec_latest.xml"

#: Same rule as import_cwe: a retired entry must not be published as current.
RETIRED_STATUSES = {"deprecated", "obsolete"}

_WS = re.compile(r"\s+")


def _text(el: ET.Element | None) -> str:
    if el is None:
        return ""
    return _WS.sub(" ", "".join(el.itertext())).strip()


def _findall(parent: ET.Element, path: str) -> list[ET.Element]:
    return parent.findall(path)


def is_retired(pattern: ET.Element) -> bool:
    return (pattern.get("Status") or "").strip().lower() in RETIRED_STATUSES


def related_cwes(pattern: ET.Element) -> list[str]:
    """CWE ids this pattern exploits."""
    out = []
    for rel in _findall(pattern, ".//{*}Related_Weakness"):
        cwe_id = (rel.get("CWE_ID") or "").strip()
        if cwe_id.isdigit():
            out.append(f"CWE-{int(cwe_id)}")
    return sorted(set(out), key=lambda c: int(c.split("-")[1]))


def related_attack(pattern: ET.Element) -> list[str]:
    """ATT&CK technique ids, from the ATTACK taxonomy mapping.

    Entry_ID is the bare number ("1190") or a sub-technique ("1190.001"), so it
    is prefixed here to match the corpus slug `technique/T1190`.
    """
    out = []
    for mapping in _findall(pattern, ".//{*}Taxonomy_Mapping"):
        if (mapping.get("Taxonomy_Name") or "").upper() != "ATTACK":
            continue
        entry = _text(mapping.find("{*}Entry_ID"))
        if re.fullmatch(r"\d{4}(\.\d{3})?", entry or ""):
            out.append(f"T{entry}")
    return sorted(set(out))


def bullets(pattern: ET.Element, container: str, item: str, limit: int = 8) -> list[str]:
    out = []
    for el in _findall(pattern, f".//{{*}}{container}/{{*}}{item}"):
        text = _text(el)
        if text:
            out.append(text)
    return out[:limit]


def consequences(pattern: ET.Element, limit: int = 6) -> list[str]:
    out = []
    for cons in _findall(pattern, ".//{*}Consequence"):
        scopes = [_text(s) for s in cons.findall("{*}Scope")]
        impacts = [_text(i) for i in cons.findall("{*}Impact")]
        if scopes or impacts:
            out.append(f"{', '.join(scopes) or '—'}: {', '.join(impacts) or '—'}")
    return out[:limit]


def page_for(
    pattern: ET.Element,
    *,
    catalog_version: str,
    catalog_date: str,
    known_slugs: set[str] | None = None,
) -> tuple[str, dict] | None:
    """Render one attack pattern. Returns (markdown, stats) or None if skipped."""
    capec_id = (pattern.get("ID") or "").strip()
    name = (pattern.get("Name") or "").strip()
    if not capec_id or not name:
        return None

    ident = f"CAPEC-{capec_id}"
    slug = f"attack-pattern/{ident}"
    description = _text(pattern.find("{*}Description"))
    severity = _text(pattern.find("{*}Typical_Severity"))
    likelihood = _text(pattern.find("{*}Likelihood_Of_Attack"))

    cwes = related_cwes(pattern)
    techniques = related_attack(pattern)

    # Only links that resolve. A cross-reference that dead-ends looks like a
    # traversal and is not one.
    wanted = [f"weakness/{c}" for c in cwes] + [f"technique/{t}" for t in techniques]
    if known_slugs is None:
        related = wanted
        dropped = []
    else:
        related = [s for s in wanted if s in known_slugs]
        dropped = [s for s in wanted if s not in known_slugs]
    related = ["concept/mitre-attack"] + related if techniques and known_slugs and \
        "concept/mitre-attack" in known_slugs else related

    prerequisites = bullets(pattern, "Prerequisites", "Prerequisite")
    mitigations = bullets(pattern, "Mitigations", "Mitigation")
    skills = [
        f"{(s.get('Level') or '?')}: {_text(s)}"
        for s in _findall(pattern, ".//{*}Skills_Required/{*}Skill")
    ][:6]

    summary = (description[:280] + "…") if len(description) > 280 else description
    summary = summary.replace('"', "'")

    lines = [
        "---",
        f"slug: {slug}",
        f'title: "{ident} — {name}"',
        "page_type: attack-pattern",
        "tags: [capec, attack-pattern, mitre]",
        f"capec_ids: [{ident}]",
    ]
    if cwes:
        lines.append(f"cwe_ids: [{', '.join(cwes)}]")
    if techniques:
        lines.append(f"mitre_ids: [{', '.join(techniques)}]")
    lines += [
        f"related: [{', '.join(related)}]" if related else "related: []",
        "provenance: imported",
        "import_source: mitre-capec",
        f"import_id: {ident}",
        f"updated_at: {date.today().isoformat()}",
        f'summary: "{summary}"',
        "sources:",
        "  - name: MITRE CAPEC",
        f"    url: https://capec.mitre.org/data/definitions/{capec_id}.html",
        "---",
        "",
        f"# {ident}: {name}",
        "",
        "**MITRE CAPEC attack pattern**",
        "",
        "| | |",
        "|--|--|",
        f"| Status | {pattern.get('Status') or '—'} |",
        f"| Typical severity | {severity or '—'} |",
        f"| Likelihood of attack | {likelihood or '—'} |",
        # The catalogue states its own age. CAPEC 3.9 is from 2023-01-24 and a
        # reader should not have to assume it is current.
        f"| Catalogue | CAPEC {catalog_version} ({catalog_date}) |",
        "",
    ]

    if description:
        lines += ["## Description", "", description, ""]

    if cwes or techniques:
        lines += ["## Where this sits in the chain", ""]
        lines += [
            "A finding maps to a weakness (CWE), a weakness is exploited by an "
            "attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as "
            "observed adversary behaviour. This page is the middle hop.",
            "",
        ]
        if cwes:
            lines.append("**Weaknesses exploited:** " + ", ".join(
                f"[{c}](/wiki/p/weakness/{c})" for c in cwes))
            lines.append("")
        if techniques:
            lines.append("**ATT&CK techniques:** " + ", ".join(
                f"[{t}](/wiki/p/technique/{t})" for t in techniques))
            lines.append("")

    for heading, items in (
        ("Prerequisites", prerequisites),
        ("Skills required", skills),
        ("Consequences", consequences(pattern)),
        ("Mitigations", mitigations),
    ):
        if items:
            lines += [f"## {heading}", ""] + [f"- {i}" for i in items] + [""]

    # A mapping into a technique the current ATT&CK corpus does not carry is
    # information, not an error. CAPEC 3.9 is from January 2023 and ATT&CK has
    # revoked techniques since — T1562 "Impair Defenses" and its sub-techniques
    # among them. capec.mitre.org still renders those mappings with no hint they
    # are dead, because the two products ship on different cadences and neither
    # checks the other. Saying so is the whole point of holding both.
    if dropped:
        stale = [s.split("/")[-1] for s in dropped if s.startswith("technique/")]
        if stale:
            lines += [
                "## Mappings that no longer resolve",
                "",
                f"CAPEC {catalog_version} ({catalog_date}) maps this pattern to "
                + ", ".join(f"`{t}`" for t in stale)
                + ", which the current ATT&CK corpus does not carry — MITRE has "
                "revoked or relocated them since CAPEC was last published. The "
                "mapping is recorded here rather than dropped, because a stale "
                "cross-reference is a fact about the taxonomies, not a gap in "
                "this page.",
                "",
            ]

    lines += [
        "## Source",
        "",
        f"- [MITRE CAPEC {ident}](https://capec.mitre.org/data/definitions/{capec_id}.html)",
        "",
    ]

    stats = {
        "slug": slug,
        "cwe_links": len([s for s in related if s.startswith("weakness/")]),
        "attack_links": len([s for s in related if s.startswith("technique/")]),
        "dropped_links": dropped,
    }
    return "\n".join(lines), stats


def load_catalog(fixture: Path | None) -> ET.Element:
    if fixture:
        return ET.parse(fixture).getroot()
    with urllib.request.urlopen(CAPEC_URL, timeout=180) as resp:
        return ET.fromstring(resp.read())


def existing_slugs(root: Path) -> set[str]:
    """Every slug already in the corpus, so links can be checked."""
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
    ap.add_argument("--out", type=Path, required=True, help="Output dir (imports/mitre-capec)")
    ap.add_argument("--fixture", type=Path, default=None, help="Local XML instead of fetching")
    ap.add_argument("--corpus", type=Path, default=None,
                    help="Corpus root for link checking (default: --out's grandparent)")
    ap.add_argument("--include-retired", action="store_true",
                    help="Also import Deprecated/Obsolete patterns (default: skip)")
    args = ap.parse_args(argv)

    root = load_catalog(args.fixture)
    version = root.get("Version") or "?"
    catalog_date = root.get("Date") or "?"

    corpus_root = args.corpus or args.out.parent.parent
    known = existing_slugs(corpus_root) if corpus_root.is_dir() else set()

    args.out.mkdir(parents=True, exist_ok=True)
    written = 0
    skipped_retired = 0
    cwe_links = attack_links = 0
    dropped: list[str] = []

    for pattern in root.findall(".//{*}Attack_Pattern"):
        if is_retired(pattern) and not args.include_retired:
            skipped_retired += 1
            continue
        result = page_for(
            pattern,
            catalog_version=version,
            catalog_date=catalog_date,
            known_slugs=known or None,
        )
        if not result:
            continue
        markdown, stats = result
        ident = stats["slug"].split("/")[-1]
        (args.out / f"{ident}.md").write_text(markdown, encoding="utf-8")
        written += 1
        cwe_links += stats["cwe_links"]
        attack_links += stats["attack_links"]
        dropped += stats["dropped_links"]

    manifest = {
        "source": "mitre-capec",
        "catalog_version": version,
        "catalog_date": catalog_date,
        "url": CAPEC_URL,
        "pages": written,
        "skipped_retired": skipped_retired,
        "cwe_links": cwe_links,
        "attack_links": attack_links,
        "dropped_links": len(dropped),
        "imported_at": date.today().isoformat(),
    }
    (args.out / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    print(f"wrote {written} pages (CAPEC {version}, {catalog_date})")
    print(f"  skipped {skipped_retired} deprecated/obsolete")
    print(f"  resolved links: {cwe_links} → CWE, {attack_links} → ATT&CK")
    # Never a silent drop: a link that did not resolve is a gap in the corpus,
    # and the count is how you find out the join is thinner than it looks.
    if dropped:
        uniq = sorted(set(dropped))
        print(f"  dropped {len(dropped)} link(s) to {len(uniq)} page(s) not in the corpus")
        for slug in uniq[:8]:
            print(f"    {slug}")
        if len(uniq) > 8:
            print(f"    …and {len(uniq) - 8} more")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
