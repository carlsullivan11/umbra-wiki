---
slug: weakness/CWE-9
title: "CWE-9 — J2EE Misconfiguration: Weak Access Permissions for EJB Methods"
page_type: weakness
tags: [cwe, weakness, mitre]
cwe_ids: [CWE-9]
related: [concept/cve-anatomy]
provenance: imported
import_source: mitre-cwe
import_id: CWE-9
updated_at: 2026-08-14
summary: "If elevated access rights are assigned to EJB methods, then an attacker can take advantage of the permissions to exploit the product."
sources:
  - name: MITRE CWE
    url: https://cwe.mitre.org/data/definitions/9.html
---

# CWE-9: J2EE Misconfiguration: Weak Access Permissions for EJB Methods

**MITRE CWE weakness**

| | |
|--|--|
| Kind | Weakness |
| Abstraction | Variant |
| Status | Draft |
| Likelihood of exploit | — |

## Description

If elevated access rights are assigned to EJB methods, then an attacker can take advantage of the permissions to exploit the product.

If the EJB deployment descriptor contains one or more method permissions that grant access to the special ANYONE role, it indicates that access control for the application has not been fully thought through or that the application is structured in such a way that reasonable access control restrictions are impossible.

## Common consequences

- Other: Other

## Mitigations

**Architecture and Design** — Follow the principle of least privilege when assigning access rights to EJB methods. Permission to invoke EJB methods should not be granted to the ANYONE role.

## References

- CWE page: https://cwe.mitre.org/data/definitions/9.html
- CWE list: https://cwe.mitre.org/data/index.html
