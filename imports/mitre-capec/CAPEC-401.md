---
slug: attack-pattern/CAPEC-401
title: "CAPEC-401 — Physically Hacking Hardware"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-401]
cwe_ids: [CWE-1263]
related: [weakness/CWE-1263]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-401
updated_at: 2026-08-31
summary: "An adversary exploits a weakness in access control to gain access to currently installed hardware and precedes to implement changes or secretly replace a hardware component which undermines the system's integrity for the purpose of carrying out an attack."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/401.html
---

# CAPEC-401: Physically Hacking Hardware

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | High |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary exploits a weakness in access control to gain access to currently installed hardware and precedes to implement changes or secretly replace a hardware component which undermines the system's integrity for the purpose of carrying out an attack.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-1263](/wiki/p/weakness/CWE-1263)

## Source

- [MITRE CAPEC CAPEC-401](https://capec.mitre.org/data/definitions/401.html)
