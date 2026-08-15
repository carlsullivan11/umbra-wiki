---
slug: weakness/CWE-51
title: "CWE-51 — Path Equivalence: '/multiple//internal/slash'"
page_type: weakness
tags: [cwe, weakness, mitre]
cwe_ids: [CWE-51]
related: [concept/cve-anatomy]
provenance: imported
import_source: mitre-cwe
import_id: CWE-51
updated_at: 2026-08-14
summary: "The product accepts path input in the form of multiple internal slash ('/multiple//internal/slash/') without appropriate validation, which can lead to ambiguous path resolution and allow an attacker t"
sources:
  - name: MITRE CWE
    url: https://cwe.mitre.org/data/definitions/51.html
---

# CWE-51: Path Equivalence: '/multiple//internal/slash'

**MITRE CWE weakness**

| | |
|--|--|
| Kind | Weakness |
| Abstraction | Variant |
| Status | Incomplete |
| Likelihood of exploit | — |

## Description

The product accepts path input in the form of multiple internal slash ('/multiple//internal/slash/') without appropriate validation, which can lead to ambiguous path resolution and allow an attacker to traverse the file system to unintended locations or access arbitrary files.



## Common consequences

- Confidentiality, Integrity: Read Files or Directories, Modify Files or Directories

## Mitigations

**Implementation** — Inputs should be decoded and canonicalized to the application's current internal representation before being validated (CWE-180). Make sure that the application does not decode the same input twice (CWE-174). Such errors could be used to bypass allowlist validation schemes by introducing dangerous inputs after they have been checked.

## References

- CWE page: https://cwe.mitre.org/data/definitions/51.html
- CWE list: https://cwe.mitre.org/data/index.html
