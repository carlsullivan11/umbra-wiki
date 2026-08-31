---
slug: attack-pattern/CAPEC-535
title: "CAPEC-535 — Malicious Gray Market Hardware"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-535]
related: []
provenance: imported
import_source: mitre-capec
import_id: CAPEC-535
updated_at: 2026-08-31
summary: "An attacker maliciously alters hardware components that will be sold on the gray market, allowing for victim disruption and compromise when the victim needs replacement hardware components for systems where the parts are no longer in regular supply from original suppliers, or whe…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/535.html
---

# CAPEC-535: Malicious Gray Market Hardware

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker maliciously alters hardware components that will be sold on the gray market, allowing for victim disruption and compromise when the victim needs replacement hardware components for systems where the parts are no longer in regular supply from original suppliers, or where the hardware components from the attacker seems to be a great benefit from a cost perspective.

## Prerequisites

- Physical access to a gray market reseller's hardware components supply, or the ability to appear as a gray market reseller to the victim's buyer.

## Skills required

- High: Able to develop and manufacture malicious hardware components that perform the same functions and processes as their non-malicious counterparts.

## Mitigations

- Purchase only from authorized resellers.
- Validate serial numbers from multiple sources

## Source

- [MITRE CAPEC CAPEC-535](https://capec.mitre.org/data/definitions/535.html)
