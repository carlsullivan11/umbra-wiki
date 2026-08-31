---
slug: attack-pattern/CAPEC-392
title: "CAPEC-392 — Lock Bumping"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-392]
related: []
provenance: imported
import_source: mitre-capec
import_id: CAPEC-392
updated_at: 2026-08-31
summary: "An attacker uses a bump key to force a lock on a building or facility and gain entry. Lock Bumping is the use of a special type of key that can be tapped or bumped to cause the pins within the lock to fall into temporary alignment, allowing the lock to be opened. Lock bumping all…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/392.html
---

# CAPEC-392: Lock Bumping

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | — |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker uses a bump key to force a lock on a building or facility and gain entry. Lock Bumping is the use of a special type of key that can be tapped or bumped to cause the pins within the lock to fall into temporary alignment, allowing the lock to be opened. Lock bumping allows an attacker to open a lock without having the correct key. A standard lock is secured by a set of internal pins that prevent the device from turning. Spring loaded driver pins push down on the key pins. When the correct key is inserted, the ridges on the key push the key pins up and against the driver pins, causing correct alignment which allows the lock cylinder to rotate. A bump key is a specially constructed key that exploits this design. When the bump key is struck or firmly tapped, its teeth transfer the force of the tap into the key pins, causing the lock to momentarily shift into proper alignment for the mechanism to be opened.

## Source

- [MITRE CAPEC CAPEC-392](https://capec.mitre.org/data/definitions/392.html)
