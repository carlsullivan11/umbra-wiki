---
slug: attack-pattern/CAPEC-646
title: "CAPEC-646 — Peripheral Footprinting"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-646]
cwe_ids: [CWE-200]
mitre_ids: [T1120]
related: [weakness/CWE-200, technique/T1120]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-646
updated_at: 2026-08-31
summary: "Adversaries may attempt to obtain information about attached peripheral devices and components connected to a computer system. Examples may include discovering the presence of iOS devices by searching for backups, analyzing the Windows registry to determine what USB devices have …"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/646.html
---

# CAPEC-646: Peripheral Footprinting

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Medium |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

Adversaries may attempt to obtain information about attached peripheral devices and components connected to a computer system. Examples may include discovering the presence of iOS devices by searching for backups, analyzing the Windows registry to determine what USB devices have been connected, or infecting a victim system with malware to report when a USB device has been connected. This may allow the adversary to gain additional insight about the system or network environment, which may be useful in constructing further attacks.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-200](/wiki/p/weakness/CWE-200)

**ATT&CK techniques:** [T1120](/wiki/p/technique/T1120)

## Prerequisites

- The adversary needs either physical or remote access to the victim system.

## Skills required

- Medium: The adversary needs to be able to infect the victim system in a manner that gives them remote access.
- Medium: If analyzing the Windows registry, the adversary must understand the registry structure to know where to look for devices.

## Mitigations

- Identify programs that may be used to acquire peripheral information and block them by using a software restriction policy or tools that restrict program execution by using a process allowlist.

## Source

- [MITRE CAPEC CAPEC-646](https://capec.mitre.org/data/definitions/646.html)
