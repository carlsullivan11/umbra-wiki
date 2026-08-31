---
slug: attack-pattern/CAPEC-541
title: "CAPEC-541 — Application Fingerprinting"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-541]
cwe_ids: [CWE-204, CWE-205, CWE-208]
mitre_ids: [T1592.002]
related: [weakness/CWE-204, weakness/CWE-205, weakness/CWE-208, technique/T1592.002]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-541
updated_at: 2026-08-31
summary: "An adversary engages in fingerprinting activities to determine the type or version of an application installed on a remote target."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/541.html
---

# CAPEC-541: Application Fingerprinting

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Low |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary engages in fingerprinting activities to determine the type or version of an application installed on a remote target.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-204](/wiki/p/weakness/CWE-204), [CWE-205](/wiki/p/weakness/CWE-205), [CWE-208](/wiki/p/weakness/CWE-208)

**ATT&CK techniques:** [T1592.002](/wiki/p/technique/T1592.002)

## Prerequisites

- None

## Source

- [MITRE CAPEC CAPEC-541](https://capec.mitre.org/data/definitions/541.html)
