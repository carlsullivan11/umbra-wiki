---
slug: weakness/CWE-45
title: "CWE-45 — Path Equivalence: 'file...name' (Multiple Internal Dot)"
page_type: weakness
tags: [cwe, weakness, mitre]
cwe_ids: [CWE-45]
related: [concept/cve-anatomy]
provenance: imported
import_source: mitre-cwe
import_id: CWE-45
updated_at: 2026-08-14
summary: "The product accepts path input in the form of multiple internal dot ('file...dir') without appropriate validation, which can lead to ambiguous path resolution and allow an attacker to traverse the fil"
sources:
  - name: MITRE CWE
    url: https://cwe.mitre.org/data/definitions/45.html
---

# CWE-45: Path Equivalence: 'file...name' (Multiple Internal Dot)

**MITRE CWE weakness**

| | |
|--|--|
| Kind | Weakness |
| Abstraction | Variant |
| Status | Incomplete |
| Likelihood of exploit | — |

## Description

The product accepts path input in the form of multiple internal dot ('file...dir') without appropriate validation, which can lead to ambiguous path resolution and allow an attacker to traverse the file system to unintended locations or access arbitrary files.



## Common consequences

- Confidentiality, Integrity: Read Files or Directories, Modify Files or Directories

## Mitigations

(none listed)

## References

- CWE page: https://cwe.mitre.org/data/definitions/45.html
- CWE list: https://cwe.mitre.org/data/index.html
