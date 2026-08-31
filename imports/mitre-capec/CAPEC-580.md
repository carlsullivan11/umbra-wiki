---
slug: attack-pattern/CAPEC-580
title: "CAPEC-580 — System Footprinting"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-580]
cwe_ids: [CWE-204, CWE-205, CWE-208]
mitre_ids: [T1082]
related: [weakness/CWE-204, weakness/CWE-205, weakness/CWE-208, technique/T1082]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-580
updated_at: 2026-08-31
summary: "An adversary engages in active probing and exploration activities to determine security information about a remote target system. Often times adversaries will rely on remote applications that can be probed for system configurations."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/580.html
---

# CAPEC-580: System Footprinting

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Low |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary engages in active probing and exploration activities to determine security information about a remote target system. Often times adversaries will rely on remote applications that can be probed for system configurations.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-204](/wiki/p/weakness/CWE-204), [CWE-205](/wiki/p/weakness/CWE-205), [CWE-208](/wiki/p/weakness/CWE-208)

**ATT&CK techniques:** [T1082](/wiki/p/technique/T1082)

## Prerequisites

- The adversary must have logical access to the target network and system.

## Skills required

- Low: The adversary needs to know basic linux commands.

## Consequences

- Confidentiality: Read Data

## Mitigations

- Keep patches up to date by installing weekly or daily if possible.
- Identify programs that may be used to acquire peripheral information and block them by using a software restriction policy or tools that restrict program execution by using a process allowlist.

## Source

- [MITRE CAPEC CAPEC-580](https://capec.mitre.org/data/definitions/580.html)
