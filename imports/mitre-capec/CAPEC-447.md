---
slug: attack-pattern/CAPEC-447
title: "CAPEC-447 — Design Alteration"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-447]
related: []
provenance: imported
import_source: mitre-capec
import_id: CAPEC-447
updated_at: 2026-08-31
summary: "An adversary modifies the design of a technology, product, or component to acheive a negative impact once the system is deployed. In this type of attack, the goal of the adversary is to modify the design of the system, prior to development starting, in such a way that the negativ…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/447.html
---

# CAPEC-447: Design Alteration

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | High |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary modifies the design of a technology, product, or component to acheive a negative impact once the system is deployed. In this type of attack, the goal of the adversary is to modify the design of the system, prior to development starting, in such a way that the negative impact can be leveraged when the system is later deployed. Design alteration attacks differ from development alteration attacks in that design alteration attacks take place prior to development and which then may or may not be developed by the adverary. Design alteration attacks include modifying system designs to degrade system performance, cause unexpected states or errors, and general design changes that may lead to additional vulnerabilities. These attacks generally require insider access to modify design documents, but they may also be spoofed via web communications. The product is then developed and delivered to the user where the negative impact can be leveraged at a later time.

## Prerequisites

- Access to system design documentation prior to the development phase. This access is often obtained via insider access or by leveraging another attack pattern to gain permissions that the adversary wouldn't normally have.
- Ability to forge web communications to deliver modified design documentation.

## Consequences

- Authorization: Execute Unauthorized Commands
- Availability: Unreliable Execution
- Integrity: Alter Execution Logic

## Mitigations

- Assess design documentation prior to development to ensure that they function as intended and without any malicious functionality.
- Ensure that design documentation is saved in a secure location and has proper access controls set in place to avoid unnecessary modification.

## Source

- [MITRE CAPEC CAPEC-447](https://capec.mitre.org/data/definitions/447.html)
