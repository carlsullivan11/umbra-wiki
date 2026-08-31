---
slug: attack-pattern/CAPEC-195
title: "CAPEC-195 — Principal Spoof"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-195]
related: []
provenance: imported
import_source: mitre-capec
import_id: CAPEC-195
updated_at: 2026-08-31
summary: "A Principal Spoof is a form of Identity Spoofing where an adversary pretends to be some other person in an interaction. This is often accomplished by crafting a message (either written, verbal, or visual) that appears to come from a person other than the adversary. Phishing and P…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/195.html
---

# CAPEC-195: Principal Spoof

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

A Principal Spoof is a form of Identity Spoofing where an adversary pretends to be some other person in an interaction. This is often accomplished by crafting a message (either written, verbal, or visual) that appears to come from a person other than the adversary. Phishing and Pharming attacks often attempt to do this so that their attempts to gather sensitive information appear to come from a legitimate source. A Principal Spoof does not use stolen or spoofed authentication credentials, instead relying on the appearance and content of the message to reflect identity.

## Prerequisites

- The target must associate data or activities with a person's identity and the adversary must be able to modify this identity without detection.

## Source

- [MITRE CAPEC CAPEC-195](https://capec.mitre.org/data/definitions/195.html)
