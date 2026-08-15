---
slug: weakness/CWE-53
title: "CWE-53 — Path Equivalence: '\multiple\\internal\backslash'"
page_type: weakness
tags: [cwe, weakness, mitre]
cwe_ids: [CWE-53]
related: [concept/cve-anatomy]
provenance: imported
import_source: mitre-cwe
import_id: CWE-53
updated_at: 2026-08-14
summary: "The product accepts path input in the form of multiple internal backslash ('\multiple\trailing\\slash') without appropriate validation, which can lead to ambiguous path resolution and allow an attacke"
sources:
  - name: MITRE CWE
    url: https://cwe.mitre.org/data/definitions/53.html
---

# CWE-53: Path Equivalence: '\multiple\\internal\backslash'

**MITRE CWE weakness**

| | |
|--|--|
| Kind | Weakness |
| Abstraction | Variant |
| Status | Incomplete |
| Likelihood of exploit | — |

## Description

The product accepts path input in the form of multiple internal backslash ('\multiple\trailing\\slash') without appropriate validation, which can lead to ambiguous path resolution and allow an attacker to traverse the file system to unintended locations or access arbitrary files.



## Common consequences

- Confidentiality, Integrity: Read Files or Directories, Modify Files or Directories

## Mitigations

**Implementation** — Inputs should be decoded and canonicalized to the application's current internal representation before being validated (CWE-180). Make sure that the application does not decode the same input twice (CWE-174). Such errors could be used to bypass allowlist validation schemes by introducing dangerous inputs after they have been checked.

## References

- CWE page: https://cwe.mitre.org/data/definitions/53.html
- CWE list: https://cwe.mitre.org/data/index.html
