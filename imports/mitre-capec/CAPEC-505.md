---
slug: attack-pattern/CAPEC-505
title: "CAPEC-505 — Scheme Squatting"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-505]
related: []
provenance: imported
import_source: mitre-capec
import_id: CAPEC-505
updated_at: 2026-08-31
summary: "An adversary, through a previously installed malicious application, registers for a URL scheme intended for a target application that has not been installed. Thereafter, messages intended for the target application are handled by the malicious application. Upon receiving a messag…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/505.html
---

# CAPEC-505: Scheme Squatting

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | — |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary, through a previously installed malicious application, registers for a URL scheme intended for a target application that has not been installed. Thereafter, messages intended for the target application are handled by the malicious application. Upon receiving a message, the malicious application displays a screen that mimics the target application, thereby convincing the user to enter sensitive information. This type of attack is most often used to obtain sensitive information (e.g., credentials) from the user as they think that they are interacting with the intended target application.

## Mitigations

- The only known mitigation to this attack is to avoid installing the malicious application on the device. Applications usually have to declare the schemes they wish to register, so detecting this during a review is feasible.

## Source

- [MITRE CAPEC CAPEC-505](https://capec.mitre.org/data/definitions/505.html)
