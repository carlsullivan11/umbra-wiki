---
slug: weakness/CWE-66
title: "CWE-66 — Improper Handling of File Names that Identify Virtual Resources"
page_type: weakness
tags: [cwe, weakness, mitre]
cwe_ids: [CWE-66]
related: [concept/cve-anatomy]
provenance: imported
import_source: mitre-cwe
import_id: CWE-66
updated_at: 2026-08-14
summary: "The product does not handle or incorrectly handles a file name that identifies a 'virtual' resource that is not directly specified within the directory that is associated with the file name, causing t"
sources:
  - name: MITRE CWE
    url: https://cwe.mitre.org/data/definitions/66.html
---

# CWE-66: Improper Handling of File Names that Identify Virtual Resources

**MITRE CWE weakness**

| | |
|--|--|
| Kind | Weakness |
| Abstraction | Base |
| Status | Draft |
| Likelihood of exploit | — |

## Description

The product does not handle or incorrectly handles a file name that identifies a "virtual" resource that is not directly specified within the directory that is associated with the file name, causing the product to perform file-based operations on a resource that is not a file.

Virtual file names are represented like normal file names, but they are effectively aliases for other resources that do not behave like normal files. Depending on their functionality, they could be alternate entities. They are not necessarily listed in directories.

## Common consequences

- Other: Other

## Mitigations

(none listed)

## References

- CWE page: https://cwe.mitre.org/data/definitions/66.html
- CWE list: https://cwe.mitre.org/data/index.html
