---
slug: weakness/CWE-72
title: "CWE-72 — Improper Handling of Apple HFS+ Alternate Data Stream Path"
page_type: weakness
tags: [cwe, weakness, mitre]
cwe_ids: [CWE-72]
related: [concept/cve-anatomy]
provenance: imported
import_source: mitre-cwe
import_id: CWE-72
updated_at: 2026-08-14
summary: "The product does not properly handle special paths that may identify the data or resource fork of a file on the HFS+ file system."
sources:
  - name: MITRE CWE
    url: https://cwe.mitre.org/data/definitions/72.html
---

# CWE-72: Improper Handling of Apple HFS+ Alternate Data Stream Path

**MITRE CWE weakness**

| | |
|--|--|
| Kind | Weakness |
| Abstraction | Variant |
| Status | Incomplete |
| Likelihood of exploit | — |

## Description

The product does not properly handle special paths that may identify the data or resource fork of a file on the HFS+ file system.

If the product chooses actions to take based on the file name, then if an attacker provides the data or resource fork, the product may take unexpected actions. Further, if the product intends to restrict access to a file, then an attacker might still be able to bypass intended access restrictions by requesting the data or resource fork for that file.

## Common consequences

- Confidentiality, Integrity: Read Files or Directories, Modify Files or Directories

## Mitigations

(none listed)

## References

- CWE page: https://cwe.mitre.org/data/definitions/72.html
- CWE list: https://cwe.mitre.org/data/index.html
