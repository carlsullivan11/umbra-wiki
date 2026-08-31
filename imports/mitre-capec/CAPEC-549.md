---
slug: attack-pattern/CAPEC-549
title: "CAPEC-549 — Local Execution of Code"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-549]
cwe_ids: [CWE-829]
related: [weakness/CWE-829]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-549
updated_at: 2026-08-31
summary: "An adversary installs and executes malicious code on the target system in an effort to achieve a negative technical impact. Examples include rootkits, ransomware, spyware, adware, and others."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/549.html
---

# CAPEC-549: Local Execution of Code

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | High |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary installs and executes malicious code on the target system in an effort to achieve a negative technical impact. Examples include rootkits, ransomware, spyware, adware, and others.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-829](/wiki/p/weakness/CWE-829)

## Prerequisites

- Knowledge of the target system's vulnerabilities that can be capitalized on with malicious code.The adversary must be able to place the malicious code on the target system.

## Consequences

- Confidentiality, Integrity, Availability: Execute Unauthorized Commands
- Confidentiality, Integrity, Availability: Other

## Mitigations

- Employ robust cybersecurity training for all employees.
- Implement system antivirus software that scans all attachments before opening them.
- Regularly patch all software.
- Execute all suspicious files in a sandbox environment.

## Source

- [MITRE CAPEC CAPEC-549](https://capec.mitre.org/data/definitions/549.html)
