---
slug: attack-pattern/CAPEC-70
title: "CAPEC-70 — Try Common or Default Usernames and Passwords"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-70]
cwe_ids: [CWE-262, CWE-263, CWE-308, CWE-309, CWE-521, CWE-654, CWE-798]
mitre_ids: [T1078.001]
related: [weakness/CWE-262, weakness/CWE-263, weakness/CWE-308, weakness/CWE-309, weakness/CWE-521, weakness/CWE-654, weakness/CWE-798, technique/T1078.001]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-70
updated_at: 2026-08-31
summary: "An adversary may try certain common or default usernames and passwords to gain access into the system and perform unauthorized actions. An adversary may try an intelligent brute force using empty passwords, known vendor default credentials, as well as a dictionary of common usern…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/70.html
---

# CAPEC-70: Try Common or Default Usernames and Passwords

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary may try certain common or default usernames and passwords to gain access into the system and perform unauthorized actions. An adversary may try an intelligent brute force using empty passwords, known vendor default credentials, as well as a dictionary of common usernames and passwords. Many vendor products come preconfigured with default (and thus well-known) usernames and passwords that should be deleted prior to usage in a production environment. It is a common mistake to forget to remove these default login credentials. Another problem is that users would pick very simple (common) passwords (e.g. "secret" or "password") that make it easier for the attacker to gain access to the system compared to using a brute force attack or even a dictionary attack using a full dictionary.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-262](/wiki/p/weakness/CWE-262), [CWE-263](/wiki/p/weakness/CWE-263), [CWE-308](/wiki/p/weakness/CWE-308), [CWE-309](/wiki/p/weakness/CWE-309), [CWE-521](/wiki/p/weakness/CWE-521), [CWE-654](/wiki/p/weakness/CWE-654), [CWE-798](/wiki/p/weakness/CWE-798)

**ATT&CK techniques:** [T1078.001](/wiki/p/technique/T1078.001)

## Prerequisites

- The system uses one factor password based authentication.The adversary has the means to interact with the system.

## Skills required

- Low: An adversary just needs to gain access to common default usernames/passwords specific to the technologies used by the system. Additionally, a brute force attack leveraging common passwords can be easily realized if the user name is known.

## Consequences

- Confidentiality, Access Control, Authorization: Gain Privileges

## Mitigations

- Delete all default account credentials that may be put in by the product vendor.
- Implement a password throttling mechanism. This mechanism should take into account both the IP address and the log in name of the user.
- Put together a strong password policy and make sure that all user created passwords comply with it. Alternatively automatically generate strong passwords for users.
- Passwords need to be recycled to prevent aging, that is every once in a while a new password must be chosen.

## Source

- [MITRE CAPEC CAPEC-70](https://capec.mitre.org/data/definitions/70.html)
