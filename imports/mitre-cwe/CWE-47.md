---
slug: weakness/CWE-47
title: "CWE-47 — Path Equivalence: ' filename' (Leading Space)"
page_type: weakness
tags: [cwe, weakness, mitre]
cwe_ids: [CWE-47]
related: [concept/cve-anatomy]
provenance: imported
import_source: mitre-cwe
import_id: CWE-47
updated_at: 2026-08-14
summary: "The product accepts path input in the form of leading space (' filedir') without appropriate validation, which can lead to ambiguous path resolution and allow an attacker to traverse the file system t"
sources:
  - name: MITRE CWE
    url: https://cwe.mitre.org/data/definitions/47.html
---

# CWE-47: Path Equivalence: ' filename' (Leading Space)

**MITRE CWE weakness**

| | |
|--|--|
| Kind | Weakness |
| Abstraction | Variant |
| Status | Incomplete |
| Likelihood of exploit | — |

## Description

The product accepts path input in the form of leading space (' filedir') without appropriate validation, which can lead to ambiguous path resolution and allow an attacker to traverse the file system to unintended locations or access arbitrary files.



## Common consequences

- Confidentiality, Integrity: Read Files or Directories, Modify Files or Directories

## Mitigations

(none listed)

## References

- CWE page: https://cwe.mitre.org/data/definitions/47.html
- CWE list: https://cwe.mitre.org/data/index.html
