---
slug: weakness/CWE-42
title: "CWE-42 — Path Equivalence: 'filename.' (Trailing Dot)"
page_type: weakness
tags: [cwe, weakness, mitre]
cwe_ids: [CWE-42]
related: [concept/cve-anatomy]
provenance: imported
import_source: mitre-cwe
import_id: CWE-42
updated_at: 2026-08-14
summary: "The product accepts path input in the form of trailing dot ('filedir.') without appropriate validation, which can lead to ambiguous path resolution and allow an attacker to traverse the file system to"
sources:
  - name: MITRE CWE
    url: https://cwe.mitre.org/data/definitions/42.html
---

# CWE-42: Path Equivalence: 'filename.' (Trailing Dot)

**MITRE CWE weakness**

| | |
|--|--|
| Kind | Weakness |
| Abstraction | Variant |
| Status | Incomplete |
| Likelihood of exploit | — |

## Description

The product accepts path input in the form of trailing dot ('filedir.') without appropriate validation, which can lead to ambiguous path resolution and allow an attacker to traverse the file system to unintended locations or access arbitrary files.



## Common consequences

- Access Control: Bypass Protection Mechanism

## Mitigations

(none listed)

## References

- CWE page: https://cwe.mitre.org/data/definitions/42.html
- CWE list: https://cwe.mitre.org/data/index.html
