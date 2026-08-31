---
slug: attack-pattern/CAPEC-610
title: "CAPEC-610 — Cellular Data Injection"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-610]
related: []
provenance: imported
import_source: mitre-capec
import_id: CAPEC-610
updated_at: 2026-08-31
summary: "Adversaries inject data into mobile technology traffic (data flows or signaling data) to disrupt communications or conduct additional surveillance operations."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/610.html
---

# CAPEC-610: Cellular Data Injection

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | High |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

Adversaries inject data into mobile technology traffic (data flows or signaling data) to disrupt communications or conduct additional surveillance operations.

## Prerequisites

- None

## Skills required

- High: Often achieved by nation states in conjunction with commercial cellular providers to conduct cellular traffic intercept and possible traffic injection.

## Consequences

- Availability: Resource Consumption
- Availability: Modify Data

## Mitigations

- Commercial defensive technology to detect and alert to any attempts to modify mobile technology data flows or to inject new data into existing data flows and signaling data.

## Source

- [MITRE CAPEC CAPEC-610](https://capec.mitre.org/data/definitions/610.html)
