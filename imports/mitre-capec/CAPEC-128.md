---
slug: attack-pattern/CAPEC-128
title: "CAPEC-128 — Integer Attacks"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-128]
cwe_ids: [CWE-682]
related: [weakness/CWE-682]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-128
updated_at: 2026-08-31
summary: "An attacker takes advantage of the structure of integer variables to cause these variables to assume values that are not expected by an application. For example, adding one to the largest positive integer in a signed integer variable results in a negative number. Negative numbers…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/128.html
---

# CAPEC-128: Integer Attacks

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker takes advantage of the structure of integer variables to cause these variables to assume values that are not expected by an application. For example, adding one to the largest positive integer in a signed integer variable results in a negative number. Negative numbers may be illegal in an application and the application may prevent an attacker from providing them directly, but the application may not consider that adding two positive numbers can create a negative number do to the structure of integer storage formats.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-682](/wiki/p/weakness/CWE-682)

## Prerequisites

- The target application must have an integer variable for which only some of the possible integer values are expected by the application and where there are no checks on the value of the variable before use.
- The attacker must be able to manipulate the targeted integer variable such that normal operations result in non-standard values due to the storage structure of integers.

## Source

- [MITRE CAPEC CAPEC-128](https://capec.mitre.org/data/definitions/128.html)
