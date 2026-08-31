---
slug: defense/D3-UGLPA
title: "D3-UGLPA — User Geolocation Logon Pattern Analysis"
page_type: defense
tags: [d3fend, defense, countermeasure, mitre]
d3fend_ids: [D3-UGLPA]
mitre_ids: [T1001, T1001.001, T1001.002, T1001.003, T1003, T1003.006, T1008, T1011, T1011.001, T1018, T1020, T1020.001, T1021, T1021.001, T1021.002, T1021.003, T1021.004, T1021.005, T1021.006, T1021.007, T1021.008, T1029, T1030, T1041, T1047, T1048, T1048.001, T1048.002, T1048.003, T1071, T1071.001, T1071.002, T1071.003, T1071.004, T1071.005, T1090, T1090.001, T1090.002, T1090.003, T1090.004, T1095, T1098, T1098.001, T1102, T1102.001, T1102.002, T1102.003, T1104, T1105, T1110, T1110.003, T1110.004, T1132, T1132.001, T1132.002, T1185, T1189, T1190, T1197, T1199, T1204, T1204.001, T1205, T1205.001, T1205.002, T1207, T1210, T1218, T1218.003, T1219, T1219.001, T1219.002, T1219.003, T1498, T1498.001, T1498.002, T1499, T1499.002, T1542, T1542.005, T1546, T1546.003, T1546.008, T1550, T1550.001, T1550.004, T1557, T1557.001, T1557.002, T1557.003, T1557.004, T1558, T1558.003, T1563, T1563.001, T1563.002, T1565, T1565.002, T1566, T1566.001, T1566.002, T1567, T1567.001, T1567.002, T1567.003, T1567.004, T1568, T1568.001, T1568.002, T1568.003, T1570, T1571, T1572, T1573, T1573.001, T1573.002]
related: [technique/T1001, technique/T1001.001, technique/T1001.002, technique/T1001.003, technique/T1003, technique/T1003.006, technique/T1008, technique/T1011, technique/T1011.001, technique/T1018, technique/T1020, technique/T1020.001, technique/T1021, technique/T1021.001, technique/T1021.002, technique/T1021.003, technique/T1021.004, technique/T1021.005, technique/T1021.006, technique/T1021.007, technique/T1021.008, technique/T1029, technique/T1030, technique/T1041, technique/T1047, technique/T1048, technique/T1048.001, technique/T1048.002, technique/T1048.003, technique/T1071, technique/T1071.001, technique/T1071.002, technique/T1071.003, technique/T1071.004, technique/T1071.005, technique/T1090, technique/T1090.001, technique/T1090.002, technique/T1090.003, technique/T1090.004, technique/T1095, technique/T1098, technique/T1098.001, technique/T1102, technique/T1102.001, technique/T1102.002, technique/T1102.003, technique/T1104, technique/T1105, technique/T1110, technique/T1110.003, technique/T1110.004, technique/T1132, technique/T1132.001, technique/T1132.002, technique/T1185, technique/T1189, technique/T1190, technique/T1197, technique/T1199, technique/T1204, technique/T1204.001, technique/T1205, technique/T1205.001, technique/T1205.002, technique/T1207, technique/T1210, technique/T1218, technique/T1218.003, technique/T1219, technique/T1219.001, technique/T1219.002, technique/T1219.003, technique/T1498, technique/T1498.001, technique/T1498.002, technique/T1499, technique/T1499.002, technique/T1542, technique/T1542.005, technique/T1546, technique/T1546.003, technique/T1546.008, technique/T1550, technique/T1550.001, technique/T1550.004, technique/T1557, technique/T1557.001, technique/T1557.002, technique/T1557.003, technique/T1557.004, technique/T1558, technique/T1558.003, technique/T1563, technique/T1563.001, technique/T1563.002, technique/T1565, technique/T1565.002, technique/T1566, technique/T1566.001, technique/T1566.002, technique/T1567, technique/T1567.001, technique/T1567.002, technique/T1567.003, technique/T1567.004, technique/T1568, technique/T1568.001, technique/T1568.002, technique/T1568.003, technique/T1570, technique/T1571, technique/T1572, technique/T1573, technique/T1573.001, technique/T1573.002]
provenance: imported
import_source: mitre-d3fend
import_id: D3-UGLPA
updated_at: 2026-08-31
summary: "Monitoring geolocation data of user logon attempts and comparing it to a baseline user behavior profile to identify anomalies in logon location."
sources:
  - name: MITRE D3FEND
    url: https://d3fend.mitre.org/technique/D3-UGLPA/
