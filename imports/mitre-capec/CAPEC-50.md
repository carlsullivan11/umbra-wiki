---
slug: attack-pattern/CAPEC-50
title: "CAPEC-50 — Password Recovery Exploitation"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-50]
cwe_ids: [CWE-522, CWE-640]
related: [weakness/CWE-522, weakness/CWE-640]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-50
updated_at: 2026-08-31
summary: "An attacker may take advantage of the application feature to help users recover their forgotten passwords in order to gain access into the system with the same privileges as the original user. Generally password recovery schemes tend to be weak and insecure."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/50.html
---

# CAPEC-50: Password Recovery Exploitation

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker may take advantage of the application feature to help users recover their forgotten passwords in order to gain access into the system with the same privileges as the original user. Generally password recovery schemes tend to be weak and insecure.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-522](/wiki/p/weakness/CWE-522), [CWE-640](/wiki/p/weakness/CWE-640)

## Prerequisites

- The system allows users to recover their passwords and gain access back into the system.
- Password recovery mechanism has been designed or implemented insecurely.
- Password recovery mechanism relies only on something the user knows and not something the user has.
- No third party intervention is required to use the password recovery mechanism.

## Skills required

- Low: Brute force attack
- Medium: Social engineering and more sophisticated technical attacks.

## Consequences

- Confidentiality, Access Control, Authorization: Gain Privileges

## Mitigations

- Use multiple security questions (e.g. have three and make the user answer two of them correctly). Let the user select their own security questions or provide them with choices of questions that are not generic.
- E-mail the temporary password to the registered e-mail address of the user rather than letting the user reset the password online.
- Ensure that your password recovery functionality is not vulnerable to an injection style attack.

## Source

- [MITRE CAPEC CAPEC-50](https://capec.mitre.org/data/definitions/50.html)
