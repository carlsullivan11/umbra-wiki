---
slug: weakness/CWE-93
title: "CWE-93 — Improper Neutralization of CRLF Sequences ('CRLF Injection')"
page_type: weakness
tags: [cwe, weakness, mitre]
cwe_ids: [CWE-93]
related: [concept/cve-anatomy]
provenance: imported
import_source: mitre-cwe
import_id: CWE-93
updated_at: 2026-08-14
summary: "The product uses CRLF (carriage return line feeds) as a special element, e.g. to separate lines or records, but it does not neutralize or incorrectly neutralizes CRLF sequences from inputs."
sources:
  - name: MITRE CWE
    url: https://cwe.mitre.org/data/definitions/93.html
---

# CWE-93: Improper Neutralization of CRLF Sequences ('CRLF Injection')

**MITRE CWE weakness**

| | |
|--|--|
| Kind | Weakness |
| Abstraction | Base |
| Status | Draft |
| Likelihood of exploit | — |

## Description

The product uses CRLF (carriage return line feeds) as a special element, e.g. to separate lines or records, but it does not neutralize or incorrectly neutralizes CRLF sequences from inputs.



## Common consequences

- Integrity: Modify Application Data

## Mitigations

**Implementation** — Avoid using CRLF as a special sequence.

**Implementation** — Appropriately filter or quote CRLF sequences in user-controlled input.

## References

- CWE page: https://cwe.mitre.org/data/definitions/93.html
- CWE list: https://cwe.mitre.org/data/index.html
