---
slug: attack-pattern/CAPEC-439
title: "CAPEC-439 — Manipulation During Distribution"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-439]
cwe_ids: [CWE-1269]
mitre_ids: [T1195]
related: [weakness/CWE-1269, technique/T1195]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-439
updated_at: 2026-08-31
summary: "An attacker undermines the integrity of a product, software, or technology at some stage of the distribution channel. The core threat of modification or manipulation during distribution arise from the many stages of distribution, as a product may traverse multiple suppliers and i…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/439.html
---

# CAPEC-439: Manipulation During Distribution

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | — |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker undermines the integrity of a product, software, or technology at some stage of the distribution channel. The core threat of modification or manipulation during distribution arise from the many stages of distribution, as a product may traverse multiple suppliers and integrators as the final asset is delivered. Components and services provided from a manufacturer to a supplier may be tampered with during integration or packaging.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-1269](/wiki/p/weakness/CWE-1269)

**ATT&CK techniques:** [T1195](/wiki/p/technique/T1195)

## Source

- [MITRE CAPEC CAPEC-439](https://capec.mitre.org/data/definitions/439.html)
