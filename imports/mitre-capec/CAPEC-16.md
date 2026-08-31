---
slug: attack-pattern/CAPEC-16
title: "CAPEC-16 — Dictionary-based Password Attack"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-16]
cwe_ids: [CWE-262, CWE-263, CWE-307, CWE-308, CWE-309, CWE-521, CWE-654]
related: [weakness/CWE-262, weakness/CWE-263, weakness/CWE-307, weakness/CWE-308, weakness/CWE-309, weakness/CWE-521, weakness/CWE-654]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-16
updated_at: 2026-08-31
summary: "An attacker tries each of the words in a dictionary as passwords to gain access to the system via some user's account. If the password chosen by the user was a word within the dictionary, this attack will be successful (in the absence of other mitigations). This is a specific ins…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/16.html
---

# CAPEC-16: Dictionary-based Password Attack

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker tries each of the words in a dictionary as passwords to gain access to the system via some user's account. If the password chosen by the user was a word within the dictionary, this attack will be successful (in the absence of other mitigations). This is a specific instance of the password brute forcing attack pattern. Dictionary Attacks differ from similar attacks such as Password Spraying (CAPEC-565) and Credential Stuffing (CAPEC-600), since they leverage unknown username/password combinations and don't care about inducing account lockouts.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-262](/wiki/p/weakness/CWE-262), [CWE-263](/wiki/p/weakness/CWE-263), [CWE-307](/wiki/p/weakness/CWE-307), [CWE-308](/wiki/p/weakness/CWE-308), [CWE-309](/wiki/p/weakness/CWE-309), [CWE-521](/wiki/p/weakness/CWE-521), [CWE-654](/wiki/p/weakness/CWE-654)

## Prerequisites

- The system uses one factor password based authentication.
- The system does not have a sound password policy that is being enforced.
- The system does not implement an effective password throttling mechanism.

## Skills required

- Low: A variety of password cracking tools and dictionaries are available to launch this type of an attack.

## Consequences

- Confidentiality, Access Control, Authentication: Gain Privileges
- Confidentiality: Read Data
- Integrity: Modify Data

## Mitigations

- Create a strong password policy and ensure that your system enforces this policy.
- Implement an intelligent password throttling mechanism. Care must be taken to assure that these mechanisms do not excessively enable account lockout attacks such as CAPEC-2.
- Leverage multi-factor authentication for all authentication services.

## Source

- [MITRE CAPEC CAPEC-16](https://capec.mitre.org/data/definitions/16.html)
