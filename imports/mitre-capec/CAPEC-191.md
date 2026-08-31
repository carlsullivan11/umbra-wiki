---
slug: attack-pattern/CAPEC-191
title: "CAPEC-191 — Read Sensitive Constants Within an Executable"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-191]
cwe_ids: [CWE-798]
mitre_ids: [T1552.001]
related: [weakness/CWE-798, technique/T1552.001]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-191
updated_at: 2026-08-31
summary: "An adversary engages in activities to discover any sensitive constants present within the compiled code of an executable. These constants may include literal ASCII strings within the file itself, or possibly strings hard-coded into particular routines that can be revealed by code…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/191.html
---

# CAPEC-191: Read Sensitive Constants Within an Executable

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Low |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary engages in activities to discover any sensitive constants present within the compiled code of an executable. These constants may include literal ASCII strings within the file itself, or possibly strings hard-coded into particular routines that can be revealed by code refactoring methods including static and dynamic analysis.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-798](/wiki/p/weakness/CWE-798)

**ATT&CK techniques:** [T1552.001](/wiki/p/technique/T1552.001)

## Prerequisites

- Access to a binary or executable such that it can be analyzed by various utilities.

## Source

- [MITRE CAPEC CAPEC-191](https://capec.mitre.org/data/definitions/191.html)
