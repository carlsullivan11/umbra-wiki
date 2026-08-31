---
slug: attack-pattern/CAPEC-397
title: "CAPEC-397 — Cloning Magnetic Strip Cards"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-397]
related: []
provenance: imported
import_source: mitre-capec
import_id: CAPEC-397
updated_at: 2026-08-31
summary: "An attacker duplicates the data on a Magnetic strip card (i.e. 'swipe card' or 'magstripe') to gain unauthorized access to a physical location or a person's private information. Magstripe cards encode data on a band of iron-based magnetic particles arrayed in a stripe along a rec…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/397.html
---

# CAPEC-397: Cloning Magnetic Strip Cards

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | — |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker duplicates the data on a Magnetic strip card (i.e. 'swipe card' or 'magstripe') to gain unauthorized access to a physical location or a person's private information. Magstripe cards encode data on a band of iron-based magnetic particles arrayed in a stripe along a rectangular card. Most magstripe card data formats conform to ISO standards 7810, 7811, 7813, 8583, and 4909. The primary advantage of magstripe technology is ease of encoding and portability, but this also renders magnetic strip cards susceptible to unauthorized duplication. If magstripe cards are used for access control, all an attacker need do is obtain a valid card long enough to make a copy of the card and then return the card to its location (i.e. a co-worker's desk). Magstripe reader/writers are widely available as well as software for analyzing data encoded on the cards. By swiping a valid card, it becomes trivial to make any number of duplicates that function as the original.

## Source

- [MITRE CAPEC CAPEC-397](https://capec.mitre.org/data/definitions/397.html)
