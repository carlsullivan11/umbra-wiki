---
slug: attack-pattern/CAPEC-167
title: "CAPEC-167 — White Box Reverse Engineering"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-167]
cwe_ids: [CWE-1323]
related: [weakness/CWE-1323]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-167
updated_at: 2026-08-31
summary: "An attacker discovers the structure, function, and composition of a type of computer software through white box analysis techniques. White box techniques involve methods which can be applied to a piece of software when an executable or some other compiled object can be directly s…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/167.html
---

# CAPEC-167: White Box Reverse Engineering

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker discovers the structure, function, and composition of a type of computer software through white box analysis techniques. White box techniques involve methods which can be applied to a piece of software when an executable or some other compiled object can be directly subjected to analysis, revealing at least a portion of its machine instructions that can be observed upon execution.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-1323](/wiki/p/weakness/CWE-1323)

## Prerequisites

- Direct access to the object or software.

## Source

- [MITRE CAPEC CAPEC-167](https://capec.mitre.org/data/definitions/167.html)
