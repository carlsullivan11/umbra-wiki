---
slug: weakness/CWE-5
title: "CWE-5 — J2EE Misconfiguration: Data Transmission Without Encryption"
page_type: weakness
tags: [cwe, weakness, mitre]
cwe_ids: [CWE-5]
related: [concept/cve-anatomy]
provenance: imported
import_source: mitre-cwe
import_id: CWE-5
updated_at: 2026-08-14
summary: "Information sent over a network can be compromised while in transit. An attacker may be able to read or modify the contents if the data are sent in plaintext or are weakly encrypted."
sources:
  - name: MITRE CWE
    url: https://cwe.mitre.org/data/definitions/5.html
---

# CWE-5: J2EE Misconfiguration: Data Transmission Without Encryption

**MITRE CWE weakness**

| | |
|--|--|
| Kind | Weakness |
| Abstraction | Variant |
| Status | Draft |
| Likelihood of exploit | — |

## Description

Information sent over a network can be compromised while in transit. An attacker may be able to read or modify the contents if the data are sent in plaintext or are weakly encrypted.



## Common consequences

- Confidentiality: Read Application Data
- Integrity: Modify Application Data

## Mitigations

**System Configuration** — The product configuration should ensure that SSL or an encryption mechanism of equivalent strength and vetted reputation is used for all access-controlled pages.

## References

- CWE page: https://cwe.mitre.org/data/definitions/5.html
- CWE list: https://cwe.mitre.org/data/index.html
