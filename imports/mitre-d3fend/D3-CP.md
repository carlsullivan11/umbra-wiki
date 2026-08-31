---
slug: defense/D3-CP
title: "D3-CP — Certificate Pinning"
page_type: defense
tags: [d3fend, defense, countermeasure, mitre]
d3fend_ids: [D3-CP]
mitre_ids: [T1649]
related: [technique/T1649]
provenance: imported
import_source: mitre-d3fend
import_id: D3-CP
updated_at: 2026-08-31
summary: "Persisting either a server's X.509 certificate or their public key and comparing that to server's presented identity to allow for greater client confidence in the remote server's identity for SSL connections."
sources:
  - name: MITRE D3FEND
    url: https://d3fend.mitre.org/technique/D3-CP/
---

# D3-CP: Certificate Pinning

**MITRE D3FEND countermeasure**

## What it does

Persisting either a server's X.509 certificate or their public key and comparing that to server's presented identity to allow for greater client confidence in the remote server's identity for SSL connections.

## Attacks this counters

The chain in this corpus runs CVE → CWE → CAPEC → ATT&CK technique, which ends at what an adversary does. This is the hop after: what stops it.

- [T1649](/wiki/p/technique/T1649)

## Source

- [MITRE D3FEND D3-CP](https://d3fend.mitre.org/technique/D3-CP/)
