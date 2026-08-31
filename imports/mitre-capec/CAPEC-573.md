---
slug: attack-pattern/CAPEC-573
title: "CAPEC-573 — Process Footprinting"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-573]
cwe_ids: [CWE-200]
mitre_ids: [T1057]
related: [weakness/CWE-200, technique/T1057]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-573
updated_at: 2026-08-31
summary: "An adversary exploits functionality meant to identify information about the currently running processes on the target system to an authorized user. By knowing what processes are running on the target system, the adversary can learn about the target environment as a means towards …"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/573.html
---

# CAPEC-573: Process Footprinting

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Low |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary exploits functionality meant to identify information about the currently running processes on the target system to an authorized user. By knowing what processes are running on the target system, the adversary can learn about the target environment as a means towards further malicious behavior.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-200](/wiki/p/weakness/CWE-200)

**ATT&CK techniques:** [T1057](/wiki/p/technique/T1057)

## Prerequisites

- The adversary must have gained access to the target system via physical or logical means in order to carry out this attack.

## Consequences

- Confidentiality: Other
- Confidentiality, Access Control, Authorization: Bypass Protection Mechanism, Hide Activities

## Mitigations

- Identify programs that may be used to acquire process information and block them by using a software restriction policy or tools that restrict program execution by using a process allowlist.

## Source

- [MITRE CAPEC CAPEC-573](https://capec.mitre.org/data/definitions/573.html)
