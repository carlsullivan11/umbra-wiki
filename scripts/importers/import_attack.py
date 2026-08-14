#!/usr/bin/env python3
"""Import MITRE ATT&CK Enterprise techniques into umbra-wiki markdown pages.

Usage:
  python scripts/importers/import_attack.py --out imports/mitre-attack
  python scripts/importers/import_attack.py --out imports/mitre-attack \
      --fixture scripts/fixtures/attack-sample.json

Design notes (docs/CLAUDE-NEXT-STAGES.md#S4):

- **Only the generated pages are committed, never the source bundle.** The
  enterprise STIX file is ~54 MB; it is downloaded to a temp path, parsed, and
  discarded. Committing it would bloat the repo for no reader benefit.
- **Revoked and deprecated techniques are skipped.** ~161 of 858 attack-patterns
  are retired; importing them would put stale advice in front of an operator
  who searched for a technique ID.
- **Sub-techniques keep their own page** (`technique/T1557.002`) and link back
  to the parent, because that is how people search — `lookup T1557.002` must
  land on ARP Cache Poisoning, not on the parent.
- Slug namespace `technique/<ID>` does not collide with `cve/<ID>` from the
  KEV/NVD importers.

Attribution: ATT&CK® is a registered trademark of The MITRE Corporation. The
knowledge base is redistributed here under MITRE's Terms of Use, which permit
reuse with attribution and without implying endorsement.
Source: https://github.com/mitre-attack/attack-stix-data
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.request
from datetime import date
from pathlib import Path

ATTACK_URL = (
    "https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/"
    "enterprise-attack/enterprise-attack.json"
)
TECHNIQUE_RE = re.compile(r"^T\d{4}(\.\d{3})?$")


def attack_id(obj: dict) -> str | None:
    for ref in obj.get("external_references") or []:
        if ref.get("source_name") == "mitre-attack":
            return ref.get("external_id")
    return None


def attack_url(obj: dict) -> str:
    for ref in obj.get("external_references") or []:
        if ref.get("source_name") == "mitre-attack" and ref.get("url"):
            return ref["url"]
    return "https://attack.mitre.org/"


def is_retired(obj: dict) -> bool:
    """Revoked or deprecated techniques must not be published as guidance."""
    return bool(obj.get("revoked") or obj.get("x_mitre_deprecated"))


def tactics_of(obj: dict) -> list[str]:
    out: list[str] = []
    for phase in obj.get("kill_chain_phases") or []:
        if phase.get("kill_chain_name") == "mitre-attack":
            name = (phase.get("phase_name") or "").replace("-", " ").title()
            if name and name not in out:
                out.append(name)
    return out


def _yaml_list(values: list[str]) -> str:
    return ", ".join(v.replace('"', "'") for v in values)


def page_for(obj: dict) -> str | None:
    tid = attack_id(obj)
    if not tid or not TECHNIQUE_RE.match(tid):
        return None

    name = (obj.get("name") or tid).strip()
    desc = (obj.get("description") or "").strip()
    tactics = tactics_of(obj)
    platforms = obj.get("x_mitre_platforms") or []
    detection = (obj.get("x_mitre_detection") or "").strip()
    data_sources = obj.get("x_mitre_data_sources") or []
    perms = obj.get("x_mitre_permissions_required") or []
    version = obj.get("x_mitre_version") or ""
    today = date.today().isoformat()

    parent = tid.split(".")[0] if "." in tid else None
    related = ["concept/mitre-attack"]
    if parent:
        related.append(f"technique/{parent}")

    title = f"{tid} — {name}".replace('"', "'")
    summary = (desc.split("\n")[0][:200]).replace('"', "'") if desc else name

    body = f"""# {tid}: {name}

**MITRE ATT&CK® Enterprise technique**

| | |
|--|--|
| Tactics | {", ".join(tactics) or "—"} |
| Platforms | {", ".join(platforms) or "—"} |
| Permissions required | {", ".join(perms) or "—"} |
| Version | {version or "—"} |
{f"| Parent technique | [{parent}](technique/{parent}) |" if parent else ""}

