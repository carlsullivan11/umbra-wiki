---
slug: attack-pattern/CAPEC-166
title: "CAPEC-166 — Force the System to Reset Values"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-166]
cwe_ids: [CWE-306, CWE-1221, CWE-1232]
related: [weakness/CWE-306, weakness/CWE-1221, weakness/CWE-1232]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-166
updated_at: 2026-08-31
summary: "An attacker forces the target into a previous state in order to leverage potential weaknesses in the target dependent upon a prior configuration or state-dependent factors. Even in cases where an attacker may not be able to directly control the configuration of the targeted appli…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/166.html
---

# CAPEC-166: Force the System to Reset Values

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker forces the target into a previous state in order to leverage potential weaknesses in the target dependent upon a prior configuration or state-dependent factors. Even in cases where an attacker may not be able to directly control the configuration of the targeted application, they may be able to reset the configuration to a prior state since many applications implement reset functions.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-306](/wiki/p/weakness/CWE-306), [CWE-1221](/wiki/p/weakness/CWE-1221), [CWE-1232](/wiki/p/weakness/CWE-1232)

## Prerequisites

- The targeted application must have a reset function that returns the configuration of the application to an earlier state.
- The reset functionality must be inadequately protected against use.

## Source

- [MITRE CAPEC CAPEC-166](https://capec.mitre.org/data/definitions/166.html)
