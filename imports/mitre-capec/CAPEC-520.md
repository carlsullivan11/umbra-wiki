---
slug: attack-pattern/CAPEC-520
title: "CAPEC-520 — Counterfeit Hardware Component Inserted During Product Assembly"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-520]
mitre_ids: [T1195.003]
related: [technique/T1195.003]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-520
updated_at: 2026-08-31
summary: "An adversary with either direct access to the product assembly process or to the supply of subcomponents used in the product assembly process introduces counterfeit hardware components into product assembly. The assembly containing the counterfeit components results in a system s…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/520.html
---

# CAPEC-520: Counterfeit Hardware Component Inserted During Product Assembly

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary with either direct access to the product assembly process or to the supply of subcomponents used in the product assembly process introduces counterfeit hardware components into product assembly. The assembly containing the counterfeit components results in a system specifically designed for malicious purposes.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**ATT&CK techniques:** [T1195.003](/wiki/p/technique/T1195.003)

## Prerequisites

- The adversary will need either physical access or be able to supply malicious hardware components to the product development facility.

## Skills required

- High: Resources to maliciously construct components used by the manufacturer.
- High: Resources to physically infiltrate manufacturer or manufacturer's supplier.

## Mitigations

- Hardware attacks are often difficult to detect, as inserted components can be difficult to identify or remain dormant for an extended period of time.
- Acquire hardware and hardware components from trusted vendors. Additionally, determine where vendors purchase components or if any components are created/acquired via subcontractors to determine where supply chain risks may exist.

## Source

- [MITRE CAPEC CAPEC-520](https://capec.mitre.org/data/definitions/520.html)
