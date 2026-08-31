---
slug: defense/D3-SSC
title: "D3-SSC — Shadow Stack Comparisons"
page_type: defense
tags: [d3fend, defense, countermeasure, mitre]
d3fend_ids: [D3-SSC]
mitre_ids: [T1068, T1203, T1210, T1211, T1212]
related: [technique/T1068, technique/T1203, technique/T1210, technique/T1211, technique/T1212]
provenance: imported
import_source: mitre-d3fend
import_id: D3-SSC
updated_at: 2026-08-31
summary: "Comparing a call stack in system memory with a shadow call stack maintained by the processor to determine unauthorized shellcode activity."
sources:
  - name: MITRE D3FEND
    url: https://d3fend.mitre.org/technique/D3-SSC/
---

# D3-SSC: Shadow Stack Comparisons

**MITRE D3FEND countermeasure**

## What it does

Comparing a call stack in system memory with a shadow call stack maintained by the processor to determine unauthorized shellcode activity.

## Attacks this counters

The chain in this corpus runs CVE → CWE → CAPEC → ATT&CK technique, which ends at what an adversary does. This is the hop after: what stops it.

- [T1068](/wiki/p/technique/T1068)
- [T1203](/wiki/p/technique/T1203)
- [T1210](/wiki/p/technique/T1210)
- [T1211](/wiki/p/technique/T1211)
- [T1212](/wiki/p/technique/T1212)

## Source

- [MITRE D3FEND D3-SSC](https://d3fend.mitre.org/technique/D3-SSC/)
