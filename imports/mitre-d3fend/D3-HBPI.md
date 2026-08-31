---
slug: defense/D3-HBPI
title: "D3-HBPI — Hardware-based Process Isolation"
page_type: defense
tags: [d3fend, defense, countermeasure, mitre]
d3fend_ids: [D3-HBPI]
mitre_ids: [T1003, T1003.001, T1003.002, T1003.004, T1007, T1010, T1016, T1016.001, T1016.002, T1018, T1033, T1047, T1053, T1053.002, T1053.003, T1053.005, T1053.006, T1053.007, T1055, T1055.004, T1055.013, T1057, T1082, T1124, T1134, T1134.004, T1140, T1212, T1218, T1218.001, T1218.002, T1218.003, T1218.005, T1218.011, T1220, T1505, T1505.001, T1505.002, T1505.003, T1546, T1546.007, T1546.009, T1546.010, T1548, T1548.002, T1550, T1550.001, T1550.002, T1550.003, T1550.004, T1556, T1556.001, T1556.002, T1556.003, T1556.004, T1556.005, T1556.006, T1556.007, T1556.008, T1556.009, T1621]
related: [technique/T1003, technique/T1003.001, technique/T1003.002, technique/T1003.004, technique/T1007, technique/T1010, technique/T1016, technique/T1016.001, technique/T1016.002, technique/T1018, technique/T1033, technique/T1047, technique/T1053, technique/T1053.002, technique/T1053.003, technique/T1053.005, technique/T1053.006, technique/T1053.007, technique/T1055, technique/T1055.004, technique/T1055.013, technique/T1057, technique/T1082, technique/T1124, technique/T1134, technique/T1134.004, technique/T1140, technique/T1212, technique/T1218, technique/T1218.001, technique/T1218.002, technique/T1218.003, technique/T1218.005, technique/T1218.011, technique/T1220, technique/T1505, technique/T1505.001, technique/T1505.002, technique/T1505.003, technique/T1546, technique/T1546.007, technique/T1546.009, technique/T1546.010, technique/T1548, technique/T1548.002, technique/T1550, technique/T1550.001, technique/T1550.002, technique/T1550.003, technique/T1550.004, technique/T1556, technique/T1556.001, technique/T1556.002, technique/T1556.003, technique/T1556.004, technique/T1556.005, technique/T1556.006, technique/T1556.007, technique/T1556.008, technique/T1556.009, technique/T1621]
provenance: imported
import_source: mitre-d3fend
import_id: D3-HBPI
updated_at: 2026-08-31
summary: "Preventing one process from writing to the memory space of another process through hardware based address manager implementations."
sources:
  - name: MITRE D3FEND
    url: https://d3fend.mitre.org/technique/D3-HBPI/
---

# D3-HBPI: Hardware-based Process Isolation

**MITRE D3FEND countermeasure**

## What it does

Preventing one process from writing to the memory space of another process through hardware based address manager implementations.

## Attacks this counters

The chain in this corpus runs CVE → CWE → CAPEC → ATT&CK technique, which ends at what an adversary does. This is the hop after: what stops it.

- [T1003](/wiki/p/technique/T1003)
- [T1003.001](/wiki/p/technique/T1003.001)
- [T1003.002](/wiki/p/technique/T1003.002)
- [T1003.004](/wiki/p/technique/T1003.004)
- [T1007](/wiki/p/technique/T1007)
- [T1010](/wiki/p/technique/T1010)
- [T1016](/wiki/p/technique/T1016)
- [T1016.001](/wiki/p/technique/T1016.001)
- [T1016.002](/wiki/p/technique/T1016.002)
- [T1018](/wiki/p/technique/T1018)
- [T1033](/wiki/p/technique/T1033)
- [T1047](/wiki/p/technique/T1047)
- [T1053](/wiki/p/technique/T1053)
- [T1053.002](/wiki/p/technique/T1053.002)
- [T1053.003](/wiki/p/technique/T1053.003)
- [T1053.005](/wiki/p/technique/T1053.005)
- [T1053.006](/wiki/p/technique/T1053.006)
- [T1053.007](/wiki/p/technique/T1053.007)
- [T1055](/wiki/p/technique/T1055)
- [T1055.004](/wiki/p/technique/T1055.004)
- [T1055.013](/wiki/p/technique/T1055.013)
- [T1057](/wiki/p/technique/T1057)
- [T1082](/wiki/p/technique/T1082)
- [T1124](/wiki/p/technique/T1124)
- [T1134](/wiki/p/technique/T1134)
- [T1134.004](/wiki/p/technique/T1134.004)
- [T1140](/wiki/p/technique/T1140)
- [T1212](/wiki/p/technique/T1212)
- [T1218](/wiki/p/technique/T1218)
- [T1218.001](/wiki/p/technique/T1218.001)
- [T1218.002](/wiki/p/technique/T1218.002)
- [T1218.003](/wiki/p/technique/T1218.003)
- [T1218.005](/wiki/p/technique/T1218.005)
- [T1218.011](/wiki/p/technique/T1218.011)
- [T1220](/wiki/p/technique/T1220)
- [T1505](/wiki/p/technique/T1505)
- [T1505.001](/wiki/p/technique/T1505.001)
- [T1505.002](/wiki/p/technique/T1505.002)
- [T1505.003](/wiki/p/technique/T1505.003)
- [T1546](/wiki/p/technique/T1546)
- [T1546.007](/wiki/p/technique/T1546.007)
- [T1546.009](/wiki/p/technique/T1546.009)
- [T1546.010](/wiki/p/technique/T1546.010)
- [T1548](/wiki/p/technique/T1548)
- [T1548.002](/wiki/p/technique/T1548.002)
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

- [MITRE D3FEND D3-HBPI](https://d3fend.mitre.org/technique/D3-HBPI/)
