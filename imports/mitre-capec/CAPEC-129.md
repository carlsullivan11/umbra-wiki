---
slug: attack-pattern/CAPEC-129
title: "CAPEC-129 — Pointer Manipulation"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-129]
cwe_ids: [CWE-682, CWE-822, CWE-823]
related: [weakness/CWE-682, weakness/CWE-822, weakness/CWE-823]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-129
updated_at: 2026-08-31
summary: "This attack pattern involves an adversary manipulating a pointer within a target application resulting in the application accessing an unintended memory location. This can result in the crashing of the application or, for certain pointer values, access to data that would not norm…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/129.html
---

# CAPEC-129: Pointer Manipulation

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

This attack pattern involves an adversary manipulating a pointer within a target application resulting in the application accessing an unintended memory location. This can result in the crashing of the application or, for certain pointer values, access to data that would not normally be possible or the execution of arbitrary code. Since pointers are simply integer variables, Integer Attacks may often be used in Pointer Attacks.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-682](/wiki/p/weakness/CWE-682), [CWE-822](/wiki/p/weakness/CWE-822), [CWE-823](/wiki/p/weakness/CWE-823)

## Prerequisites

- The target application must have a pointer variable that the attacker can influence to hold an arbitrary value.

## Source

- [MITRE CAPEC CAPEC-129](https://capec.mitre.org/data/definitions/129.html)
