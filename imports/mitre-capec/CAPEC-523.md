---
slug: attack-pattern/CAPEC-523
title: "CAPEC-523 — Malicious Software Implanted"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-523]
mitre_ids: [T1195.002]
related: [technique/T1195.002]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-523
updated_at: 2026-08-31
summary: "An attacker implants malicious software into the system in the supply chain distribution channel, with purpose of causing malicious disruption or allowing for additional compromise when the system is deployed."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/523.html
---

# CAPEC-523: Malicious Software Implanted

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker implants malicious software into the system in the supply chain distribution channel, with purpose of causing malicious disruption or allowing for additional compromise when the system is deployed.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**ATT&CK techniques:** [T1195.002](/wiki/p/technique/T1195.002)

## Prerequisites

- Physical access to the system after it has left the manufacturer but before it is deployed at the victim location.

## Skills required

- High: Advanced knowledge of the design of the system and it's operating system components and subcomponents.
- High: Malicious software creation.

## Mitigations

- Deploy strong code integrity policies to allow only authorized apps to run.
- Use endpoint detection and response solutions that can automaticalkly detect and remediate suspicious activities.
- Maintain a highly secure build and update infrastructure by immediately applying security patches for OS and software, implementing mandatory integrity controls to ensure only trusted tools run, and requiring multi-factor authentication for admins.
- Require SSL for update channels and implement certificate transparency based verification.
- Sign everything, including configuration files, XML files and packages.
- Develop an incident response process, disclose supply chain incidents and notify customers with accurate and timely information.

## Source

- [MITRE CAPEC CAPEC-523](https://capec.mitre.org/data/definitions/523.html)
