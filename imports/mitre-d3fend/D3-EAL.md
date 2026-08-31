---
slug: defense/D3-EAL
title: "D3-EAL — Executable Allowlisting"
page_type: defense
tags: [d3fend, defense, countermeasure, mitre]
d3fend_ids: [D3-EAL]
mitre_ids: [T1007, T1010, T1016, T1016.001, T1016.002, T1018, T1027, T1027.001, T1027.002, T1027.004, T1033, T1036, T1036.001, T1036.003, T1037, T1037.001, T1037.002, T1037.003, T1037.004, T1047, T1053, T1053.002, T1053.003, T1053.005, T1053.006, T1053.007, T1055, T1055.003, T1055.004, T1055.013, T1057, T1059, T1059.001, T1059.002, T1059.003, T1059.004, T1059.005, T1059.006, T1059.007, T1059.008, T1059.009, T1059.010, T1059.011, T1059.012, T1059.013, T1082, T1124, T1134, T1134.004, T1137, T1137.001, T1140, T1204, T1204.002, T1218, T1218.001, T1218.002, T1218.003, T1218.005, T1218.011, T1220, T1505, T1505.001, T1505.003, T1546, T1546.002, T1546.005, T1546.006, T1546.008, T1546.009, T1546.010, T1546.013, T1546.015, T1547, T1547.001, T1547.009, T1548, T1548.002, T1565, T1565.003, T1574, T1574.007, T1574.008, T1574.009]
related: [technique/T1007, technique/T1010, technique/T1016, technique/T1016.001, technique/T1016.002, technique/T1018, technique/T1027, technique/T1027.001, technique/T1027.002, technique/T1027.004, technique/T1033, technique/T1036, technique/T1036.001, technique/T1036.003, technique/T1037, technique/T1037.001, technique/T1037.002, technique/T1037.003, technique/T1037.004, technique/T1047, technique/T1053, technique/T1053.002, technique/T1053.003, technique/T1053.005, technique/T1053.006, technique/T1053.007, technique/T1055, technique/T1055.003, technique/T1055.004, technique/T1055.013, technique/T1057, technique/T1059, technique/T1059.001, technique/T1059.002, technique/T1059.003, technique/T1059.004, technique/T1059.005, technique/T1059.006, technique/T1059.007, technique/T1059.008, technique/T1059.009, technique/T1059.010, technique/T1059.011, technique/T1059.012, technique/T1059.013, technique/T1082, technique/T1124, technique/T1134, technique/T1134.004, technique/T1137, technique/T1137.001, technique/T1140, technique/T1204, technique/T1204.002, technique/T1218, technique/T1218.001, technique/T1218.002, technique/T1218.003, technique/T1218.005, technique/T1218.011, technique/T1220, technique/T1505, technique/T1505.001, technique/T1505.003, technique/T1546, technique/T1546.002, technique/T1546.005, technique/T1546.006, technique/T1546.008, technique/T1546.009, technique/T1546.010, technique/T1546.013, technique/T1546.015, technique/T1547, technique/T1547.001, technique/T1547.009, technique/T1548, technique/T1548.002, technique/T1565, technique/T1565.003, technique/T1574, technique/T1574.007, technique/T1574.008, technique/T1574.009]
provenance: imported
import_source: mitre-d3fend
import_id: D3-EAL
updated_at: 2026-08-31
summary: "Using a digital signature to authenticate a file before opening."
sources:
  - name: MITRE D3FEND
    url: https://d3fend.mitre.org/technique/D3-EAL/
---

# D3-EAL: Executable Allowlisting

**MITRE D3FEND countermeasure**

## What it does

Using a digital signature to authenticate a file before opening.

## Attacks this counters

The chain in this corpus runs CVE → CWE → CAPEC → ATT&CK technique, which ends at what an adversary does. This is the hop after: what stops it.

