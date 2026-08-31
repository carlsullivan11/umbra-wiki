---
slug: attack-pattern/CAPEC-40
title: "CAPEC-40 — Manipulating Writeable Terminal Devices"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-40]
cwe_ids: [CWE-77]
related: [weakness/CWE-77]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-40
updated_at: 2026-08-31
summary: "This attack exploits terminal devices that allow themselves to be written to by other users. The attacker sends command strings to the target terminal device hoping that the target user will hit enter and thereby execute the malicious command with their privileges. The attacker c…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/40.html
---

# CAPEC-40: Manipulating Writeable Terminal Devices

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Very High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

This attack exploits terminal devices that allow themselves to be written to by other users. The attacker sends command strings to the target terminal device hoping that the target user will hit enter and thereby execute the malicious command with their privileges. The attacker can send the results (such as copying /etc/passwd) to a known directory and collect once the attack has succeeded.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-77](/wiki/p/weakness/CWE-77)

## Prerequisites

- User terminals must have a permissive access control such as world writeable that allows normal users to control data on other user's terminals.

## Skills required

- Low: Ability to discover permissions on terminal devices. Of course, brute force can also be used.

## Consequences

- Confidentiality, Access Control, Authorization: Gain Privileges
- Confidentiality: Read Data
- Confidentiality, Integrity, Availability: Execute Unauthorized Commands

## Mitigations

- Design: Ensure that terminals are only writeable by named owner user and/or administrator
- Design: Enforce principle of least privilege

## Source

- [MITRE CAPEC CAPEC-40](https://capec.mitre.org/data/definitions/40.html)
