---
slug: attack-pattern/CAPEC-600
title: "CAPEC-600 — Credential Stuffing"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-600]
cwe_ids: [CWE-262, CWE-263, CWE-307, CWE-308, CWE-309, CWE-522, CWE-654]
mitre_ids: [T1110.004]
related: [weakness/CWE-262, weakness/CWE-263, weakness/CWE-307, weakness/CWE-308, weakness/CWE-309, weakness/CWE-522, weakness/CWE-654, technique/T1110.004]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-600
updated_at: 2026-08-31
summary: "An adversary tries known username/password combinations against different systems, applications, or services to gain additional authenticated access. Credential Stuffing attacks rely upon the fact that many users leverage the same username/password combination for multiple system…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/600.html
---

# CAPEC-600: Credential Stuffing

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary tries known username/password combinations against different systems, applications, or services to gain additional authenticated access. Credential Stuffing attacks rely upon the fact that many users leverage the same username/password combination for multiple systems, applications, and services.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-262](/wiki/p/weakness/CWE-262), [CWE-263](/wiki/p/weakness/CWE-263), [CWE-307](/wiki/p/weakness/CWE-307), [CWE-308](/wiki/p/weakness/CWE-308), [CWE-309](/wiki/p/weakness/CWE-309), [CWE-522](/wiki/p/weakness/CWE-522), [CWE-654](/wiki/p/weakness/CWE-654)

**ATT&CK techniques:** [T1110.004](/wiki/p/technique/T1110.004)

## Prerequisites

- The system/application uses one factor password based authentication, SSO, and/or cloud-based authentication.
- The system/application does not have a sound password policy that is being enforced.
- The system/application does not implement an effective password throttling mechanism.
- The adversary possesses a list of known user accounts and corresponding passwords that may exist on the target.

## Skills required

- Low: A Credential Stuffing attack is very straightforward.

## Consequences

- Confidentiality, Access Control, Authentication: Gain Privileges
- Confidentiality, Authorization: Read Data
- Integrity: Modify Data

## Mitigations

- Leverage multi-factor authentication for all authentication services and prior to granting an entity access to the domain network.
- Create a strong password policy and ensure that your system enforces this policy.
- Ensure users are not reusing username/password combinations for multiple systems, applications, or services.
- Do not reuse local administrator account credentials across systems.
- Deny remote use of local admin credentials to log into domain systems.
- Do not allow accounts to be a local administrator on more than one system.
- Implement an intelligent password throttling mechanism. Care must be taken to assure that these mechanisms do not excessively enable account lockout attacks such as CAPEC-2.
- Monitor system and domain logs for abnormal credential access.

## Source

- [MITRE CAPEC CAPEC-600](https://capec.mitre.org/data/definitions/600.html)
