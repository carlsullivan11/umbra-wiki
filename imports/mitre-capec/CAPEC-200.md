---
slug: attack-pattern/CAPEC-200
title: "CAPEC-200 — Removal of filters: Input filters, output filters, data masking"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-200]
related: []
provenance: imported
import_source: mitre-capec
import_id: CAPEC-200
updated_at: 2026-08-31
summary: "An attacker removes or disables filtering mechanisms on the target application. Input filters prevent invalid data from being sent to an application (for example, overly large inputs that might cause a buffer overflow or other malformed inputs that may not be correctly handled by…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/200.html
---

# CAPEC-200: Removal of filters: Input filters, output filters, data masking

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker removes or disables filtering mechanisms on the target application. Input filters prevent invalid data from being sent to an application (for example, overly large inputs that might cause a buffer overflow or other malformed inputs that may not be correctly handled by an application). Input filters might also be designed to constrained executable content.

## Prerequisites

- The target application must utilize some sort of filtering mechanism (input, output, or data masking).

## Source

- [MITRE CAPEC CAPEC-200](https://capec.mitre.org/data/definitions/200.html)
