---
slug: attack-pattern/CAPEC-116
title: "CAPEC-116 — Excavation"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-116]
cwe_ids: [CWE-200, CWE-1243]
related: [weakness/CWE-200, weakness/CWE-1243]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-116
updated_at: 2026-08-31
summary: "An adversary actively probes the target in a manner that is designed to solicit information that could be leveraged for malicious purposes."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/116.html
---

# CAPEC-116: Excavation

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Medium |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary actively probes the target in a manner that is designed to solicit information that could be leveraged for malicious purposes.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-200](/wiki/p/weakness/CWE-200), [CWE-1243](/wiki/p/weakness/CWE-1243)

## Prerequisites

- An adversary requires some way of interacting with the system.

## Consequences

- Confidentiality: Read Data

## Mitigations

- Minimize error/response output to only what is necessary for functional use or corrective language.
- Remove potentially sensitive information that is not necessary for the application's functionality.

## Source

- [MITRE CAPEC CAPEC-116](https://capec.mitre.org/data/definitions/116.html)
