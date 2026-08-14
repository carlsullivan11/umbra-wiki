# Schema — umbra-wiki pages

Each page is a Markdown file with YAML frontmatter.

## Required frontmatter

| Field | Type | Description |
|-------|------|-------------|
| `slug` | string | Stable id, e.g. `protocol/arp`, `cve/CVE-2024-3400` |
| `title` | string | Display title |
| `page_type` | enum | `concept` `protocol` `technique` `ta` `cve` `standard` `tool` `detection` `playbook` `framework` |
| `provenance` | enum | `curated` `imported` `generated_reviewed` |

## Optional

| Field | Type |
|-------|------|
| `tags` | string list |
| `mitre_ids` | e.g. `T1557.002` |
| `cve_ids` | e.g. `CVE-2024-3400` |
| `cwe_ids` | e.g. `CWE-79` |
| `standards` | e.g. `RFC826`, `IEEE-802.3`, `NIST-CSF-PR.DS` |
| `related` | list of slugs |
| `sources` | list of `{name, url}` |
| `import_source` | `nvd` `kev` `mitre` `cwe` `oui` `rfc` … |
| `import_id` | upstream id |
| `summary` | one-line blurb (else first body paragraph) |
| `updated_at` | ISO date |

## Example

```markdown
---
slug: protocol/arp
title: Address Resolution Protocol (ARP)
page_type: protocol
tags: [network, l2]
mitre_ids: [T1557.002]
related: [concept/arp-cache-poisoning]
provenance: curated
updated_at: 2026-08-14
---

ARP maps IPv4 addresses to link-layer (MAC) addresses on a local network…
```

## Paths

- Curated: `curated/<section>/<file>.md`
- Imports: `imports/<source>/...`
- Slug need not match path but should stay stable once published
