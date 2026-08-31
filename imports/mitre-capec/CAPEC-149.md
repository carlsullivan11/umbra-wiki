---
slug: attack-pattern/CAPEC-149
title: "CAPEC-149 — Explore for Predictable Temporary File Names"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-149]
cwe_ids: [CWE-377]
related: [weakness/CWE-377]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-149
updated_at: 2026-08-31
summary: "An attacker explores a target to identify the names and locations of predictable temporary files for the purpose of launching further attacks against the target. This involves analyzing naming conventions and storage locations of the temporary files created by a target applicatio…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/149.html
---

# CAPEC-149: Explore for Predictable Temporary File Names

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker explores a target to identify the names and locations of predictable temporary files for the purpose of launching further attacks against the target. This involves analyzing naming conventions and storage locations of the temporary files created by a target application. If an attacker can predict the names of temporary files they can use this information to mount other attacks, such as information gathering and symlink attacks.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-377](/wiki/p/weakness/CWE-377)

## Prerequisites

- The targeted application must create names for temporary files using a predictable procedure, e.g. using sequentially increasing numbers.
- The attacker must be able to see the names of the files the target is creating.

## Source

- [MITRE CAPEC CAPEC-149](https://capec.mitre.org/data/definitions/149.html)
