---
slug: attack-pattern/CAPEC-75
title: "CAPEC-75 — Manipulating Writeable Configuration Files"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-75]
cwe_ids: [CWE-77, CWE-99, CWE-346, CWE-349, CWE-353, CWE-354]
related: [weakness/CWE-77, weakness/CWE-99, weakness/CWE-346, weakness/CWE-349, weakness/CWE-353, weakness/CWE-354]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-75
updated_at: 2026-08-31
summary: "Generally these are manually edited files that are not in the preview of the system administrators, any ability on the attackers' behalf to modify these files, for example in a CVS repository, gives unauthorized access directly to the application, the same as authorized users."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/75.html
---

# CAPEC-75: Manipulating Writeable Configuration Files

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Very High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

Generally these are manually edited files that are not in the preview of the system administrators, any ability on the attackers' behalf to modify these files, for example in a CVS repository, gives unauthorized access directly to the application, the same as authorized users.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-77](/wiki/p/weakness/CWE-77), [CWE-99](/wiki/p/weakness/CWE-99), [CWE-346](/wiki/p/weakness/CWE-346), [CWE-349](/wiki/p/weakness/CWE-349), [CWE-353](/wiki/p/weakness/CWE-353), [CWE-354](/wiki/p/weakness/CWE-354)

## Prerequisites

- Configuration files must be modifiable by the attacker

## Skills required

- Medium: To identify vulnerable configuration files, and understand how to manipulate servers and erase forensic evidence

## Consequences

- Confidentiality, Access Control, Authorization: Gain Privileges

## Mitigations

- Design: Enforce principle of least privilege
- Design: Backup copies of all configuration files
- Implementation: Integrity monitoring for configuration files
- Implementation: Enforce audit logging on code and configuration promotion procedures.
- Implementation: Load configuration from separate process and memory space, for example a separate physical device like a CD

## Source

- [MITRE CAPEC CAPEC-75](https://capec.mitre.org/data/definitions/75.html)
