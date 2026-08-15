---
slug: weakness/CWE-7
title: "CWE-7 — J2EE Misconfiguration: Missing Custom Error Page"
page_type: weakness
tags: [cwe, weakness, mitre]
cwe_ids: [CWE-7]
related: [concept/cve-anatomy]
provenance: imported
import_source: mitre-cwe
import_id: CWE-7
updated_at: 2026-08-14
summary: "The default error page of a web application should not display sensitive information about the product."
sources:
  - name: MITRE CWE
    url: https://cwe.mitre.org/data/definitions/7.html
---

# CWE-7: J2EE Misconfiguration: Missing Custom Error Page

**MITRE CWE weakness**

| | |
|--|--|
| Kind | Weakness |
| Abstraction | Variant |
| Status | Incomplete |
| Likelihood of exploit | — |

## Description

The default error page of a web application should not display sensitive information about the product.

A Web application must define a default error page for 4xx errors (e.g. 404), 5xx (e.g. 500) errors and catch java.lang.Throwable exceptions to prevent attackers from mining information from the application container's built-in error response. When an attacker explores a web site looking for vulnerabilities, the amount of information that the site provides is crucial to the eventual success or failure of any attempted attacks.

## Common consequences

- Confidentiality: Read Application Data

## Mitigations

**Implementation** — Handle exceptions appropriately in source code.

**Implementation** — Always define appropriate error pages. The application configuration should specify a default error page in order to guarantee that the application will never leak error messages to an attacker. Handling standard HTTP error codes is useful and user-friendly in addition to being a good security practice, and a good configuration will also define a last-chance error handler that catches any exception that could possibly be thrown by the application.

**Implementation** — Do not attempt to process an error or attempt to mask it.

**Implementation** — Verify return values are correct and do not supply sensitive information about the system.

## References

- CWE page: https://cwe.mitre.org/data/definitions/7.html
- CWE list: https://cwe.mitre.org/data/index.html
