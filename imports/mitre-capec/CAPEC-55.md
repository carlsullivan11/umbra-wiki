---
slug: attack-pattern/CAPEC-55
title: "CAPEC-55 — Rainbow Table Password Cracking"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-55]
cwe_ids: [CWE-261, CWE-262, CWE-263, CWE-308, CWE-309, CWE-521, CWE-654, CWE-916]
mitre_ids: [T1110.002]
related: [weakness/CWE-261, weakness/CWE-262, weakness/CWE-263, weakness/CWE-308, weakness/CWE-309, weakness/CWE-521, weakness/CWE-654, weakness/CWE-916, technique/T1110.002]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-55
updated_at: 2026-08-31
summary: "An attacker gets access to the database table where hashes of passwords are stored. They then use a rainbow table of pre-computed hash chains to attempt to look up the original password. Once the original password corresponding to the hash is obtained, the attacker uses the origi…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/55.html
---

# CAPEC-55: Rainbow Table Password Cracking

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker gets access to the database table where hashes of passwords are stored. They then use a rainbow table of pre-computed hash chains to attempt to look up the original password. Once the original password corresponding to the hash is obtained, the attacker uses the original password to gain access to the system.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-261](/wiki/p/weakness/CWE-261), [CWE-262](/wiki/p/weakness/CWE-262), [CWE-263](/wiki/p/weakness/CWE-263), [CWE-308](/wiki/p/weakness/CWE-308), [CWE-309](/wiki/p/weakness/CWE-309), [CWE-521](/wiki/p/weakness/CWE-521), [CWE-654](/wiki/p/weakness/CWE-654), [CWE-916](/wiki/p/weakness/CWE-916)

**ATT&CK techniques:** [T1110.002](/wiki/p/technique/T1110.002)

## Prerequisites

- Hash of the original password is available to the attacker. For a better chance of success, an attacker should have more than one hash of the original password, and ideally the whole table.
- Salt was not used to create the hash of the original password. Otherwise the rainbow tables have to be re-computed, which is very expensive and will make the attack effectively infeasible (especially if salt was added in iterations).
- The system uses one factor password based authentication.

## Skills required

- Low: A variety of password cracking tools are available that can leverage a rainbow table. The more difficult part is to obtain the password hash(es) in the first place.

## Consequences

- Confidentiality, Access Control, Authorization: Gain Privileges

## Mitigations

- Use salt when computing password hashes. That is, concatenate the salt (random bits) with the original password prior to hashing it.

## Source

- [MITRE CAPEC CAPEC-55](https://capec.mitre.org/data/definitions/55.html)
