---
slug: attack-pattern/CAPEC-620
title: "CAPEC-620 — Drop Encryption Level"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-620]
cwe_ids: [CWE-757]
mitre_ids: [T1600]
related: [weakness/CWE-757, technique/T1600]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-620
updated_at: 2026-08-31
summary: "An attacker forces the encryption level to be lowered, thus enabling a successful attack against the encrypted data."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/620.html
---

# CAPEC-620: Drop Encryption Level

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker forces the encryption level to be lowered, thus enabling a successful attack against the encrypted data.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-757](/wiki/p/weakness/CWE-757)

**ATT&CK techniques:** [T1600](/wiki/p/technique/T1600)

## Consequences

- Access Control: Bypass Protection Mechanism

## Source

- [MITRE CAPEC CAPEC-620](https://capec.mitre.org/data/definitions/620.html)
