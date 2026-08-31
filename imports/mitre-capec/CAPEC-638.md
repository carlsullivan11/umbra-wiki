---
slug: attack-pattern/CAPEC-638
title: "CAPEC-638 — Altered Component Firmware"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-638]
mitre_ids: [T1542.002]
related: [technique/T1542.002]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-638
updated_at: 2026-08-31
summary: "An adversary exploits systems features and/or improperly protected firmware of hardware components, such as Hard Disk Drives (HDD), with the goal of executing malicious code from within the component's Master Boot Record (MBR). Conducting this type of attack entails the adversary…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/638.html
---

# CAPEC-638: Altered Component Firmware

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Very High |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary exploits systems features and/or improperly protected firmware of hardware components, such as Hard Disk Drives (HDD), with the goal of executing malicious code from within the component's Master Boot Record (MBR). Conducting this type of attack entails the adversary infecting the target with firmware altering malware, using known tools, and a payload. Once this malware is executed, the MBR is modified to include instructions to execute the payload at desired intervals and when the system is booted up. A successful attack will obtain persistence within the victim system even if the operating system is reinstalled and/or if the component is formatted or has its data erased.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**ATT&CK techniques:** [T1542.002](/wiki/p/technique/T1542.002)

## Prerequisites

- Advanced knowledge about the target component's firmware
- Advanced knowledge about Master Boot Records (MBR)
- Advanced knowledge about tools used to insert firmware altering malware.
- Advanced knowledge about component shipments to the target organization.

## Skills required

- High: Ability to access and reverse engineer hardware component firmware.
- High: Ability to intercept components in transit.
- Medium: Ability to create malicious payload to be executed from MBR.
- Low: Ability to leverage known malware tools to infect target system and insert firmware altering malware/payload

## Consequences

- Authentication, Authorization: Gain Privileges, Execute Unauthorized Commands, Bypass Protection Mechanism, Hide Activities
- Confidentiality, Access Control: Read Data, Modify Data

## Mitigations

- Leverage hardware components known to not be susceptible to these types of attacks.
- Implement hardware RAID infrastructure.

## Source

- [MITRE CAPEC CAPEC-638](https://capec.mitre.org/data/definitions/638.html)
