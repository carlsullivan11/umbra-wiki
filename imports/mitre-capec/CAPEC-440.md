---
slug: attack-pattern/CAPEC-440
title: "CAPEC-440 — Hardware Integrity Attack"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-440]
mitre_ids: [T1195.003, T1200]
related: [technique/T1195.003, technique/T1200]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-440
updated_at: 2026-08-31
summary: "An adversary exploits a weakness in the system maintenance process and causes a change to be made to a technology, product, component, or sub-component or a new one installed during its deployed use at the victim location for the purpose of carrying out an attack."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/440.html
---

# CAPEC-440: Hardware Integrity Attack

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | High |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary exploits a weakness in the system maintenance process and causes a change to be made to a technology, product, component, or sub-component or a new one installed during its deployed use at the victim location for the purpose of carrying out an attack.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**ATT&CK techniques:** [T1195.003](/wiki/p/technique/T1195.003), [T1200](/wiki/p/technique/T1200)

## Prerequisites

- Influence over the deployed system at a victim location.

## Consequences

- Integrity: Execute Unauthorized Commands

## Source

- [MITRE CAPEC CAPEC-440](https://capec.mitre.org/data/definitions/440.html)
