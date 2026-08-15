---
slug: weakness/CWE-76
title: "CWE-76 — Improper Neutralization of Equivalent Special Elements"
page_type: weakness
tags: [cwe, weakness, mitre]
cwe_ids: [CWE-76]
related: [concept/cve-anatomy]
provenance: imported
import_source: mitre-cwe
import_id: CWE-76
updated_at: 2026-08-14
summary: "The product correctly neutralizes certain special elements, but it improperly neutralizes equivalent special elements."
sources:
  - name: MITRE CWE
    url: https://cwe.mitre.org/data/definitions/76.html
---

# CWE-76: Improper Neutralization of Equivalent Special Elements

**MITRE CWE weakness**

| | |
|--|--|
| Kind | Weakness |
| Abstraction | Base |
| Status | Draft |
| Likelihood of exploit | High |

## Description

The product correctly neutralizes certain special elements, but it improperly neutralizes equivalent special elements.

The product may have a fixed list of special characters it believes is complete. However, there may be alternate encodings, or representations that also have the same meaning. For example, the product may filter out a leading slash (/) to prevent absolute path names, but does not account for a tilde (~) followed by a user name, which on some *nix systems could be expanded to an absolute pathname. Alternately, the product might filter a dangerous "-e" command-line switch when calling an external program, but it might not account for "--exec" or other switches that have the same semantics.

## Common consequences

- Other: Other

## Mitigations

**Requirements** — Programming languages and supporting technologies might be chosen which are not subject to these issues.

**Implementation** — Utilize an appropriate mix of allowlist and denylist parsing to filter equivalent special element syntax from all input.

## References

- CWE page: https://cwe.mitre.org/data/definitions/76.html
- CWE list: https://cwe.mitre.org/data/index.html
