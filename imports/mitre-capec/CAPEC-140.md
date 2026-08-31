---
slug: attack-pattern/CAPEC-140
title: "CAPEC-140 — Bypassing of Intermediate Forms in Multiple-Form Sets"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-140]
cwe_ids: [CWE-372]
related: [weakness/CWE-372]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-140
updated_at: 2026-08-31
summary: "Some web applications require users to submit information through an ordered sequence of web forms. This is often done if there is a very large amount of information being collected or if information on earlier forms is used to pre-populate fields or determine which additional in…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/140.html
---

# CAPEC-140: Bypassing of Intermediate Forms in Multiple-Form Sets

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

Some web applications require users to submit information through an ordered sequence of web forms. This is often done if there is a very large amount of information being collected or if information on earlier forms is used to pre-populate fields or determine which additional information the application needs to collect. An attacker who knows the names of the various forms in the sequence may be able to explicitly type in the name of a later form and navigate to it without first going through the previous forms. This can result in incomplete collection of information, incorrect assumptions about the information submitted by the attacker, or other problems that can impair the functioning of the application.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-372](/wiki/p/weakness/CWE-372)

## Prerequisites

- The target must collect information from the user in a series of forms where each form has its own URL that the attacker can anticipate and the application must fail to detect attempts to access intermediate forms without first filling out the previous forms.

## Source

- [MITRE CAPEC CAPEC-140](https://capec.mitre.org/data/definitions/140.html)