- [T1007](/wiki/p/technique/T1007)
- [T1010](/wiki/p/technique/T1010)
- [T1016](/wiki/p/technique/T1016)
- [T1016.001](/wiki/p/technique/T1016.001)
- [T1016.002](/wiki/p/technique/T1016.002)
- [T1018](/wiki/p/technique/T1018)
- [T1027](/wiki/p/technique/T1027)
- [T1027.001](/wiki/p/technique/T1027.001)
- [T1027.002](/wiki/p/technique/T1027.002)
- [T1027.004](/wiki/p/technique/T1027.004)
- [T1033](/wiki/p/technique/T1033)
- [T1036](/wiki/p/technique/T1036)
- [T1036.001](/wiki/p/technique/T1036.001)
- [T1036.003](/wiki/p/technique/T1036.003)
- [T1037](/wiki/p/technique/T1037)
- [T1037.001](/wiki/p/technique/T1037.001)
- [T1037.002](/wiki/p/technique/T1037.002)
- [T1037.003](/wiki/p/technique/T1037.003)
- [T1037.004](/wiki/p/technique/T1037.004)
- [T1047](/wiki/p/technique/T1047)
- [T1053](/wiki/p/technique/T1053)
- [T1053.002](/wiki/p/technique/T1053.002)
- [T1053.003](/wiki/p/technique/T1053.003)
- [T1053.005](/wiki/p/technique/T1053.005)
- [T1053.006](/wiki/p/technique/T1053.006)
- [T1053.007](/wiki/p/technique/T1053.007)
- [T1055](/wiki/p/technique/T1055)
- [T1055.003](/wiki/p/technique/T1055.003)
- [T1055.004](/wiki/p/technique/T1055.004)
- [T1055.013](/wiki/p/technique/T1055.013)
- [T1057](/wiki/p/technique/T1057)
- [T1059](/wiki/p/technique/T1059)
- [T1059.001](/wiki/p/technique/T1059.001)
- [T1059.002](/wiki/p/technique/T1059.002)
- [T1059.003](/wiki/p/technique/T1059.003)
- [T1059.004](/wiki/p/technique/T1059.004)
- [T1059.005](/wiki/p/technique/T1059.005)
- [T1059.006](/wiki/p/technique/T1059.006)
- [T1059.007](/wiki/p/technique/T1059.007)
- [T1059.008](/wiki/p/technique/T1059.008)
- [T1059.009](/wiki/p/technique/T1059.009)
- [T1059.010](/wiki/p/technique/T1059.010)
- [T1059.011](/wiki/p/technique/T1059.011)
- [T1059.012](/wiki/p/technique/T1059.012)
- [T1059.013](/wiki/p/technique/T1059.013)
- [T1082](/wiki/p/technique/T1082)
- [T1124](/wiki/p/technique/T1124)
- [T1134](/wiki/p/technique/T1134)
- [T1134.004](/wiki/p/technique/T1134.004)
- [T1137](/wiki/p/technique/T1137)
- [T1137.001](/wiki/p/technique/T1137.001)
- [T1140](/wiki/p/technique/T1140)
- [T1204](/wiki/p/technique/T1204)
- [T1204.002](/wiki/p/technique/T1204.002)
- [T1218](/wiki/p/technique/T1218)
- [T1218.001](/wiki/p/technique/T1218.001)
- [T1218.002](/wiki/p/technique/T1218.002)
- [T1218.003](/wiki/p/technique/T1218.003)
- [T1218.005](/wiki/p/technique/T1218.005)
- [T1218.011](/wiki/p/technique/T1218.011)
- [T1220](/wiki/p/technique/T1220)
- [T1505](/wiki/p/technique/T1505)
- [T1505.001](/wiki/p/technique/T1505.001)
- [T1505.003](/wiki/p/technique/T1505.003)
- [T1546](/wiki/p/technique/T1546)
- [T1546.002](/wiki/p/technique/T1546.002)
- [T1546.005](/wiki/p/technique/T1546.005)
- [T1546.006](/wiki/p/technique/T1546.006)
- [T1546.008](/wiki/p/technique/T1546.008)
- [T1546.009](/wiki/p/technique/T1546.009)
- [T1546.010](/wiki/p/technique/T1546.010)
- [T1546.013](/wiki/p/technique/T1546.013)
- [T1546.015](/wiki/p/technique/T1546.015)
- [T1547](/wiki/p/technique/T1547)
- [T1547.001](/wiki/p/technique/T1547.001)
- [T1547.009](/wiki/p/technique/T1547.009)
- [T1548](/wiki/p/technique/T1548)
- [T1548.002](/wiki/p/technique/T1548.002)
- [T1565](/wiki/p/technique/T1565)
- [T1565.003](/wiki/p/technique/T1565.003)
- [T1574](/wiki/p/technique/T1574)
- [T1574.007](/wiki/p/technique/T1574.007)
- [T1574.008](/wiki/p/technique/T1574.008)
- [T1574.009](/wiki/p/technique/T1574.009)

## Source

- [MITRE D3FEND D3-EAL](https://d3fend.mitre.org/technique/D3-EAL/)
