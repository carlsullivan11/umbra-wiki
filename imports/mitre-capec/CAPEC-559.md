---
slug: attack-pattern/CAPEC-559
title: "CAPEC-559 — Orbital Jamming"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-559]
related: []
provenance: imported
import_source: mitre-capec
import_id: CAPEC-559
updated_at: 2026-08-31
summary: "In this attack pattern, the adversary sends disruptive signals at a target satellite using a rogue uplink station to disrupt the intended transmission. Those within the satellite's footprint are prevented from reaching the satellite's targeted or neighboring channels. The satelli…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/559.html
---

# CAPEC-559: Orbital Jamming

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

In this attack pattern, the adversary sends disruptive signals at a target satellite using a rogue uplink station to disrupt the intended transmission. Those within the satellite's footprint are prevented from reaching the satellite's targeted or neighboring channels. The satellite's footprint size depends upon its position in the sky; higher orbital satellites cover multiple continents.

## Prerequisites

- This attack requires the knowledge of the satellite's coordinates for targeting.

## Consequences

- Availability: Other

## Source

- [MITRE CAPEC CAPEC-559](https://capec.mitre.org/data/definitions/559.html)
