---
slug: attack-pattern/CAPEC-399
title: "CAPEC-399 — Cloning RFID Cards or Chips"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-399]
related: []
provenance: imported
import_source: mitre-capec
import_id: CAPEC-399
updated_at: 2026-08-31
summary: "An attacker analyzes data returned by an RFID chip and uses this information to duplicate a RFID signal that responds identically to the target chip. In some cases RFID chips are used for building access control, employee identification, or as markers on products being delivered …"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/399.html
---

# CAPEC-399: Cloning RFID Cards or Chips

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | — |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker analyzes data returned by an RFID chip and uses this information to duplicate a RFID signal that responds identically to the target chip. In some cases RFID chips are used for building access control, employee identification, or as markers on products being delivered along a supply chain. Some organizations also embed RFID tags inside computer assets to trigger alarms if they are removed from particular rooms, zones, or buildings. Similar to Magnetic strip cards, RFID cards are susceptible to duplication (cloning) and reuse.

## Source

- [MITRE CAPEC CAPEC-399](https://capec.mitre.org/data/definitions/399.html)
