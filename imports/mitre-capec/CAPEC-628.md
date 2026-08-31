---
slug: attack-pattern/CAPEC-628
title: "CAPEC-628 — Carry-Off GPS Attack"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-628]
related: []
provenance: imported
import_source: mitre-capec
import_id: CAPEC-628
updated_at: 2026-08-31
summary: "A common form of a GPS spoofing attack, commonly termed a carry-off attack begins with an adversary broadcasting signals synchronized with the genuine signals observed by the target receiver. The power of the counterfeit signals is then gradually increased and drawn away from the…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/628.html
---

# CAPEC-628: Carry-Off GPS Attack

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

A common form of a GPS spoofing attack, commonly termed a carry-off attack begins with an adversary broadcasting signals synchronized with the genuine signals observed by the target receiver. The power of the counterfeit signals is then gradually increased and drawn away from the genuine signals. Over time, the adversary can carry the target away from their intended destination and toward a location chosen by the adversary.

## Prerequisites

- The target must be relying on valid GPS signal to perform critical operations.

## Skills required

- High: This attack requires advanced knoweldge in GPS technology.

## Source

- [MITRE CAPEC CAPEC-628](https://capec.mitre.org/data/definitions/628.html)
