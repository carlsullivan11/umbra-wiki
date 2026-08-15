---
slug: weakness/CWE-64
title: "CWE-64 — Windows Shortcut Following (.LNK)"
page_type: weakness
tags: [cwe, weakness, mitre]
cwe_ids: [CWE-64]
related: [concept/cve-anatomy]
provenance: imported
import_source: mitre-cwe
import_id: CWE-64
updated_at: 2026-08-14
summary: "The product, when opening a file or directory, does not sufficiently handle when the file is a Windows shortcut (.LNK) whose target is outside of the intended control sphere. This could allow an attac"
sources:
  - name: MITRE CWE
    url: https://cwe.mitre.org/data/definitions/64.html
---

# CWE-64: Windows Shortcut Following (.LNK)

**MITRE CWE weakness**

| | |
|--|--|
| Kind | Weakness |
| Abstraction | Variant |
| Status | Incomplete |
| Likelihood of exploit | Low |

## Description

The product, when opening a file or directory, does not sufficiently handle when the file is a Windows shortcut (.LNK) whose target is outside of the intended control sphere. This could allow an attacker to cause the product to operate on unauthorized files.



## Common consequences

- Confidentiality, Integrity: Read Files or Directories, Modify Files or Directories

## Mitigations

**Architecture and Design** — Follow the principle of least privilege when assigning access rights to entities in a software system. Denying access to a file can prevent an attacker from replacing that file with a link to a sensitive file. Ensure good compartmentalization in the system to provide protected areas that can be trusted.

## References

- CWE page: https://cwe.mitre.org/data/definitions/64.html
- CWE list: https://cwe.mitre.org/data/index.html
