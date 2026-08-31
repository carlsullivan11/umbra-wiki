---
slug: attack-pattern/CAPEC-160
title: "CAPEC-160 — Exploit Script-Based APIs"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-160]
cwe_ids: [CWE-346]
related: [weakness/CWE-346]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-160
updated_at: 2026-08-31
summary: "Some APIs support scripting instructions as arguments. Methods that take scripted instructions (or references to scripted instructions) can be very flexible and powerful. However, if an attacker can specify the script that serves as input to these methods they can gain access to …"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/160.html
---

# CAPEC-160: Exploit Script-Based APIs

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

Some APIs support scripting instructions as arguments. Methods that take scripted instructions (or references to scripted instructions) can be very flexible and powerful. However, if an attacker can specify the script that serves as input to these methods they can gain access to a great deal of functionality. For example, HTML pages support <script> tags that allow scripting languages to be embedded in the page and then interpreted by the receiving web browser. If the content provider is malicious, these scripts can compromise the client application. Some applications may even execute the scripts under their own identity (rather than the identity of the user providing the script) which can allow attackers to perform activities that would otherwise be denied to them.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-346](/wiki/p/weakness/CWE-346)

## Prerequisites

- The target application must include the use of APIs that execute scripts.
- The target application must allow the attacker to provide some or all of the arguments to one of these script interpretation methods and must fail to adequately filter these arguments for dangerous or unwanted script commands.

## Source

- [MITRE CAPEC CAPEC-160](https://capec.mitre.org/data/definitions/160.html)
