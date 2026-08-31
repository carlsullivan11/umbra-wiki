---
slug: attack-pattern/CAPEC-153
title: "CAPEC-153 — Input Data Manipulation"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-153]
cwe_ids: [CWE-20]
related: [weakness/CWE-20]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-153
updated_at: 2026-08-31
summary: "An attacker exploits a weakness in input validation by controlling the format, structure, and composition of data to an input-processing interface. By supplying input of a non-standard or unexpected form an attacker can adversely impact the security of the target."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/153.html
---

# CAPEC-153: Input Data Manipulation

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker exploits a weakness in input validation by controlling the format, structure, and composition of data to an input-processing interface. By supplying input of a non-standard or unexpected form an attacker can adversely impact the security of the target.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-20](/wiki/p/weakness/CWE-20)

## Prerequisites

- The target must accept user data for processing and the manner in which this data is processed must depend on some aspect of the format or flags that the attacker can control.

## Source

- [MITRE CAPEC CAPEC-153](https://capec.mitre.org/data/definitions/153.html)
