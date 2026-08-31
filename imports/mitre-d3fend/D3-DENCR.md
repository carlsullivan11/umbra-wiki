---
slug: defense/D3-DENCR
title: "D3-DENCR — Disk Encryption"
page_type: defense
tags: [d3fend, defense, countermeasure, mitre]
d3fend_ids: [D3-DENCR]
mitre_ids: [T1564, T1564.005, T1619]
related: [technique/T1564, technique/T1564.005, technique/T1619]
provenance: imported
import_source: mitre-d3fend
import_id: D3-DENCR
updated_at: 2026-08-31
summary: "Encrypting a hard disk partition to prevent cleartext access to a file system."
sources:
  - name: MITRE D3FEND
    url: https://d3fend.mitre.org/technique/D3-DENCR/
---

# D3-DENCR: Disk Encryption

**MITRE D3FEND countermeasure**

## What it does

Encrypting a hard disk partition to prevent cleartext access to a file system.

## Attacks this counters

The chain in this corpus runs CVE → CWE → CAPEC → ATT&CK technique, which ends at what an adversary does. This is the hop after: what stops it.

- [T1564](/wiki/p/technique/T1564)
- [T1564.005](/wiki/p/technique/T1564.005)
- [T1619](/wiki/p/technique/T1619)

## Source

- [MITRE D3FEND D3-DENCR](https://d3fend.mitre.org/technique/D3-DENCR/)
