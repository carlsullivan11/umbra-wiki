---
slug: attack-pattern/CAPEC-560
title: "CAPEC-560 — Use of Known Domain Credentials"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-560]
cwe_ids: [CWE-262, CWE-263, CWE-307, CWE-308, CWE-309, CWE-522, CWE-654, CWE-1273]
mitre_ids: [T1078]
related: [weakness/CWE-262, weakness/CWE-263, weakness/CWE-307, weakness/CWE-308, weakness/CWE-309, weakness/CWE-522, weakness/CWE-654, weakness/CWE-1273, technique/T1078]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-560
updated_at: 2026-08-31
summary: "An adversary guesses or obtains (i.e. steals or purchases) legitimate credentials (e.g. userID/password) to achieve authentication and to perform authorized actions under the guise of an authenticated user or service."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/560.html
---

# CAPEC-560: Use of Known Domain Credentials

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary guesses or obtains (i.e. steals or purchases) legitimate credentials (e.g. userID/password) to achieve authentication and to perform authorized actions under the guise of an authenticated user or service.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-262](/wiki/p/weakness/CWE-262), [CWE-263](/wiki/p/weakness/CWE-263), [CWE-307](/wiki/p/weakness/CWE-307), [CWE-308](/wiki/p/weakness/CWE-308), [CWE-309](/wiki/p/weakness/CWE-309), [CWE-522](/wiki/p/weakness/CWE-522), [CWE-654](/wiki/p/weakness/CWE-654), [CWE-1273](/wiki/p/weakness/CWE-1273)

**ATT&CK techniques:** [T1078](/wiki/p/technique/T1078)

## Prerequisites

- The system/application uses one factor password based authentication, SSO, and/or cloud-based authentication.
- The system/application does not have a sound password policy that is being enforced.
- The system/application does not implement an effective password throttling mechanism.
- The adversary possesses a list of known user accounts and corresponding passwords that may exist on the target.

## Skills required

- Low: Once an adversary obtains a known credential, leveraging it is trivial.

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

- [MITRE CAPEC CAPEC-560](https://capec.mitre.org/data/definitions/560.html)
