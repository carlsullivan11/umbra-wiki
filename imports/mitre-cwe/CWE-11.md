---
slug: weakness/CWE-11
title: "CWE-11 — ASP.NET Misconfiguration: Creating Debug Binary"
page_type: weakness
tags: [cwe, weakness, mitre]
cwe_ids: [CWE-11]
related: [concept/cve-anatomy]
provenance: imported
import_source: mitre-cwe
import_id: CWE-11
updated_at: 2026-08-14
summary: "Debugging messages help attackers learn about the system and plan a form of attack."
sources:
  - name: MITRE CWE
    url: https://cwe.mitre.org/data/definitions/11.html
---

# CWE-11: ASP.NET Misconfiguration: Creating Debug Binary

**MITRE CWE weakness**

| | |
|--|--|
| Kind | Weakness |
| Abstraction | Variant |
| Status | Draft |
| Likelihood of exploit | — |

## Description

Debugging messages help attackers learn about the system and plan a form of attack.

ASP .NET applications can be configured to produce debug binaries. These binaries give detailed debugging messages and should not be used in production environments. Debug binaries are meant to be used in a development or testing environment and can pose a security risk if they are deployed to production.

## Common consequences

- Confidentiality: Read Application Data

## Mitigations

**System Configuration** — Avoid releasing debug binaries into the production environment. Change the debug mode to false when the application is deployed into production.

## References

- CWE page: https://cwe.mitre.org/data/definitions/11.html
- CWE list: https://cwe.mitre.org/data/index.html
