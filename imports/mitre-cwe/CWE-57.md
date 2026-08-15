---
slug: weakness/CWE-57
title: "CWE-57 — Path Equivalence: 'fakedir/../realdir/filename'"
page_type: weakness
tags: [cwe, weakness, mitre]
cwe_ids: [CWE-57]
related: [concept/cve-anatomy]
provenance: imported
import_source: mitre-cwe
import_id: CWE-57
updated_at: 2026-08-14
summary: "The product contains protection mechanisms to restrict access to 'realdir/filename', but it constructs pathnames using external input in the form of 'fakedir/../realdir/filename' that are not handled "
sources:
  - name: MITRE CWE
    url: https://cwe.mitre.org/data/definitions/57.html
---

# CWE-57: Path Equivalence: 'fakedir/../realdir/filename'

**MITRE CWE weakness**

| | |
|--|--|
| Kind | Weakness |
| Abstraction | Variant |
| Status | Incomplete |
| Likelihood of exploit | — |

## Description

The product contains protection mechanisms to restrict access to 'realdir/filename', but it constructs pathnames using external input in the form of 'fakedir/../realdir/filename' that are not handled by those mechanisms. This allows attackers to perform unauthorized actions against the targeted file.



## Common consequences

- Confidentiality, Integrity: Read Files or Directories, Modify Files or Directories

## Mitigations

**Implementation** — Inputs should be decoded and canonicalized to the application's current internal representation before being validated (CWE-180). Make sure that the application does not decode the same input twice (CWE-174). Such errors could be used to bypass allowlist validation schemes by introducing dangerous inputs after they have been checked.

## References

- CWE page: https://cwe.mitre.org/data/definitions/57.html
- CWE list: https://cwe.mitre.org/data/index.html
