---
slug: defense/D3-RRID
title: "D3-RRID — Reverse Resolution IP Denylisting"
page_type: defense
tags: [d3fend, defense, countermeasure, mitre]
d3fend_ids: [D3-RRID]
mitre_ids: [T1071, T1071.004, T1568, T1568.001, T1568.002, T1568.003]
related: [technique/T1071, technique/T1071.004, technique/T1568, technique/T1568.001, technique/T1568.002, technique/T1568.003]
provenance: imported
import_source: mitre-d3fend
import_id: D3-RRID
updated_at: 2026-08-31
summary: "Blocking a reverse lookup based on the query's IP address value."
sources:
  - name: MITRE D3FEND
    url: https://d3fend.mitre.org/technique/D3-RRID/
---

# D3-RRID: Reverse Resolution IP Denylisting

**MITRE D3FEND countermeasure**

## What it does

Blocking a reverse lookup based on the query's IP address value.

## Attacks this counters

The chain in this corpus runs CVE → CWE → CAPEC → ATT&CK technique, which ends at what an adversary does. This is the hop after: what stops it.

- [T1071](/wiki/p/technique/T1071)
- [T1071.004](/wiki/p/technique/T1071.004)
- [T1568](/wiki/p/technique/T1568)
- [T1568.001](/wiki/p/technique/T1568.001)
- [T1568.002](/wiki/p/technique/T1568.002)
- [T1568.003](/wiki/p/technique/T1568.003)

## Source

- [MITRE D3FEND D3-RRID](https://d3fend.mitre.org/technique/D3-RRID/)
