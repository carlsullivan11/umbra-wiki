---
slug: attack-pattern/CAPEC-169
title: "CAPEC-169 — Footprinting"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-169]
cwe_ids: [CWE-200]
mitre_ids: [T1217, T1592, T1595]
related: [weakness/CWE-200, technique/T1217, technique/T1592, technique/T1595]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-169
updated_at: 2026-08-31
summary: "An adversary engages in probing and exploration activities to identify constituents and properties of the target."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/169.html
---

# CAPEC-169: Footprinting

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Very Low |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary engages in probing and exploration activities to identify constituents and properties of the target.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-200](/wiki/p/weakness/CWE-200)

**ATT&CK techniques:** [T1217](/wiki/p/technique/T1217), [T1592](/wiki/p/technique/T1592), [T1595](/wiki/p/technique/T1595)

## Prerequisites

- An application must publicize identifiable information about the system or application through voluntary or involuntary means. Certain identification details of information systems are visible on communication networks (e.g., if an adversary uses a sniffer to inspect the traffic) due to their inherent structure and protocol standards. Any system or network that can be detected can be footprinted. However, some configuration choices may limit the useful information that can be collected during a footprinting attack.

## Skills required

- Low: The adversary knows how to send HTTP request, run the scan tool.

## Consequences

- Confidentiality: Read Data

## Mitigations

- Keep patches up to date by installing weekly or daily if possible.
- Shut down unnecessary services/ports.
- Change default passwords by choosing strong passwords.
- Curtail unexpected input.
- Encrypt and password-protect sensitive data.
- Avoid including information that has the potential to identify and compromise your organization's security such as access to business plans, formulas, and proprietary documents.

## Source

- [MITRE CAPEC CAPEC-169](https://capec.mitre.org/data/definitions/169.html)
