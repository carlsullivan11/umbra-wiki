---
slug: attack-pattern/CAPEC-531
title: "CAPEC-531 — Hardware Component Substitution"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-531]
mitre_ids: [T1195.003]
related: [technique/T1195.003]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-531
updated_at: 2026-08-31
summary: "An attacker substitutes out a tested and approved hardware component for a maliciously-altered hardware component. This type of attack is carried out directly on the system, enabling the attacker to then cause disruption or additional compromise."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/531.html
---

# CAPEC-531: Hardware Component Substitution

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker substitutes out a tested and approved hardware component for a maliciously-altered hardware component. This type of attack is carried out directly on the system, enabling the attacker to then cause disruption or additional compromise.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**ATT&CK techniques:** [T1195.003](/wiki/p/technique/T1195.003)

## Prerequisites

- Physical access to the system or the integration facility where hardware components are kept.

## Skills required

- High: Able to develop and manufacture malicious system components that perform the same functions and processes as their non-malicious counterparts.

## Source

- [MITRE CAPEC CAPEC-531](https://capec.mitre.org/data/definitions/531.html)
