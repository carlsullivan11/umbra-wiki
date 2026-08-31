---
slug: defense/D3-CS
title: "D3-CS — Credential Scrubbing"
page_type: defense
tags: [d3fend, defense, countermeasure, mitre]
d3fend_ids: [D3-CS]
mitre_ids: [T1505, T1505.001]
related: [technique/T1505, technique/T1505.001]
provenance: imported
import_source: mitre-d3fend
import_id: D3-CS
updated_at: 2026-08-31
summary: "The systematic removal of hard-coded credentials from source code to prevent accidental exposure and unauthorized access."
sources:
  - name: MITRE D3FEND
    url: https://d3fend.mitre.org/technique/D3-CS/
---

# D3-CS: Credential Scrubbing

**MITRE D3FEND countermeasure**

## What it does

The systematic removal of hard-coded credentials from source code to prevent accidental exposure and unauthorized access.

## Attacks this counters

The chain in this corpus runs CVE → CWE → CAPEC → ATT&CK technique, which ends at what an adversary does. This is the hop after: what stops it.

- [T1505](/wiki/p/technique/T1505)
- [T1505.001](/wiki/p/technique/T1505.001)

## Source

- [MITRE D3FEND D3-CS](https://d3fend.mitre.org/technique/D3-CS/)