## Description

{desc or "(no description published)"}

## Detection

{detection or "(no detection guidance published)"}

## Data sources

{chr(10).join(f"- {d}" for d in data_sources) if data_sources else "- (none listed)"}

## References

- ATT&CK page: {attack_url(obj)}
- ATT&CK Enterprise matrix: https://attack.mitre.org/matrices/enterprise/
"""

    fm = f"""---
slug: technique/{tid}
title: "{title}"
page_type: technique
tags: [attack, technique, mitre{"".join(f", {t.lower().replace(' ', '-')}" for t in tactics)}]
mitre_ids: [{tid}]
related: [{_yaml_list(related)}]
provenance: imported
import_source: mitre-attack
import_id: {tid}
updated_at: {today}
summary: "{summary}"
sources:
  - name: MITRE ATT&CK
    url: {attack_url(obj)}
---

"""
    return fm + body


def load_bundle(fixture: Path | None) -> dict:
    if fixture:
        return json.loads(fixture.read_text(encoding="utf-8"))
    req = urllib.request.Request(
        ATTACK_URL, headers={"User-Agent": "umbra-wiki-importer/0.1"}
    )
    with urllib.request.urlopen(req, timeout=300) as resp:  # noqa: S310
        return json.loads(resp.read().decode("utf-8"))


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", type=Path, required=True, help="Output dir (imports/mitre-attack)")
    ap.add_argument("--fixture", type=Path, default=None, help="Local STIX bundle (skip network)")
    ap.add_argument("--limit", type=int, default=0, help="Max pages (0 = all techniques)")
    ap.add_argument(
        "--include-retired",
        action="store_true",
        help="Also import revoked/deprecated techniques (default: skip)",
    )
    args = ap.parse_args(argv)

    bundle = load_bundle(args.fixture)
    objects = bundle.get("objects") or []
    techniques = [o for o in objects if o.get("type") == "attack-pattern"]

    args.out.mkdir(parents=True, exist_ok=True)
    written = skipped_retired = 0
    for obj in techniques:
        if is_retired(obj) and not args.include_retired:
            skipped_retired += 1
            continue
        page = page_for(obj)
        if not page:
            continue
        tid = attack_id(obj)
        # Sub-techniques live beside their parent for readability on disk.
        sub = args.out / tid.split(".")[0]
        sub.mkdir(parents=True, exist_ok=True)
        (sub / f"{tid}.md").write_text(page, encoding="utf-8")
        written += 1
        if args.limit and written >= args.limit:
            break

    manifest = {
        "source": "mitre-attack",
        "url": ATTACK_URL if not args.fixture else str(args.fixture),
        "count": written,
        "skipped_retired": skipped_retired,
        "attack_domain": "enterprise",
        "fetched_at": date.today().isoformat(),
    }
    (args.out / "manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
    )

    corpus_root = args.out.parent.parent if args.out.parent.name == "imports" else Path(".")
    attr = corpus_root / "meta" / "attribution" / "mitre-attack.md"
    if attr.parent.is_dir():
        attr.write_text(
            f"""# MITRE ATT&CK attribution

- Source: MITRE ATT&CK® Enterprise (STIX 2.1)
- URL: {ATTACK_URL}
- Imported pages: `{written}` techniques (see imports/mitre-attack/manifest.json)
- Skipped: `{skipped_retired}` revoked/deprecated techniques — retired guidance
  is deliberately not published.
- Only generated pages are committed; the ~54 MB source bundle is not.
- Terms: ATT&CK® and MITRE ATT&CK® are registered trademarks of The MITRE
  Corporation. Redistributed under MITRE's Terms of Use
  (https://attack.mitre.org/resources/legal-and-branding/terms-of-use/), which
  permit reuse with attribution. MITRE does not endorse this project.
- Last importer run date: {date.today().isoformat()}
""",
            encoding="utf-8",
        )

    print(f"wrote {written} ATT&CK pages → {args.out} (skipped {skipped_retired} retired)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
