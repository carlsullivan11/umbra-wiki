---
slug: attack-pattern/CAPEC-388
title: "CAPEC-388 — Application API Button Hijacking"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-388]
cwe_ids: [CWE-311, CWE-345, CWE-346, CWE-471, CWE-602]
related: [weakness/CWE-311, weakness/CWE-345, weakness/CWE-346, weakness/CWE-471, weakness/CWE-602]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-388
updated_at: 2026-08-31
summary: "An attacker manipulates either egress or ingress data from a client within an application framework in order to change the destination and/or content of buttons displayed to a user within API messages. Performing this attack allows the attacker to manipulate content in such a way…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/388.html
---

# CAPEC-388: Application API Button Hijacking

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker manipulates either egress or ingress data from a client within an application framework in order to change the destination and/or content of buttons displayed to a user within API messages. Performing this attack allows the attacker to manipulate content in such a way as to produce messages or content that looks authentic but contains buttons that point to an attacker controlled destination.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-311](/wiki/p/weakness/CWE-311), [CWE-345](/wiki/p/weakness/CWE-345), [CWE-346](/wiki/p/weakness/CWE-346), [CWE-471](/wiki/p/weakness/CWE-471), [CWE-602](/wiki/p/weakness/CWE-602)

## Prerequisites

- Targeted software is utilizing application framework APIs

## Source

- [MITRE CAPEC CAPEC-388](https://capec.mitre.org/data/definitions/388.html)
