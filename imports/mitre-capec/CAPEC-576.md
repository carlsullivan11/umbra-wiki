---
slug: attack-pattern/CAPEC-576
title: "CAPEC-576 — Group Permission Footprinting"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-576]
cwe_ids: [CWE-200]
mitre_ids: [T1069, T1615]
related: [weakness/CWE-200, technique/T1069, technique/T1615]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-576
updated_at: 2026-08-31
summary: "An adversary exploits functionality meant to identify information about user groups and their permissions on the target system to an authorized user. By knowing what users/permissions are registered on the target system, the adversary can inform further and more targeted maliciou…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/576.html
---

# CAPEC-576: Group Permission Footprinting

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Low |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary exploits functionality meant to identify information about user groups and their permissions on the target system to an authorized user. By knowing what users/permissions are registered on the target system, the adversary can inform further and more targeted malicious behavior. An example Windows command which can list local groups is "net localgroup".

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-200](/wiki/p/weakness/CWE-200)

**ATT&CK techniques:** [T1069](/wiki/p/technique/T1069), [T1615](/wiki/p/technique/T1615)

## Prerequisites

- The adversary must have gained access to the target system via physical or logical means in order to carry out this attack.

## Consequences

- Confidentiality: Other
- Confidentiality, Access Control, Authorization: Bypass Protection Mechanism, Hide Activities

## Mitigations

- Identify programs (such as "net") that may be used to enumerate local group permissions and block them by using a software restriction Policy or tools that restrict program execution by using a process allowlist.

## Source

- [MITRE CAPEC CAPEC-576](https://capec.mitre.org/data/definitions/576.html)
