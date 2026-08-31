---
slug: attack-pattern/CAPEC-643
title: "CAPEC-643 — Identify Shared Files/Directories on System"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-643]
cwe_ids: [CWE-200, CWE-267]
mitre_ids: [T1135]
related: [weakness/CWE-200, weakness/CWE-267, technique/T1135]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-643
updated_at: 2026-08-31
summary: "An adversary discovers connections between systems by exploiting the target system's standard practice of revealing them in searchable, common areas. Through the identification of shared folders/drives between systems, the adversary may further their goals of locating and collect…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/643.html
---

# CAPEC-643: Identify Shared Files/Directories on System

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary discovers connections between systems by exploiting the target system's standard practice of revealing them in searchable, common areas. Through the identification of shared folders/drives between systems, the adversary may further their goals of locating and collecting sensitive information/files, or map potential routes for lateral movement within the network.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-200](/wiki/p/weakness/CWE-200), [CWE-267](/wiki/p/weakness/CWE-267)

**ATT&CK techniques:** [T1135](/wiki/p/technique/T1135)

## Prerequisites

- The adversary must have obtained logical access to the system by some means (e.g., via obtained credentials or planting malware on the system).

## Skills required

- Low: Once the adversary has logical access (which can potentially require high knowledge and skill level), the adversary needs only the capability and facility to navigate the system through the OS graphical user interface or the command line. The adversary, or their malware, can simply employ a set of commands that search for shared drives on the system (e.g., net view \\remote system or net share).

## Consequences

- Confidentiality: Read Data

## Mitigations

- Identify unnecessary system utilities or potentially malicious software that may contain functionality to identify network share information, and audit and/or block them by using allowlist tools.

## Source

- [MITRE CAPEC CAPEC-643](https://capec.mitre.org/data/definitions/643.html)
