---
slug: attack-pattern/CAPEC-458
title: "CAPEC-458 — Flash Memory Attacks"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-458]
cwe_ids: [CWE-1282]
related: [weakness/CWE-1282]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-458
updated_at: 2026-08-31
summary: "An adversary inserts malicious logic into a product or technology via flashing the on-board memory with a code-base that contains malicious logic. Various attacks exist against the integrity of flash memory, the most direct being rootkits coded into the BIOS or chipset of a devic…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/458.html
---

# CAPEC-458: Flash Memory Attacks

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | — |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary inserts malicious logic into a product or technology via flashing the on-board memory with a code-base that contains malicious logic. Various attacks exist against the integrity of flash memory, the most direct being rootkits coded into the BIOS or chipset of a device.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-1282](/wiki/p/weakness/CWE-1282)

## Source

- [MITRE CAPEC CAPEC-458](https://capec.mitre.org/data/definitions/458.html)
