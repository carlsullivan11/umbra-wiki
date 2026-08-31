---
slug: attack-pattern/CAPEC-478
title: "CAPEC-478 — Modification of Windows Service Configuration"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-478]
cwe_ids: [CWE-284]
mitre_ids: [T1543.003, T1574.011]
related: [weakness/CWE-284, technique/T1543.003, technique/T1574.011]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-478
updated_at: 2026-08-31
summary: "An adversary exploits a weakness in access control to modify the execution parameters of a Windows service. The goal of this attack is to execute a malicious binary in place of an existing service."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/478.html
---

# CAPEC-478: Modification of Windows Service Configuration

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Usable |
| Typical severity | High |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary exploits a weakness in access control to modify the execution parameters of a Windows service. The goal of this attack is to execute a malicious binary in place of an existing service.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-284](/wiki/p/weakness/CWE-284)

**ATT&CK techniques:** [T1543.003](/wiki/p/technique/T1543.003), [T1574.011](/wiki/p/technique/T1574.011)

## Prerequisites

- The adversary must have the capability to write to the Windows Registry on the targeted system.

## Consequences

- Integrity: Execute Unauthorized Commands

## Mitigations

- Ensure proper permissions are set for Registry hives to prevent users from modifying keys for system components that may lead to privilege escalation.

## Source

- [MITRE CAPEC CAPEC-478](https://capec.mitre.org/data/definitions/478.html)
