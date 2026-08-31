---
slug: attack-pattern/CAPEC-509
title: "CAPEC-509 — Kerberoasting"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-509]
cwe_ids: [CWE-262, CWE-263, CWE-294, CWE-308, CWE-309, CWE-521, CWE-522]
mitre_ids: [T1558.003]
related: [weakness/CWE-262, weakness/CWE-263, weakness/CWE-294, weakness/CWE-308, weakness/CWE-309, weakness/CWE-521, weakness/CWE-522, technique/T1558.003]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-509
updated_at: 2026-08-31
summary: "Through the exploitation of how service accounts leverage Kerberos authentication with Service Principal Names (SPNs), the adversary obtains and subsequently cracks the hashed credentials of a service account target to exploit its privileges. The Kerberos authentication protocol …"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/509.html
---

# CAPEC-509: Kerberoasting

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | High |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

Through the exploitation of how service accounts leverage Kerberos authentication with Service Principal Names (SPNs), the adversary obtains and subsequently cracks the hashed credentials of a service account target to exploit its privileges. The Kerberos authentication protocol centers around a ticketing system which is used to request/grant access to services and to then access the requested services. As an authenticated user, the adversary may request Active Directory and obtain a service ticket with portions encrypted via RC4 with the private key of the authenticated account. By extracting the local ticket and saving it disk, the adversary can brute force the hashed value to reveal the target account credentials.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-262](/wiki/p/weakness/CWE-262), [CWE-263](/wiki/p/weakness/CWE-263), [CWE-294](/wiki/p/weakness/CWE-294), [CWE-308](/wiki/p/weakness/CWE-308), [CWE-309](/wiki/p/weakness/CWE-309), [CWE-521](/wiki/p/weakness/CWE-521), [CWE-522](/wiki/p/weakness/CWE-522)

**ATT&CK techniques:** [T1558.003](/wiki/p/technique/T1558.003)

## Prerequisites

- The adversary requires access as an authenticated user on the system. This attack pattern relates to elevating privileges.
- The adversary requires use of a third-party credential harvesting tool (e.g., Mimikatz).
- The adversary requires a brute force tool.

## Skills required

- Medium: 

## Consequences

- Confidentiality: Gain Privileges

## Mitigations

- Monitor system and domain logs for abnormal access.
- Employ a robust password policy for service accounts. Passwords should be of adequate length and complexity, and they should expire after a period of time.
- Employ the principle of least privilege: limit service accounts privileges to what is required for functionality and no more.
- Enable AES Kerberos encryption (or another stronger encryption algorithm), rather than RC4, where possible.

## Source

- [MITRE CAPEC CAPEC-509](https://capec.mitre.org/data/definitions/509.html)
