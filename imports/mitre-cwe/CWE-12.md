---
slug: weakness/CWE-12
title: "CWE-12 — ASP.NET Misconfiguration: Missing Custom Error Page"
page_type: weakness
tags: [cwe, weakness, mitre]
cwe_ids: [CWE-12]
related: [concept/cve-anatomy]
provenance: imported
import_source: mitre-cwe
import_id: CWE-12
updated_at: 2026-08-14
summary: "An ASP .NET application must enable custom error pages in order to prevent attackers from mining information from the framework's built-in responses."
sources:
  - name: MITRE CWE
    url: https://cwe.mitre.org/data/definitions/12.html
---

# CWE-12: ASP.NET Misconfiguration: Missing Custom Error Page

**MITRE CWE weakness**

| | |
|--|--|
| Kind | Weakness |
| Abstraction | Variant |
| Status | Draft |
| Likelihood of exploit | — |

## Description

An ASP .NET application must enable custom error pages in order to prevent attackers from mining information from the framework's built-in responses.



## Common consequences

- Confidentiality: Read Application Data

## Mitigations

**System Configuration** — Handle exceptions appropriately in source code. ASP .NET applications should be configured to use custom error pages instead of the framework default page.

**Architecture and Design** — Do not attempt to process an error or attempt to mask it.

**Implementation** — Verify return values are correct and do not supply sensitive information about the system.

## References

- CWE page: https://cwe.mitre.org/data/definitions/12.html
- CWE list: https://cwe.mitre.org/data/index.html
