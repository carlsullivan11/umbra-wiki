---
slug: defense/D3-TL
title: "D3-TL — Trusted Library"
page_type: defense
tags: [d3fend, defense, countermeasure, mitre]
d3fend_ids: [D3-TL]
mitre_ids: [T1505, T1505.001]
related: [technique/T1505, technique/T1505.001]
provenance: imported
import_source: mitre-d3fend
import_id: D3-TL
updated_at: 2026-08-31
summary: "A trusted library is a collection of pre-verified and secure code modules or components that are used within software applications to perform specific functions. These libraries are considered reliable and have been vetted for security vulnerabilities, ensurin…"
sources:
  - name: MITRE D3FEND
    url: https://d3fend.mitre.org/technique/D3-TL/
---

# D3-TL: Trusted Library

**MITRE D3FEND countermeasure**

## What it does

A trusted library is a collection of pre-verified and secure code modules or components that are used within software applications to perform specific functions. These libraries are considered reliable and have been vetted for security vulnerabilities, ensuring they do not introduce risks into the application.

## Attacks this counters

The chain in this corpus runs CVE → CWE → CAPEC → ATT&CK technique, which ends at what an adversary does. This is the hop after: what stops it.

- [T1505](/wiki/p/technique/T1505)
- [T1505.001](/wiki/p/technique/T1505.001)

## Source

- [MITRE D3FEND D3-TL](https://d3fend.mitre.org/technique/D3-TL/)
