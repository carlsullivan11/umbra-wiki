---
slug: attack-pattern/CAPEC-534
title: "CAPEC-534 — Malicious Hardware Update"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-534]
related: []
provenance: imported
import_source: mitre-capec
import_id: CAPEC-534
updated_at: 2026-08-31
summary: "An adversary introduces malicious hardware during an update or replacement procedure, allowing for additional compromise or site disruption at the victim location. After deployment, it is not uncommon for upgrades and replacements to occur involving hardware and various replaceab…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/534.html
---

# CAPEC-534: Malicious Hardware Update

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | High |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary introduces malicious hardware during an update or replacement procedure, allowing for additional compromise or site disruption at the victim location. After deployment, it is not uncommon for upgrades and replacements to occur involving hardware and various replaceable parts. These upgrades and replacements are intended to correct defects, provide additional features, and to replace broken or worn-out parts. However, by forcing or tricking the replacement of a good component with a defective or corrupted component, an adversary can leverage known defects to obtain a desired malicious impact.

## Skills required

- High: Able to develop and manufacture malicious hardware components that perform the same functions and processes as their non-malicious counterparts.

## Source

- [MITRE CAPEC CAPEC-534](https://capec.mitre.org/data/definitions/534.html)
