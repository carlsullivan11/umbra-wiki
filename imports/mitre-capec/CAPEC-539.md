---
slug: attack-pattern/CAPEC-539
title: "CAPEC-539 — ASIC With Malicious Functionality"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-539]
mitre_ids: [T1195.003]
related: [technique/T1195.003]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-539
updated_at: 2026-08-31
summary: "An attacker with access to the development environment process of an application-specific integrated circuit (ASIC) for a victim system being developed or maintained after initial deployment can insert malicious functionality into the system for the purpose of disruption or furth…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/539.html
---

# CAPEC-539: ASIC With Malicious Functionality

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker with access to the development environment process of an application-specific integrated circuit (ASIC) for a victim system being developed or maintained after initial deployment can insert malicious functionality into the system for the purpose of disruption or further compromise.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**ATT&CK techniques:** [T1195.003](/wiki/p/technique/T1195.003)

## Prerequisites

- The attacker must have working knowledge of some if not all of the components involved in the target system as well as the infrastructure and development environment of the manufacturer.
- Advanced knowledge about the ASIC installed within the target system.

## Skills required

- High: Able to develop and manufacture malicious subroutines for an ASIC environment without degradation of existing functions and processes.

## Source

- [MITRE CAPEC CAPEC-539](https://capec.mitre.org/data/definitions/539.html)
