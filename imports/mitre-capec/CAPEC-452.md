---
slug: attack-pattern/CAPEC-452
title: "CAPEC-452 — Infected Hardware"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-452]
related: []
provenance: imported
import_source: mitre-capec
import_id: CAPEC-452
updated_at: 2026-08-31
summary: "An adversary inserts malicious logic into hardware, typically in the form of a computer virus or rootkit. This logic is often hidden from the user of the hardware and works behind the scenes to achieve negative impacts. This pattern of attack focuses on hardware already fielded a…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/452.html
---

# CAPEC-452: Infected Hardware

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | High |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary inserts malicious logic into hardware, typically in the form of a computer virus or rootkit. This logic is often hidden from the user of the hardware and works behind the scenes to achieve negative impacts. This pattern of attack focuses on hardware already fielded and used in operation as opposed to hardware that is still under development and part of the supply chain.

## Prerequisites

- Access to the hardware currently deployed at a victim location.

## Consequences

- Authorization: Execute Unauthorized Commands

## Source

- [MITRE CAPEC CAPEC-452](https://capec.mitre.org/data/definitions/452.html)
