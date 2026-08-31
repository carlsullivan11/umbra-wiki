---
slug: attack-pattern/CAPEC-521
title: "CAPEC-521 — Hardware Design Specifications Are Altered"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-521]
related: []
provenance: imported
import_source: mitre-capec
import_id: CAPEC-521
updated_at: 2026-08-31
summary: "An attacker with access to a manufacturer's hardware manufacturing process documentation alters the design specifications, which introduces flaws advantageous to the attacker once the system is deployed."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/521.html
---

# CAPEC-521: Hardware Design Specifications Are Altered

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker with access to a manufacturer's hardware manufacturing process documentation alters the design specifications, which introduces flaws advantageous to the attacker once the system is deployed.

## Prerequisites

- Advanced knowledge of hardware capabilities of a manufacturer's product.
- Access to the manufacturer's documentation.

## Skills required

- High: Ability to read, interpret, and subsequently alter manufacturer's documentation to cause errors in design specifications.
- High: Ability to stealthly gain access via remote compromise or physical access to the manufacturer's documentation.

## Mitigations

- Digitize documents and cryptographically sign them to verify authenticity.
- Password protect documents and make them read-only for unauthorized users.
- Avoid emailing important documents and configurations.
- Ensure deleted files are actually deleted.
- Maintain backups of the document for recovery and verification.
- Separate need-to-know information from system configuration information depending on the user.

## Source

- [MITRE CAPEC CAPEC-521](https://capec.mitre.org/data/definitions/521.html)
