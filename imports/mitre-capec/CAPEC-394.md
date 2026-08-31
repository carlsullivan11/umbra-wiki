---
slug: attack-pattern/CAPEC-394
title: "CAPEC-394 — Using a Snap Gun Lock to Force a Lock"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-394]
related: []
provenance: imported
import_source: mitre-capec
import_id: CAPEC-394
updated_at: 2026-08-31
summary: "An attacker uses a Snap Gun, also known as a Pick Gun, to force the lock on a building or facility. A Pick Gun is a special type of lock picking instrument that works on similar principles as lock bumping. A snap gun is a hand-held device with an attached metal pick. The metal pi…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/394.html
---

# CAPEC-394: Using a Snap Gun Lock to Force a Lock

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | — |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker uses a Snap Gun, also known as a Pick Gun, to force the lock on a building or facility. A Pick Gun is a special type of lock picking instrument that works on similar principles as lock bumping. A snap gun is a hand-held device with an attached metal pick. The metal pick strikes the pins within the lock, transferring motion from the key pins to the driver pins and forcing the lock into momentary alignment. A standard lock is secured by a set of internal pins that prevent the device from turning. Spring loaded driver pins push down on the key pins. When the correct key is inserted, the ridges on the key push the key pins up and against the driver pins, causing correct alignment which allows the lock cylinder to rotate. A Snap Gun exploits this design by using a metal pin to strike all of the key pins at once, forcing the driver pins to shift into an unlocked position. Unlike bump keys or lock picks, a Snap Gun may damage the lock more easily, leaving evidence that the lock has been tampered with.

## Source

- [MITRE CAPEC CAPEC-394](https://capec.mitre.org/data/definitions/394.html)
