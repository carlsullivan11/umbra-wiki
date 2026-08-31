---
slug: attack-pattern/CAPEC-395
title: "CAPEC-395 — Bypassing Electronic Locks and Access Controls"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-395]
related: []
provenance: imported
import_source: mitre-capec
import_id: CAPEC-395
updated_at: 2026-08-31
summary: "An attacker exploits security assumptions to bypass electronic locks or other forms of access controls. Most attacks against electronic access controls follow similar methods but utilize different tools. Some electronic locks utilize magnetic strip cards, others employ RFID tags …"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/395.html
---

# CAPEC-395: Bypassing Electronic Locks and Access Controls

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | — |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker exploits security assumptions to bypass electronic locks or other forms of access controls. Most attacks against electronic access controls follow similar methods but utilize different tools. Some electronic locks utilize magnetic strip cards, others employ RFID tags embedded within a card or badge, or may involve more sophisticated protections such as voice-print, thumb-print, or retinal biometrics. Magnetic Strip and RFID technologies are the most widespread because they are cost effective to deploy and more easily integrated with other electronic security measures. These technologies share common weaknesses that an attacker can exploit to gain access to a facility protected by the mechanisms via copying legitimate cards or badges, or generating new cards using reverse-engineered algorithms.

## Source

- [MITRE CAPEC CAPEC-395](https://capec.mitre.org/data/definitions/395.html)
