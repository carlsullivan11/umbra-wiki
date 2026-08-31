---
slug: attack-pattern/CAPEC-556
title: "CAPEC-556 — Replace File Extension Handlers"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-556]
cwe_ids: [CWE-284]
mitre_ids: [T1546.001]
related: [weakness/CWE-284, technique/T1546.001]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-556
updated_at: 2026-08-31
summary: "When a file is opened, its file handler is checked to determine which program opens the file. File handlers are configuration properties of many operating systems. Applications can modify the file handler for a given file extension to call an arbitrary program when a file with th…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/556.html
---

# CAPEC-556: Replace File Extension Handlers

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | — |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

When a file is opened, its file handler is checked to determine which program opens the file. File handlers are configuration properties of many operating systems. Applications can modify the file handler for a given file extension to call an arbitrary program when a file with the given extension is opened.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-284](/wiki/p/weakness/CWE-284)

**ATT&CK techniques:** [T1546.001](/wiki/p/technique/T1546.001)

## Mitigations

- Inspect registry for changes. Limit privileges of user accounts so changes to default file handlers can only be performed by authorized administrators.

## Source

- [MITRE CAPEC CAPEC-556](https://capec.mitre.org/data/definitions/556.html)
