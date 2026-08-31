---
slug: attack-pattern/CAPEC-190
title: "CAPEC-190 — Reverse Engineer an Executable to Expose Assumed Hidden Functionality"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-190]
cwe_ids: [CWE-912]
related: [weakness/CWE-912]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-190
updated_at: 2026-08-31
summary: "An attacker analyzes a binary file or executable for the purpose of discovering the structure, function, and possibly source-code of the file by using a variety of analysis techniques to effectively determine how the software functions and operates. This type of analysis is also …"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/190.html
---

# CAPEC-190: Reverse Engineer an Executable to Expose Assumed Hidden Functionality

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Low |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker analyzes a binary file or executable for the purpose of discovering the structure, function, and possibly source-code of the file by using a variety of analysis techniques to effectively determine how the software functions and operates. This type of analysis is also referred to as Reverse Code Engineering, as techniques exist for extracting source code from an executable. Several techniques are often employed for this purpose, both black box and white box. The use of computer bus analyzers and packet sniffers allows the binary to be studied at a level of interactions with its computing environment, such as a host OS, inter-process communication, and/or network communication. This type of analysis falls into the 'black box' category because it involves behavioral analysis of the software without reference to source code, object code, or protocol specifications.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-912](/wiki/p/weakness/CWE-912)

## Source

- [MITRE CAPEC CAPEC-190](https://capec.mitre.org/data/definitions/190.html)
