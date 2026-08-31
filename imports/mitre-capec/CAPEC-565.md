---
slug: attack-pattern/CAPEC-565
title: "CAPEC-565 — Password Spraying"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-565]
cwe_ids: [CWE-262, CWE-263, CWE-307, CWE-308, CWE-309, CWE-521, CWE-654]
mitre_ids: [T1110.003]
related: [weakness/CWE-262, weakness/CWE-263, weakness/CWE-307, weakness/CWE-308, weakness/CWE-309, weakness/CWE-521, weakness/CWE-654, technique/T1110.003]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-565
updated_at: 2026-08-31
summary: "In a Password Spraying attack, an adversary tries a small list (e.g. 3-5) of common or expected passwords, often matching the target's complexity policy, against a known list of user accounts to gain valid credentials. The adversary tries a particular password for each user accou…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/565.html
---

# CAPEC-565: Password Spraying

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

In a Password Spraying attack, an adversary tries a small list (e.g. 3-5) of common or expected passwords, often matching the target's complexity policy, against a known list of user accounts to gain valid credentials. The adversary tries a particular password for each user account, before moving onto the next password in the list. This approach assists the adversary in remaining undetected by avoiding rapid or frequent account lockouts. The adversary may then reattempt the process with additional passwords, once enough time has passed to prevent inducing a lockout.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-262](/wiki/p/weakness/CWE-262), [CWE-263](/wiki/p/weakness/CWE-263), [CWE-307](/wiki/p/weakness/CWE-307), [CWE-308](/wiki/p/weakness/CWE-308), [CWE-309](/wiki/p/weakness/CWE-309), [CWE-521](/wiki/p/weakness/CWE-521), [CWE-654](/wiki/p/weakness/CWE-654)

**ATT&CK techniques:** [T1110.003](/wiki/p/technique/T1110.003)

## Prerequisites

- The system/application uses one factor password based authentication.
- The system/application does not have a sound password policy that is being enforced.
- The system/application does not implement an effective password throttling mechanism.
- The adversary possesses a list of known user accounts on the target system/application.

## Skills required

- Low: A Password Spraying attack is very straightforward. A variety of password cracking tools are widely available.

## Consequences

- Confidentiality, Access Control, Authentication: Gain Privileges
- Confidentiality, Authorization: Read Data
- Integrity: Modify Data

## Mitigations

- Create a strong password policy and ensure that your system enforces this policy.
- Implement an intelligent password throttling mechanism. Care must be taken to assure that these mechanisms do not excessively enable account lockout attacks such as CAPEC-2.
- Leverage multi-factor authentication for all authentication services and prior to granting an entity access to the domain network.

## Source

- [MITRE CAPEC CAPEC-565](https://capec.mitre.org/data/definitions/565.html)
