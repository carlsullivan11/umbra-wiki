---
slug: attack-pattern/CAPEC-583
title: "CAPEC-583 — Disabling Network Hardware"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-583]
related: []
provenance: imported
import_source: mitre-capec
import_id: CAPEC-583
updated_at: 2026-08-31
summary: "In this attack pattern, an adversary physically disables networking hardware by powering it down or disconnecting critical equipment. Disabling or shutting off critical system resources prevents them from performing their service as intended, which can have direct and indirect co…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/583.html
---

# CAPEC-583: Disabling Network Hardware

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | — |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

In this attack pattern, an adversary physically disables networking hardware by powering it down or disconnecting critical equipment. Disabling or shutting off critical system resources prevents them from performing their service as intended, which can have direct and indirect consequences on other systems. This attack pattern is considerably less technical than the selective blocking used in most obstruction attacks.

## Prerequisites

- The adversary requires physical access to the targeted communications equipment (networking devices, cables, etc.), which may be spread over a wide area.

## Consequences

- Availability: Other

## Mitigations

- Ensure rigorous physical defensive measures to keep the adversary from accessing critical systems..

## Source

- [MITRE CAPEC CAPEC-583](https://capec.mitre.org/data/definitions/583.html)
