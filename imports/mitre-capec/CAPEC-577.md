---
slug: attack-pattern/CAPEC-577
title: "CAPEC-577 — Owner Footprinting"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-577]
cwe_ids: [CWE-200]
mitre_ids: [T1033]
related: [weakness/CWE-200, technique/T1033]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-577
updated_at: 2026-08-31
summary: "An adversary exploits functionality meant to identify information about the primary users on the target system to an authorized user. They may do this, for example, by reviewing logins or file modification times. By knowing what owners use the target system, the adversary can inf…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/577.html
---

# CAPEC-577: Owner Footprinting

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Low |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary exploits functionality meant to identify information about the primary users on the target system to an authorized user. They may do this, for example, by reviewing logins or file modification times. By knowing what owners use the target system, the adversary can inform further and more targeted malicious behavior. An example Windows command that may accomplish this is "dir /A ntuser.dat". Which will display the last modified time of a user's ntuser.dat file when run within the root folder of a user. This time is synonymous with the last time that user was logged in.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-200](/wiki/p/weakness/CWE-200)

**ATT&CK techniques:** [T1033](/wiki/p/technique/T1033)

## Prerequisites

- The adversary must have gained access to the target system via physical or logical means in order to carry out this attack.
- Administrator permissions are required to view the home folder of other users.

## Consequences

- Confidentiality: Other
- Confidentiality, Access Control, Authorization: Bypass Protection Mechanism, Hide Activities

## Mitigations

- Ensure that proper permissions on files and folders are enacted to limit accessibility.

## Source

- [MITRE CAPEC CAPEC-577](https://capec.mitre.org/data/definitions/577.html)
