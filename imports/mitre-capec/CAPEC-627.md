---
slug: attack-pattern/CAPEC-627
title: "CAPEC-627 — Counterfeit GPS Signals"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-627]
related: []
provenance: imported
import_source: mitre-capec
import_id: CAPEC-627
updated_at: 2026-08-31
summary: "An adversary attempts to deceive a GPS receiver by broadcasting counterfeit GPS signals, structured to resemble a set of normal GPS signals. These spoofed signals may be structured in such a way as to cause the receiver to estimate its position to be somewhere other than where it…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/627.html
---

# CAPEC-627: Counterfeit GPS Signals

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary attempts to deceive a GPS receiver by broadcasting counterfeit GPS signals, structured to resemble a set of normal GPS signals. These spoofed signals may be structured in such a way as to cause the receiver to estimate its position to be somewhere other than where it actually is, or to be located where it is but at a different time, as determined by the adversary.

## Prerequisites

- The target must be relying on valid GPS signal to perform critical operations.

## Skills required

- High: The ability to spoof GPS signals is not trival.

## Consequences

- Integrity: Modify Data

## Source

- [MITRE CAPEC CAPEC-627](https://capec.mitre.org/data/definitions/627.html)
