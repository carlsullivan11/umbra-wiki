---
slug: weakness/CWE-58
title: "CWE-58 — Path Equivalence: Windows 8.3 Filename"
page_type: weakness
tags: [cwe, weakness, mitre]
cwe_ids: [CWE-58]
related: [concept/cve-anatomy]
provenance: imported
import_source: mitre-cwe
import_id: CWE-58
updated_at: 2026-08-14
summary: "The product contains a protection mechanism that restricts access to a long filename on a Windows operating system, but it does not properly restrict access to the equivalent short '8.3' filename."
sources:
  - name: MITRE CWE
    url: https://cwe.mitre.org/data/definitions/58.html
---

# CWE-58: Path Equivalence: Windows 8.3 Filename

**MITRE CWE weakness**

| | |
|--|--|
| Kind | Weakness |
| Abstraction | Variant |
| Status | Incomplete |
| Likelihood of exploit | — |

## Description

The product contains a protection mechanism that restricts access to a long filename on a Windows operating system, but it does not properly restrict access to the equivalent short "8.3" filename.



## Common consequences

- Confidentiality, Integrity: Read Files or Directories, Modify Files or Directories

## Mitigations

**System Configuration** — Disable Windows from supporting 8.3 filenames by editing the Windows registry. Preventing 8.3 filenames will not remove previously generated 8.3 filenames.

## References

- CWE page: https://cwe.mitre.org/data/definitions/58.html
- CWE list: https://cwe.mitre.org/data/index.html
