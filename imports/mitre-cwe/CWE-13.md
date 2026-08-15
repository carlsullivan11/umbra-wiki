---
slug: weakness/CWE-13
title: "CWE-13 — ASP.NET Misconfiguration: Password in Configuration File"
page_type: weakness
tags: [cwe, weakness, mitre]
cwe_ids: [CWE-13]
related: [concept/cve-anatomy]
provenance: imported
import_source: mitre-cwe
import_id: CWE-13
updated_at: 2026-08-14
summary: "Storing a plaintext password in a configuration file allows anyone who can read the file access to the password-protected resource making them an easy target for attackers."
sources:
  - name: MITRE CWE
    url: https://cwe.mitre.org/data/definitions/13.html
---

# CWE-13: ASP.NET Misconfiguration: Password in Configuration File

**MITRE CWE weakness**

| | |
|--|--|
| Kind | Weakness |
| Abstraction | Variant |
| Status | Draft |
| Likelihood of exploit | — |

## Description

Storing a plaintext password in a configuration file allows anyone who can read the file access to the password-protected resource making them an easy target for attackers.



## Common consequences

- Access Control: Gain Privileges or Assume Identity

## Mitigations

**Implementation** — Credentials stored in configuration files should be encrypted, Use standard APIs and industry accepted algorithms to encrypt the credentials stored in configuration files.

## References

- CWE page: https://cwe.mitre.org/data/definitions/13.html
- CWE list: https://cwe.mitre.org/data/index.html
