---
slug: weakness/CWE-97
title: "CWE-97 — Improper Neutralization of Server-Side Includes (SSI) Within a Web Page"
page_type: weakness
tags: [cwe, weakness, mitre]
cwe_ids: [CWE-97]
related: [concept/cve-anatomy]
provenance: imported
import_source: mitre-cwe
import_id: CWE-97
updated_at: 2026-08-14
summary: "The product generates a web page, but does not neutralize or incorrectly neutralizes user-controllable input that could be interpreted as a server-side include (SSI) directive."
sources:
  - name: MITRE CWE
    url: https://cwe.mitre.org/data/definitions/97.html
---

# CWE-97: Improper Neutralization of Server-Side Includes (SSI) Within a Web Page

**MITRE CWE weakness**

| | |
|--|--|
| Kind | Weakness |
| Abstraction | Variant |
| Status | Draft |
| Likelihood of exploit | — |

## Description

The product generates a web page, but does not neutralize or incorrectly neutralizes user-controllable input that could be interpreted as a server-side include (SSI) directive.



## Common consequences

- Confidentiality, Integrity, Availability: Execute Unauthorized Code or Commands

## Mitigations

(none listed)

## References

- CWE page: https://cwe.mitre.org/data/definitions/97.html
- CWE list: https://cwe.mitre.org/data/index.html
