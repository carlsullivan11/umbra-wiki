---
slug: weakness/CWE-46
title: "CWE-46 — Path Equivalence: 'filename ' (Trailing Space)"
page_type: weakness
tags: [cwe, weakness, mitre]
cwe_ids: [CWE-46]
related: [concept/cve-anatomy]
provenance: imported
import_source: mitre-cwe
import_id: CWE-46
updated_at: 2026-08-14
summary: "The product accepts path input in the form of trailing space ('filedir ') without appropriate validation, which can lead to ambiguous path resolution and allow an attacker to traverse the file system "
sources:
  - name: MITRE CWE
    url: https://cwe.mitre.org/data/definitions/46.html
---

# CWE-46: Path Equivalence: 'filename ' (Trailing Space)

**MITRE CWE weakness**

| | |
|--|--|
| Kind | Weakness |
| Abstraction | Variant |
| Status | Incomplete |
| Likelihood of exploit | — |

## Description

The product accepts path input in the form of trailing space ('filedir ') without appropriate validation, which can lead to ambiguous path resolution and allow an attacker to traverse the file system to unintended locations or access arbitrary files.



## Common consequences

- Confidentiality, Integrity: Read Files or Directories, Modify Files or Directories

## Mitigations

(none listed)

## References

- CWE page: https://cwe.mitre.org/data/definitions/46.html
- CWE list: https://cwe.mitre.org/data/index.html
