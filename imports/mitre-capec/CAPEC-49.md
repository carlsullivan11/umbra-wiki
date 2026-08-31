---
slug: attack-pattern/CAPEC-49
title: "CAPEC-49 — Password Brute Forcing"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-49]
cwe_ids: [CWE-257, CWE-262, CWE-263, CWE-307, CWE-308, CWE-309, CWE-521, CWE-654]
mitre_ids: [T1110.001]
related: [weakness/CWE-257, weakness/CWE-262, weakness/CWE-263, weakness/CWE-307, weakness/CWE-308, weakness/CWE-309, weakness/CWE-521, weakness/CWE-654, technique/T1110.001]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-49
updated_at: 2026-08-31
summary: "An adversary tries every possible value for a password until they succeed. A brute force attack, if feasible computationally, will always be successful because it will essentially go through all possible passwords given the alphabet used (lower case letters, upper case letters, n…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/49.html
---

# CAPEC-49: Password Brute Forcing

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary tries every possible value for a password until they succeed. A brute force attack, if feasible computationally, will always be successful because it will essentially go through all possible passwords given the alphabet used (lower case letters, upper case letters, numbers, symbols, etc.) and the maximum length of the password.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-257](/wiki/p/weakness/CWE-257), [CWE-262](/wiki/p/weakness/CWE-262), [CWE-263](/wiki/p/weakness/CWE-263), [CWE-307](/wiki/p/weakness/CWE-307), [CWE-308](/wiki/p/weakness/CWE-308), [CWE-309](/wiki/p/weakness/CWE-309), [CWE-521](/wiki/p/weakness/CWE-521), [CWE-654](/wiki/p/weakness/CWE-654)

**ATT&CK techniques:** [T1110.001](/wiki/p/technique/T1110.001)

## Prerequisites

- An adversary needs to know a username to target.
- The system uses password based authentication as the one factor authentication mechanism.
- An application does not have a password throttling mechanism in place. A good password throttling mechanism will make it almost impossible computationally to brute force a password as it may either lock out the user after a certain number of incorrect attempts or introduce time out periods. Both of these would make a brute force attack impractical.

## Skills required

- Low: A brute force attack is very straightforward. A variety of password cracking tools are widely available.

## Consequences

- Confidentiality, Access Control, Authorization: Gain Privileges
- Confidentiality: Read Data
- Integrity: Modify Data

## Mitigations

- Implement a password throttling mechanism. This mechanism should take into account both the IP address and the log in name of the user.
- Put together a strong password policy and make sure that all user created passwords comply with it. Alternatively automatically generate strong passwords for users.
- Passwords need to be recycled to prevent aging, that is every once in a while a new password must be chosen.

## Source

- [MITRE CAPEC CAPEC-49](https://capec.mitre.org/data/definitions/49.html)
