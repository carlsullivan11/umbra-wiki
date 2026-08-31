---
slug: attack-pattern/CAPEC-530
title: "CAPEC-530 — Provide Counterfeit Component"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-530]
related: []
provenance: imported
import_source: mitre-capec
import_id: CAPEC-530
updated_at: 2026-08-31
summary: "An attacker provides a counterfeit component during the procurement process of a lower-tier component supplier to a sub-system developer or integrator, which is then built into the system being upgraded or repaired by the victim, allowing the attacker to cause disruption or addit…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/530.html
---

# CAPEC-530: Provide Counterfeit Component

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker provides a counterfeit component during the procurement process of a lower-tier component supplier to a sub-system developer or integrator, which is then built into the system being upgraded or repaired by the victim, allowing the attacker to cause disruption or additional compromise.

## Prerequisites

- Advanced knowledge about the target system and sub-components.

## Skills required

- High: Able to develop and manufacture malicious system components that resemble legitimate name-brand components.

## Mitigations

- There are various methods to detect if the component is a counterfeit. See section II of [REF-703] for many techniques.

## Source

- [MITRE CAPEC CAPEC-530](https://capec.mitre.org/data/definitions/530.html)
