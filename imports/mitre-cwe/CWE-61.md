---
slug: weakness/CWE-61
title: "CWE-61 — UNIX Symbolic Link (Symlink) Following"
page_type: weakness
tags: [cwe, weakness, mitre]
cwe_ids: [CWE-61]
related: [concept/cve-anatomy]
provenance: imported
import_source: mitre-cwe
import_id: CWE-61
updated_at: 2026-08-14
summary: "The product, when opening a file or directory, does not sufficiently account for when the file is a symbolic link that resolves to a target outside of the intended control sphere. This could allow an "
sources:
  - name: MITRE CWE
    url: https://cwe.mitre.org/data/definitions/61.html
---

# CWE-61: UNIX Symbolic Link (Symlink) Following

**MITRE CWE weakness**

| | |
|--|--|
| Kind | Weakness |
| Abstraction | Compound |
| Status | Incomplete |
| Likelihood of exploit | High |

## Description

The product, when opening a file or directory, does not sufficiently account for when the file is a symbolic link that resolves to a target outside of the intended control sphere. This could allow an attacker to cause the product to operate on unauthorized files.

A product that allows UNIX symbolic links (symlink) as part of paths whether in internal code or through user input can allow an attacker to spoof the symbolic link and traverse the file system to unintended locations or access arbitrary files. The symbolic link can permit an attacker to read/write/corrupt a file that they originally did not have permissions to access.

## Common consequences

- Confidentiality, Integrity: Read Files or Directories, Modify Files or Directories

## Mitigations

**Implementation** — Symbolic link attacks often occur when a program creates a tmp directory that stores files/links. Access to the directory should be restricted to the program as to prevent attackers from manipulating the files.

**Architecture and Design** — Follow the principle of least privilege when assigning access rights to entities in a software system. Denying access to a file can prevent an attacker from replacing that file with a link to a sensitive file. Ensure good compartmentalization in the system to provide protected areas that can be trusted.

## References

- CWE page: https://cwe.mitre.org/data/definitions/61.html
- CWE list: https://cwe.mitre.org/data/index.html
