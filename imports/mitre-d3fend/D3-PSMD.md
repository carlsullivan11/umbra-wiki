---
slug: defense/D3-PSMD
title: "D3-PSMD — Process Self-Modification Detection"
page_type: defense
tags: [d3fend, defense, countermeasure, mitre]
d3fend_ids: [D3-PSMD]
mitre_ids: [T1003, T1003.001, T1003.002, T1003.004, T1033, T1053, T1053.002, T1053.003, T1053.005, T1053.006, T1053.007, T1212, T1505, T1505.002, T1505.003, T1546, T1546.007, T1550, T1550.001, T1550.002, T1550.003, T1550.004, T1556, T1556.001, T1556.002, T1556.003, T1556.004, T1556.005, T1556.006, T1556.007, T1556.008, T1556.009, T1621]
related: [technique/T1003, technique/T1003.001, technique/T1003.002, technique/T1003.004, technique/T1033, technique/T1053, technique/T1053.002, technique/T1053.003, technique/T1053.005, technique/T1053.006, technique/T1053.007, technique/T1212, technique/T1505, technique/T1505.002, technique/T1505.003, technique/T1546, technique/T1546.007, technique/T1550, technique/T1550.001, technique/T1550.002, technique/T1550.003, technique/T1550.004, technique/T1556, technique/T1556.001, technique/T1556.002, technique/T1556.003, technique/T1556.004, technique/T1556.005, technique/T1556.006, technique/T1556.007, technique/T1556.008, technique/T1556.009, technique/T1621]
provenance: imported
import_source: mitre-d3fend
import_id: D3-PSMD
updated_at: 2026-08-31
summary: "Detects processes that modify, change, or replace their own code at runtime."
sources:
  - name: MITRE D3FEND
    url: https://d3fend.mitre.org/technique/D3-PSMD/
---

# D3-PSMD: Process Self-Modification Detection

**MITRE D3FEND countermeasure**

## What it does

Detects processes that modify, change, or replace their own code at runtime.

## Attacks this counters

The chain in this corpus runs CVE → CWE → CAPEC → ATT&CK technique, which ends at what an adversary does. This is the hop after: what stops it.

- [T1003](/wiki/p/technique/T1003)
- [T1003.001](/wiki/p/technique/T1003.001)
- [T1003.002](/wiki/p/technique/T1003.002)
- [T1003.004](/wiki/p/technique/T1003.004)
- [T1033](/wiki/p/technique/T1033)
- [T1053](/wiki/p/technique/T1053)
- [T1053.002](/wiki/p/technique/T1053.002)
- [T1053.003](/wiki/p/technique/T1053.003)
- [T1053.005](/wiki/p/technique/T1053.005)
- [T1053.006](/wiki/p/technique/T1053.006)
- [T1053.007](/wiki/p/technique/T1053.007)
- [T1212](/wiki/p/technique/T1212)
- [T1505](/wiki/p/technique/T1505)
- [T1505.002](/wiki/p/technique/T1505.002)
- [T1505.003](/wiki/p/technique/T1505.003)
- [T1546](/wiki/p/technique/T1546)
- [T1546.007](/wiki/p/technique/T1546.007)
- [T1550](/wiki/p/technique/T1550)
- [T1550.001](/wiki/p/technique/T1550.001)
- [T1550.002](/wiki/p/technique/T1550.002)
- [T1550.003](/wiki/p/technique/T1550.003)
- [T1550.004](/wiki/p/technique/T1550.004)
- [T1556](/wiki/p/technique/T1556)
- [T1556.001](/wiki/p/technique/T1556.001)
- [T1556.002](/wiki/p/technique/T1556.002)
- [T1556.003](/wiki/p/technique/T1556.003)
- [T1556.004](/wiki/p/technique/T1556.004)
- [T1556.005](/wiki/p/technique/T1556.005)
- [T1556.006](/wiki/p/technique/T1556.006)
- [T1556.007](/wiki/p/technique/T1556.007)
- [T1556.008](/wiki/p/technique/T1556.008)
- [T1556.009](/wiki/p/technique/T1556.009)
- [T1621](/wiki/p/technique/T1621)

## Source

- [MITRE D3FEND D3-PSMD](https://d3fend.mitre.org/technique/D3-PSMD/)
