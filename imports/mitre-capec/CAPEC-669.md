---
slug: attack-pattern/CAPEC-669
title: "CAPEC-669 — Alteration of a Software Update"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-669]
mitre_ids: [T1195.002]
related: [technique/T1195.002]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-669
updated_at: 2026-08-31
summary: "An adversary with access to an organization’s software update infrastructure inserts malware into the content of an outgoing update to fielded systems where a wide range of malicious effects are possible. With the same level of access, the adversary can alter a software update to…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/669.html
---

# CAPEC-669: Alteration of a Software Update

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary with access to an organization’s software update infrastructure inserts malware into the content of an outgoing update to fielded systems where a wide range of malicious effects are possible. With the same level of access, the adversary can alter a software update to perform specific malicious acts including granting the adversary control over the software’s normal functionality.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**ATT&CK techniques:** [T1195.002](/wiki/p/technique/T1195.002)

## Prerequisites

- An adversary would need to have penetrated an organization’s software update infrastructure including gaining access to components supporting the configuration management of software versions and updates related to the software maintenance of customer systems.

## Skills required

- High: Skills required include the ability to infiltrate the organization’s software update infrastructure either from the Internet or from within the organization, including subcontractors, and be able to change software being delivered to customer/user systems in an undetected manner.

## Consequences

- Access Control: Gain Privileges
- Authorization: Execute Unauthorized Commands
- Integrity: Modify Data
- Confidentiality: Read Data

## Mitigations

- Have a Software Assurance Plan that includes maintaining strict configuration management control of source code, object code and software development, build and distribution tools; manual code reviews and static code analysis for developmental software; and tracking of all storage and movement of code.
- Require elevated privileges for distribution of software and software updates.

## Source

- [MITRE CAPEC CAPEC-669](https://capec.mitre.org/data/definitions/669.html)
