---
slug: attack-pattern/CAPEC-678
title: "CAPEC-678 — System Build Data Maliciously Altered"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-678]
mitre_ids: [T1195.002]
related: [technique/T1195.002]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-678
updated_at: 2026-08-31
summary: "During the system build process, the system is deliberately misconfigured by the alteration of the build data. Access to system configuration data files and build processes is susceptible to deliberate misconfiguration of the system."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/678.html
---

# CAPEC-678: System Build Data Maliciously Altered

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

During the system build process, the system is deliberately misconfigured by the alteration of the build data. Access to system configuration data files and build processes is susceptible to deliberate misconfiguration of the system.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**ATT&CK techniques:** [T1195.002](/wiki/p/technique/T1195.002)

## Prerequisites

- An adversary has access to the data files and processes used for executing system configuration and performing the build.

## Consequences

- Integrity: Execute Unauthorized Commands
- Access Control: Gain Privileges
- Confidentiality: Modify Data, Read Data

## Mitigations

- Implement configuration management security practices that protect the integrity of software and associated data.
- Monitor and control access to the configuration management system.
- Harden centralized repositories against attack.
- Establish acceptance criteria for configuration management check-in to assure integrity.
- Plan for and audit the security of configuration management administration processes.
- Maintain configuration control over operational systems.

## Source

- [MITRE CAPEC CAPEC-678](https://capec.mitre.org/data/definitions/678.html)
