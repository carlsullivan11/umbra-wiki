---
slug: attack-pattern/CAPEC-516
title: "CAPEC-516 — Hardware Component Substitution During Baselining"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-516]
mitre_ids: [T1195.003]
related: [technique/T1195.003]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-516
updated_at: 2026-08-31
summary: "An adversary with access to system components during allocated baseline development can substitute a maliciously altered hardware component for a baseline component during the product development and research phases. This can lead to adjustments and calibrations being made in the…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/516.html
---

# CAPEC-516: Hardware Component Substitution During Baselining

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary with access to system components during allocated baseline development can substitute a maliciously altered hardware component for a baseline component during the product development and research phases. This can lead to adjustments and calibrations being made in the product so that when the final product, now containing the modified component, is deployed it will not perform as designed and be advantageous to the adversary.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**ATT&CK techniques:** [T1195.003](/wiki/p/technique/T1195.003)

## Prerequisites

- The adversary will need either physical access or be able to supply malicious hardware components to the product development facility.

## Skills required

- Medium: Intelligence data on victim's purchasing habits.
- High: Resources to maliciously construct/alter hardware components used for testing by the supplier.
- High: Resources to physically infiltrate supplier.

## Mitigations

- Hardware attacks are often difficult to detect, as inserted components can be difficult to identify or remain dormant for an extended period of time.
- Acquire hardware and hardware components from trusted vendors. Additionally, determine where vendors purchase components or if any components are created/acquired via subcontractors to determine where supply chain risks may exist.

## Source

- [MITRE CAPEC CAPEC-516](https://capec.mitre.org/data/definitions/516.html)
