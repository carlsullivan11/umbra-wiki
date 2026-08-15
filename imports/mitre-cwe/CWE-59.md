---
slug: weakness/CWE-59
title: "CWE-59 — Improper Link Resolution Before File Access ('Link Following')"
page_type: weakness
tags: [cwe, weakness, mitre]
cwe_ids: [CWE-59]
related: [concept/cve-anatomy]
provenance: imported
import_source: mitre-cwe
import_id: CWE-59
updated_at: 2026-08-14
summary: "The product attempts to access a file based on the filename, but it does not properly prevent that filename from identifying a link or shortcut that resolves to an unintended resource."
sources:
  - name: MITRE CWE
    url: https://cwe.mitre.org/data/definitions/59.html
---

# CWE-59: Improper Link Resolution Before File Access ('Link Following')

**MITRE CWE weakness**

| | |
|--|--|
| Kind | Weakness |
| Abstraction | Base |
| Status | Draft |
| Likelihood of exploit | Medium |

## Description

The product attempts to access a file based on the filename, but it does not properly prevent that filename from identifying a link or shortcut that resolves to an unintended resource.



## Common consequences

- Confidentiality, Integrity, Access Control: Read Files or Directories, Modify Files or Directories, Bypass Protection Mechanism
- Other: Execute Unauthorized Code or Commands

## Mitigations

**Architecture and Design** — Follow the principle of least privilege when assigning access rights to entities in a software system. Denying access to a file can prevent an attacker from replacing that file with a link to a sensitive file. Ensure good compartmentalization in the system to provide protected areas that can be trusted.

## References

- CWE page: https://cwe.mitre.org/data/definitions/59.html
- CWE list: https://cwe.mitre.org/data/index.html
