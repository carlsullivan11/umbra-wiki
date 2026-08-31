---
slug: attack-pattern/CAPEC-398
title: "CAPEC-398 — Magnetic Strip Card Brute Force Attacks"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-398]
related: []
provenance: imported
import_source: mitre-capec
import_id: CAPEC-398
updated_at: 2026-08-31
summary: "An adversary analyzes the data on two or more magnetic strip cards and is able to generate new cards containing valid sequences that allow unauthorized access and/or impersonation of individuals."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/398.html
---

# CAPEC-398: Magnetic Strip Card Brute Force Attacks

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | — |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary analyzes the data on two or more magnetic strip cards and is able to generate new cards containing valid sequences that allow unauthorized access and/or impersonation of individuals.

## Prerequisites

- The ability to calculate a card checksum and write out a valid checksum value. Some cards are protected by a checksum calculation, therefore it is necessary to determine what algorithm is being used to calculate the checksum and to employ that algorithm to calculate and write a new valid checksum for the card being created.

## Source

- [MITRE CAPEC CAPEC-398](https://capec.mitre.org/data/definitions/398.html)