---

# D3-UGLPA: User Geolocation Logon Pattern Analysis

**MITRE D3FEND countermeasure**

## What it does

Monitoring geolocation data of user logon attempts and comparing it to a baseline user behavior profile to identify anomalies in logon location.

## Attacks this counters

The chain in this corpus runs CVE → CWE → CAPEC → ATT&CK technique, which ends at what an adversary does. This is the hop after: what stops it.

- [T1001](/wiki/p/technique/T1001)
- [T1001.001](/wiki/p/technique/T1001.001)
- [T1001.002](/wiki/p/technique/T1001.002)
- [T1001.003](/wiki/p/technique/T1001.003)
- [T1003](/wiki/p/technique/T1003)
- [T1003.006](/wiki/p/technique/T1003.006)
- [T1008](/wiki/p/technique/T1008)
- [T1011](/wiki/p/technique/T1011)
- [T1011.001](/wiki/p/technique/T1011.001)
- [T1018](/wiki/p/technique/T1018)
- [T1020](/wiki/p/technique/T1020)
- [T1020.001](/wiki/p/technique/T1020.001)
- [T1021](/wiki/p/technique/T1021)
- [T1021.001](/wiki/p/technique/T1021.001)
- [T1021.002](/wiki/p/technique/T1021.002)
- [T1021.003](/wiki/p/technique/T1021.003)
- [T1021.004](/wiki/p/technique/T1021.004)
- [T1021.005](/wiki/p/technique/T1021.005)
- [T1021.006](/wiki/p/technique/T1021.006)
- [T1021.007](/wiki/p/technique/T1021.007)
- [T1021.008](/wiki/p/technique/T1021.008)
- [T1029](/wiki/p/technique/T1029)
- [T1030](/wiki/p/technique/T1030)
- [T1041](/wiki/p/technique/T1041)
- [T1047](/wiki/p/technique/T1047)
- [T1048](/wiki/p/technique/T1048)
- [T1048.001](/wiki/p/technique/T1048.001)
- [T1048.002](/wiki/p/technique/T1048.002)
- [T1048.003](/wiki/p/technique/T1048.003)
- [T1071](/wiki/p/technique/T1071)
- [T1071.001](/wiki/p/technique/T1071.001)
- [T1071.002](/wiki/p/technique/T1071.002)
- [T1071.003](/wiki/p/technique/T1071.003)
- [T1071.004](/wiki/p/technique/T1071.004)
- [T1071.005](/wiki/p/technique/T1071.005)
- [T1090](/wiki/p/technique/T1090)
- [T1090.001](/wiki/p/technique/T1090.001)
- [T1090.002](/wiki/p/technique/T1090.002)
- [T1090.003](/wiki/p/technique/T1090.003)
- [T1090.004](/wiki/p/technique/T1090.004)
- [T1095](/wiki/p/technique/T1095)
- [T1098](/wiki/p/technique/T1098)
- [T1098.001](/wiki/p/technique/T1098.001)
- [T1102](/wiki/p/technique/T1102)
- [T1102.001](/wiki/p/technique/T1102.001)
- [T1102.002](/wiki/p/technique/T1102.002)
- [T1102.003](/wiki/p/technique/T1102.003)
- [T1104](/wiki/p/technique/T1104)
- [T1105](/wiki/p/technique/T1105)
- [T1110](/wiki/p/technique/T1110)
- [T1110.003](/wiki/p/technique/T1110.003)
- [T1110.004](/wiki/p/technique/T1110.004)
- [T1132](/wiki/p/technique/T1132)
- [T1132.001](/wiki/p/technique/T1132.001)
- [T1132.002](/wiki/p/technique/T1132.002)
- [T1185](/wiki/p/technique/T1185)
- [T1189](/wiki/p/technique/T1189)
- [T1190](/wiki/p/technique/T1190)
- [T1197](/wiki/p/technique/T1197)
- [T1199](/wiki/p/technique/T1199)
- [T1204](/wiki/p/technique/T1204)
- [T1204.001](/wiki/p/technique/T1204.001)
- [T1205](/wiki/p/technique/T1205)
- [T1205.001](/wiki/p/technique/T1205.001)
- [T1205.002](/wiki/p/technique/T1205.002)
- [T1207](/wiki/p/technique/T1207)
- [T1210](/wiki/p/technique/T1210)
- [T1218](/wiki/p/technique/T1218)
- [T1218.003](/wiki/p/technique/T1218.003)
- [T1219](/wiki/p/technique/T1219)
- [T1219.001](/wiki/p/technique/T1219.001)
- [T1219.002](/wiki/p/technique/T1219.002)
- [T1219.003](/wiki/p/technique/T1219.003)
- [T1498](/wiki/p/technique/T1498)
- [T1498.001](/wiki/p/technique/T1498.001)
- [T1498.002](/wiki/p/technique/T1498.002)
- [T1499](/wiki/p/technique/T1499)
- [T1499.002](/wiki/p/technique/T1499.002)
- [T1542](/wiki/p/technique/T1542)
- [T1542.005](/wiki/p/technique/T1542.005)
- [T1546](/wiki/p/technique/T1546)
- [T1546.003](/wiki/p/technique/T1546.003)
- [T1546.008](/wiki/p/technique/T1546.008)
- [T1550](/wiki/p/technique/T1550)
- [T1550.001](/wiki/p/technique/T1550.001)
- [T1550.004](/wiki/p/technique/T1550.004)
- [T1557](/wiki/p/technique/T1557)
- [T1557.001](/wiki/p/technique/T1557.001)
- [T1557.002](/wiki/p/technique/T1557.002)
- [T1557.003](/wiki/p/technique/T1557.003)
- [T1557.004](/wiki/p/technique/T1557.004)
- [T1558](/wiki/p/technique/T1558)
- [T1558.003](/wiki/p/technique/T1558.003)
- [T1563](/wiki/p/technique/T1563)
- [T1563.001](/wiki/p/technique/T1563.001)
- [T1563.002](/wiki/p/technique/T1563.002)
- [T1565](/wiki/p/technique/T1565)
- [T1565.002](/wiki/p/technique/T1565.002)
- [T1566](/wiki/p/technique/T1566)
- [T1566.001](/wiki/p/technique/T1566.001)
- [T1566.002](/wiki/p/technique/T1566.002)
- [T1567](/wiki/p/technique/T1567)
- [T1567.001](/wiki/p/technique/T1567.001)
- [T1567.002](/wiki/p/technique/T1567.002)
- [T1567.003](/wiki/p/technique/T1567.003)
- [T1567.004](/wiki/p/technique/T1567.004)
- [T1568](/wiki/p/technique/T1568)
- [T1568.001](/wiki/p/technique/T1568.001)
- [T1568.002](/wiki/p/technique/T1568.002)
- [T1568.003](/wiki/p/technique/T1568.003)
- [T1570](/wiki/p/technique/T1570)
- [T1571](/wiki/p/technique/T1571)
- [T1572](/wiki/p/technique/T1572)
- [T1573](/wiki/p/technique/T1573)
- [T1573.001](/wiki/p/technique/T1573.001)
- [T1573.002](/wiki/p/technique/T1573.002)

## Source

- [MITRE D3FEND D3-UGLPA](https://d3fend.mitre.org/technique/D3-UGLPA/)
