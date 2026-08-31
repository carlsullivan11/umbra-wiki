---
slug: attack-pattern/CAPEC-518
title: "CAPEC-518 — Documentation Alteration to Produce Under-performing Systems"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-518]
related: []
provenance: imported
import_source: mitre-capec
import_id: CAPEC-518
updated_at: 2026-08-31
summary: "An attacker with access to a manufacturer's documentation alters the descriptions of system capabilities with the intent of causing errors in derived system requirements, impacting the overall effectiveness and capability of the system, allowing an attacker to take advantage of t…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/518.html
---

# CAPEC-518: Documentation Alteration to Produce Under-performing Systems

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker with access to a manufacturer's documentation alters the descriptions of system capabilities with the intent of causing errors in derived system requirements, impacting the overall effectiveness and capability of the system, allowing an attacker to take advantage of the introduced system capability flaw once the system is deployed.

## Prerequisites

- Advanced knowledge of software and hardware capabilities of a manufacturer's product.
- Access to the manufacturer's documentation.

## Skills required

- High: Ability to read, interpret, and subsequently alter manufacturer's documentation to misrepresent system capabilities.
- High: Ability to stealthly gain access via remote compromise or physical access to the manufacturer's documentation.

## Mitigations

- Digitize documents and cryptographically sign them to verify authenticity.
- Password protect documents and make them read-only for unauthorized users.
- Avoid emailing important documents and configurations.
- Ensure deleted files are actually deleted.
- Maintain backups of the document for recovery and verification.
- Separate need-to-know information from system configuration information depending on the user.

## Source

- [MITRE CAPEC CAPEC-518](https://capec.mitre.org/data/definitions/518.html)
