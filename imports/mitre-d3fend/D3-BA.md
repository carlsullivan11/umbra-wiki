---
slug: defense/D3-BA
title: "D3-BA — Bootloader Authentication"
page_type: defense
tags: [d3fend, defense, countermeasure, mitre]
d3fend_ids: [D3-BA]
mitre_ids: [T1542, T1542.003]
related: [technique/T1542, technique/T1542.003]
provenance: imported
import_source: mitre-d3fend
import_id: D3-BA
updated_at: 2026-08-31
summary: "Cryptographically authenticating the bootloader software before system boot."
sources:
  - name: MITRE D3FEND
    url: https://d3fend.mitre.org/technique/D3-BA/
---

# D3-BA: Bootloader Authentication

**MITRE D3FEND countermeasure**

## What it does

Cryptographically authenticating the bootloader software before system boot.

## Attacks this counters

The chain in this corpus runs CVE → CWE → CAPEC → ATT&CK technique, which ends at what an adversary does. This is the hop after: what stops it.

- [T1542](/wiki/p/technique/T1542)
- [T1542.003](/wiki/p/technique/T1542.003)

## Source

- [MITRE D3FEND D3-BA](https://d3fend.mitre.org/technique/D3-BA/)
