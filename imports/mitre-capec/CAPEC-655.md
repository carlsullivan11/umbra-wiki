---
slug: attack-pattern/CAPEC-655
title: "CAPEC-655 — Avoid Security Tool Identification by Adding Data"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-655]
mitre_ids: [T1027.001]
related: [technique/T1027.001]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-655
updated_at: 2026-08-31
summary: "An adversary adds data to a file to increase the file size beyond what security tools are capable of handling in an attempt to mask their actions. In addition to this, adding data to a file also changes the file's hash, frustrating security tools that look for known bad files by …"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/655.html
---

# CAPEC-655: Avoid Security Tool Identification by Adding Data

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary adds data to a file to increase the file size beyond what security tools are capable of handling in an attempt to mask their actions. In addition to this, adding data to a file also changes the file's hash, frustrating security tools that look for known bad files by their hash.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**ATT&CK techniques:** [T1027.001](/wiki/p/technique/T1027.001)

## Consequences

- Accountability: Hide Activities, Bypass Protection Mechanism
- Integrity: Modify Data

## Source

- [MITRE CAPEC CAPEC-655](https://capec.mitre.org/data/definitions/655.html)
