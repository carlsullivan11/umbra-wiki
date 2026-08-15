---
slug: weakness/CWE-14
title: "CWE-14 — Compiler Removal of Code to Clear Buffers"
page_type: weakness
tags: [cwe, weakness, mitre]
cwe_ids: [CWE-14]
related: [concept/cve-anatomy]
provenance: imported
import_source: mitre-cwe
import_id: CWE-14
updated_at: 2026-08-14
summary: "Sensitive memory is cleared according to the source code, but compiler optimizations leave the memory untouched when it is not read from again, aka 'dead store removal.'"
sources:
  - name: MITRE CWE
    url: https://cwe.mitre.org/data/definitions/14.html
---

# CWE-14: Compiler Removal of Code to Clear Buffers

**MITRE CWE weakness**

| | |
|--|--|
| Kind | Weakness |
| Abstraction | Variant |
| Status | Draft |
| Likelihood of exploit | — |

## Description

Sensitive memory is cleared according to the source code, but compiler optimizations leave the memory untouched when it is not read from again, aka "dead store removal."

This compiler optimization error occurs when: Secret data are stored in memory. The secret data are scrubbed from memory by overwriting its contents. The source code is compiled using an optimizing compiler, which identifies and removes the function that overwrites the contents as a dead store because the memory is not used subsequently.

## Common consequences

- Confidentiality, Access Control: Read Memory, Bypass Protection Mechanism

## Mitigations

**Implementation** — Store the sensitive data in a "volatile" memory location if available.

**Build and Compilation** — If possible, configure your compiler so that it does not remove dead stores.

**Architecture and Design** — Where possible, encrypt sensitive data that are used by a software system.

## References

- CWE page: https://cwe.mitre.org/data/definitions/14.html
- CWE list: https://cwe.mitre.org/data/index.html
