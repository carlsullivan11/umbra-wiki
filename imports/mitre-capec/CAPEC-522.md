---
slug: attack-pattern/CAPEC-522
title: "CAPEC-522 — Malicious Hardware Component Replacement"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-522]
mitre_ids: [T1195.003]
related: [technique/T1195.003]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-522
updated_at: 2026-08-31
summary: "An adversary replaces legitimate hardware in the system with faulty counterfeit or tampered hardware in the supply chain distribution channel, with purpose of causing malicious disruption or allowing for additional compromise when the system is deployed."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/522.html
---

# CAPEC-522: Malicious Hardware Component Replacement

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary replaces legitimate hardware in the system with faulty counterfeit or tampered hardware in the supply chain distribution channel, with purpose of causing malicious disruption or allowing for additional compromise when the system is deployed.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**ATT&CK techniques:** [T1195.003](/wiki/p/technique/T1195.003)

## Prerequisites

- Physical access to the system after it has left the manufacturer but before it is deployed at the victim location.

## Skills required

- High: Advanced knowledge of the design of the system.
- High: Hardware creation and manufacture of replacement components.

## Mitigations

- Ensure that all contractors and sub-suppliers use trusted means of shipping (e.g., bonded/cleared/vetted and insured couriers) to ensure that components, once purchased, are not subject to compromise during their delivery.
- Prevent or detect tampering with critical hardware or firmware components while in transit through use of state-of-the-art anti-tamper devices.
- Use tamper-resistant and tamper-evident packaging when shipping critical components (e.g., plastic coating for circuit boards, tamper tape, paint, sensors, and/or seals for cases and containers) and inspect received system components for evidence of tampering.

## Source

- [MITRE CAPEC CAPEC-522](https://capec.mitre.org/data/definitions/522.html)
