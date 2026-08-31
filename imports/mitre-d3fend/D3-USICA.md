---
slug: defense/D3-USICA
title: "D3-USICA — User Session Init Config Analysis"
page_type: defense
tags: [d3fend, defense, countermeasure, mitre]
d3fend_ids: [D3-USICA]
mitre_ids: [T1546, T1546.004, T1564, T1564.002]
related: [technique/T1546, technique/T1546.004, technique/T1564, technique/T1564.002]
provenance: imported
import_source: mitre-d3fend
import_id: D3-USICA
updated_at: 2026-08-31
summary: "Analyzing modifications to user session config files such as .bashrc or .bash_profile."
sources:
  - name: MITRE D3FEND
    url: https://d3fend.mitre.org/technique/D3-USICA/
---

# D3-USICA: User Session Init Config Analysis

**MITRE D3FEND countermeasure**

## What it does

Analyzing modifications to user session config files such as .bashrc or .bash_profile.

## Attacks this counters

The chain in this corpus runs CVE → CWE → CAPEC → ATT&CK technique, which ends at what an adversary does. This is the hop after: what stops it.

- [T1546](/wiki/p/technique/T1546)
- [T1546.004](/wiki/p/technique/T1546.004)
- [T1564](/wiki/p/technique/T1564)
- [T1564.002](/wiki/p/technique/T1564.002)

## Source

- [MITRE D3FEND D3-USICA](https://d3fend.mitre.org/technique/D3-USICA/)
