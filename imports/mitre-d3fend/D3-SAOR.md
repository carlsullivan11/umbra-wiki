---
slug: defense/D3-SAOR
title: "D3-SAOR — Segment Address Offset Randomization"
page_type: defense
tags: [d3fend, defense, countermeasure, mitre]
d3fend_ids: [D3-SAOR]
mitre_ids: [T1033, T1055, T1055.012, T1056, T1056.004, T1068, T1189, T1190, T1203, T1210, T1211, T1212, T1218, T1218.013, T1620]
related: [technique/T1033, technique/T1055, technique/T1055.012, technique/T1056, technique/T1056.004, technique/T1068, technique/T1189, technique/T1190, technique/T1203, technique/T1210, technique/T1211, technique/T1212, technique/T1218, technique/T1218.013, technique/T1620]
provenance: imported
import_source: mitre-d3fend
import_id: D3-SAOR
updated_at: 2026-08-31
summary: "Randomizing the base (start) address of one or more segments of memory during the initialization of a process."
sources:
  - name: MITRE D3FEND
    url: https://d3fend.mitre.org/technique/D3-SAOR/
---

# D3-SAOR: Segment Address Offset Randomization

**MITRE D3FEND countermeasure**

## What it does

Randomizing the base (start) address of one or more segments of memory during the initialization of a process.

## Attacks this counters

The chain in this corpus runs CVE → CWE → CAPEC → ATT&CK technique, which ends at what an adversary does. This is the hop after: what stops it.

- [T1033](/wiki/p/technique/T1033)
- [T1055](/wiki/p/technique/T1055)
- [T1055.012](/wiki/p/technique/T1055.012)
- [T1056](/wiki/p/technique/T1056)
- [T1056.004](/wiki/p/technique/T1056.004)
- [T1068](/wiki/p/technique/T1068)
- [T1189](/wiki/p/technique/T1189)
- [T1190](/wiki/p/technique/T1190)
- [T1203](/wiki/p/technique/T1203)
- [T1210](/wiki/p/technique/T1210)
- [T1211](/wiki/p/technique/T1211)
- [T1212](/wiki/p/technique/T1212)
- [T1218](/wiki/p/technique/T1218)
- [T1218.013](/wiki/p/technique/T1218.013)
- [T1620](/wiki/p/technique/T1620)

## Source

- [MITRE D3FEND D3-SAOR](https://d3fend.mitre.org/technique/D3-SAOR/)
