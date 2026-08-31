---
slug: attack-pattern/CAPEC-456
title: "CAPEC-456 — Infected Memory"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-456]
cwe_ids: [CWE-1257, CWE-1260, CWE-1274, CWE-1312, CWE-1316]
related: [weakness/CWE-1257, weakness/CWE-1260, weakness/CWE-1274, weakness/CWE-1312, weakness/CWE-1316]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-456
updated_at: 2026-08-31
summary: "An adversary inserts malicious logic into memory enabling them to achieve a negative impact. This logic is often hidden from the user of the system and works behind the scenes to achieve negative impacts. This pattern of attack focuses on systems already fielded and used in opera…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/456.html
---

# CAPEC-456: Infected Memory

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | High |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary inserts malicious logic into memory enabling them to achieve a negative impact. This logic is often hidden from the user of the system and works behind the scenes to achieve negative impacts. This pattern of attack focuses on systems already fielded and used in operation as opposed to systems that are still under development and part of the supply chain.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-1257](/wiki/p/weakness/CWE-1257), [CWE-1260](/wiki/p/weakness/CWE-1260), [CWE-1274](/wiki/p/weakness/CWE-1274), [CWE-1312](/wiki/p/weakness/CWE-1312), [CWE-1316](/wiki/p/weakness/CWE-1316)

## Consequences

- Authorization: Execute Unauthorized Commands

## Mitigations

- Leverage anti-virus products to detect stop operations with known virus.

## Source

- [MITRE CAPEC CAPEC-456](https://capec.mitre.org/data/definitions/456.html)
