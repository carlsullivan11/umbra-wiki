---
slug: attack-pattern/CAPEC-519
title: "CAPEC-519 — Documentation Alteration to Cause Errors in System Design"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-519]
related: []
provenance: imported
import_source: mitre-capec
import_id: CAPEC-519
updated_at: 2026-08-31
summary: "An attacker with access to a manufacturer's documentation containing requirements allocation and software design processes maliciously alters the documentation in order to cause errors in system design. This allows the attacker to take advantage of a weakness in a deployed system…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/519.html
---

# CAPEC-519: Documentation Alteration to Cause Errors in System Design

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker with access to a manufacturer's documentation containing requirements allocation and software design processes maliciously alters the documentation in order to cause errors in system design. This allows the attacker to take advantage of a weakness in a deployed system of the manufacturer for malicious purposes.

## Prerequisites

- Advanced knowledge of software capabilities of a manufacturer's product.
- Access to the manufacturer's documentation.

## Skills required

- High: Ability to read, interpret, and subsequently alter manufacturer's documentation to cause errors in system design.
- High: Ability to stealthly gain access via remote compromise or physical access to the manufacturer's documentation.

## Mitigations

- Digitize documents and cryptographically sign them to verify authenticity.
- Password protect documents and make them read-only for unauthorized users.
- Avoid emailing important documents and configurations.
- Ensure deleted files are actually deleted.
- Maintain multiple instances of the document across different privileged users for recovery and verification.

## Source

- [MITRE CAPEC CAPEC-519](https://capec.mitre.org/data/definitions/519.html)
