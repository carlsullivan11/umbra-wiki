---
slug: weakness/CWE-75
title: "CWE-75 — Failure to Sanitize Special Elements into a Different Plane (Special Element Injection)"
page_type: weakness
tags: [cwe, weakness, mitre]
cwe_ids: [CWE-75]
related: [concept/cve-anatomy]
provenance: imported
import_source: mitre-cwe
import_id: CWE-75
updated_at: 2026-08-14
summary: "The product does not adequately filter user-controlled input for special elements with control implications."
sources:
  - name: MITRE CWE
    url: https://cwe.mitre.org/data/definitions/75.html
---

# CWE-75: Failure to Sanitize Special Elements into a Different Plane (Special Element Injection)

**MITRE CWE weakness**

| | |
|--|--|
| Kind | Weakness |
| Abstraction | Class |
| Status | Draft |
| Likelihood of exploit | — |

## Description

The product does not adequately filter user-controlled input for special elements with control implications.



## Common consequences

- Integrity, Confidentiality, Availability: Modify Application Data, Execute Unauthorized Code or Commands

## Mitigations

**Requirements** — Programming languages and supporting technologies might be chosen which are not subject to these issues.

**Implementation** — Utilize an appropriate mix of allowlist and denylist parsing to filter special element syntax from all input.

## References

- CWE page: https://cwe.mitre.org/data/definitions/75.html
- CWE list: https://cwe.mitre.org/data/index.html
