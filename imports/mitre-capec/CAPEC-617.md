---
slug: attack-pattern/CAPEC-617
title: "CAPEC-617 — Cellular Rogue Base Station"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-617]
related: []
provenance: imported
import_source: mitre-capec
import_id: CAPEC-617
updated_at: 2026-08-31
summary: "In this attack scenario, the attacker imitates a cellular base station with their own 'rogue' base station equipment. Since cellular devices connect to whatever station has the strongest signal, the attacker can easily convince a targeted cellular device (e.g. the retransmission …"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/617.html
---

# CAPEC-617: Cellular Rogue Base Station

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Low |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

In this attack scenario, the attacker imitates a cellular base station with their own "rogue" base station equipment. Since cellular devices connect to whatever station has the strongest signal, the attacker can easily convince a targeted cellular device (e.g. the retransmission device) to talk to the rogue base station.

## Prerequisites

- None

## Skills required

- Low: This technique has been demonstrated by amateur hackers and commercial tools and open source projects are available to automate the attack.

## Consequences

- Confidentiality: Read Data

## Mitigations

- Passively monitor cellular network connection for real-time threat detection and logging for manual review.

## Source

- [MITRE CAPEC CAPEC-617](https://capec.mitre.org/data/definitions/617.html)
