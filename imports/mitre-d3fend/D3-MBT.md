---
slug: defense/D3-MBT
title: "D3-MBT — Memory Boundary Tracking"
page_type: defense
tags: [d3fend, defense, countermeasure, mitre]
d3fend_ids: [D3-MBT]
mitre_ids: [T1055, T1055.012, T1056, T1056.004, T1068, T1203, T1210, T1211, T1212]
related: [technique/T1055, technique/T1055.012, technique/T1056, technique/T1056.004, technique/T1068, technique/T1203, technique/T1210, technique/T1211, technique/T1212]
provenance: imported
import_source: mitre-d3fend
import_id: D3-MBT
updated_at: 2026-08-31
summary: "Analyzing a call stack for return addresses which point to unexpected memory locations."
sources:
  - name: MITRE D3FEND
    url: https://d3fend.mitre.org/technique/D3-MBT/
---

# D3-MBT: Memory Boundary Tracking

**MITRE D3FEND countermeasure**

## What it does

Analyzing a call stack for return addresses which point to unexpected memory locations.

## Attacks this counters

The chain in this corpus runs CVE → CWE → CAPEC → ATT&CK technique, which ends at what an adversary does. This is the hop after: what stops it.

- [T1055](/wiki/p/technique/T1055)
- [T1055.012](/wiki/p/technique/T1055.012)
- [T1056](/wiki/p/technique/T1056)
- [T1056.004](/wiki/p/technique/T1056.004)
- [T1068](/wiki/p/technique/T1068)
- [T1203](/wiki/p/technique/T1203)
- [T1210](/wiki/p/technique/T1210)
- [T1211](/wiki/p/technique/T1211)
- [T1212](/wiki/p/technique/T1212)

## Source

- [MITRE D3FEND D3-MBT](https://d3fend.mitre.org/technique/D3-MBT/)
