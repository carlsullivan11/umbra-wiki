---
slug: defense/D3-SFCV
title: "D3-SFCV — Stack Frame Canary Validation"
page_type: defense
tags: [d3fend, defense, countermeasure, mitre]
d3fend_ids: [D3-SFCV]
mitre_ids: [T1068, T1203, T1210, T1211, T1212]
related: [technique/T1068, technique/T1203, technique/T1210, technique/T1211, technique/T1212]
provenance: imported
import_source: mitre-d3fend
import_id: D3-SFCV
updated_at: 2026-08-31
summary: "Comparing a value stored in a stack frame with a known good value in order to prevent or detect a memory segment overwrite."
sources:
  - name: MITRE D3FEND
    url: https://d3fend.mitre.org/technique/D3-SFCV/
---

# D3-SFCV: Stack Frame Canary Validation

**MITRE D3FEND countermeasure**

## What it does

Comparing a value stored in a stack frame with a known good value in order to prevent or detect a memory segment overwrite.

## Attacks this counters

The chain in this corpus runs CVE → CWE → CAPEC → ATT&CK technique, which ends at what an adversary does. This is the hop after: what stops it.

- [T1068](/wiki/p/technique/T1068)
- [T1203](/wiki/p/technique/T1203)
- [T1210](/wiki/p/technique/T1210)
- [T1211](/wiki/p/technique/T1211)
- [T1212](/wiki/p/technique/T1212)

## Source

- [MITRE D3FEND D3-SFCV](https://d3fend.mitre.org/technique/D3-SFCV/)
