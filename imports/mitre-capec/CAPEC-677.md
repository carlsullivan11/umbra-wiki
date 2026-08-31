---
slug: attack-pattern/CAPEC-677
title: "CAPEC-677 — Server Motherboard Compromise"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-677]
mitre_ids: [T1195.003]
related: [technique/T1195.003]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-677
updated_at: 2026-08-31
summary: "Malware is inserted in a server motherboard (e.g., in the flash memory) in order to alter server functionality from that intended. The development environment or hardware/software support activity environment is susceptible to an adversary inserting malicious software into hardwa…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/677.html
---

# CAPEC-677: Server Motherboard Compromise

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

Malware is inserted in a server motherboard (e.g., in the flash memory) in order to alter server functionality from that intended. The development environment or hardware/software support activity environment is susceptible to an adversary inserting malicious software into hardware components during development or update.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**ATT&CK techniques:** [T1195.003](/wiki/p/technique/T1195.003)

## Prerequisites

- An adversary with access to hardware/software processes and tools within the development or hardware/software support environment can insert malicious software into hardware components during development or update/maintenance.

## Consequences

- Integrity: Execute Unauthorized Commands

## Mitigations

- Purchase IT systems, components and parts from government approved vendors whenever possible.
- Establish diversity among suppliers.
- Conduct rigorous threat assessments of suppliers.
- Require that Bills of Material (BoM) for critical parts and components be certified.
- Utilize contract language requiring contractors and subcontractors to flow down to subcontractors and suppliers SCRM and SCRA (Supply Chain Risk Assessment) requirements.
- Establish trusted supplier networks.

## Source

- [MITRE CAPEC CAPEC-677](https://capec.mitre.org/data/definitions/677.html)
