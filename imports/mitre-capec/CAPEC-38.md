---
slug: attack-pattern/CAPEC-38
title: "CAPEC-38 — Leveraging/Manipulating Configuration File Search Paths"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-38]
cwe_ids: [CWE-426, CWE-427]
mitre_ids: [T1574.007, T1574.009]
related: [weakness/CWE-426, weakness/CWE-427, technique/T1574.007, technique/T1574.009]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-38
updated_at: 2026-08-31
summary: "This pattern of attack sees an adversary load a malicious resource into a program's standard path so that when a known command is executed then the system instead executes the malicious component. The adversary can either modify the search path a program uses, like a PATH variabl…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/38.html
---

# CAPEC-38: Leveraging/Manipulating Configuration File Search Paths

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Very High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

This pattern of attack sees an adversary load a malicious resource into a program's standard path so that when a known command is executed then the system instead executes the malicious component. The adversary can either modify the search path a program uses, like a PATH variable or classpath, or they can manipulate resources on the path to point to their malicious components. J2EE applications and other component based applications that are built from multiple binaries can have very long list of dependencies to execute. If one of these libraries and/or references is controllable by the attacker then application controls can be circumvented by the attacker.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-426](/wiki/p/weakness/CWE-426), [CWE-427](/wiki/p/weakness/CWE-427)

**ATT&CK techniques:** [T1574.007](/wiki/p/technique/T1574.007), [T1574.009](/wiki/p/technique/T1574.009)

## Prerequisites

- The attacker must be able to write to redirect search paths on the victim host.

## Skills required

- Low: To identify and execute against an over-privileged system interface

## Consequences

- Confidentiality, Integrity, Availability: Execute Unauthorized Commands
- Confidentiality, Access Control, Authorization: Gain Privileges

## Mitigations

- Design: Enforce principle of least privilege
- Design: Ensure that the program's compound parts, including all system dependencies, classpath, path, and so on, are secured to the same or higher level assurance as the program
- Implementation: Host integrity monitoring

## Source

- [MITRE CAPEC CAPEC-38](https://capec.mitre.org/data/definitions/38.html)
