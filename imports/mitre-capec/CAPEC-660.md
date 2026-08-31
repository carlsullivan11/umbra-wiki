---
slug: attack-pattern/CAPEC-660
title: "CAPEC-660 — Root/Jailbreak Detection Evasion via Hooking"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-660]
cwe_ids: [CWE-829]
mitre_ids: [T1055]
related: [weakness/CWE-829, technique/T1055]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-660
updated_at: 2026-08-31
summary: "An adversary forces a non-restricted mobile application to load arbitrary code or code files, via Hooking, with the goal of evading Root/Jailbreak detection. Mobile device users often Root/Jailbreak their devices in order to gain administrative control over the mobile operating s…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/660.html
---

# CAPEC-660: Root/Jailbreak Detection Evasion via Hooking

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Very High |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary forces a non-restricted mobile application to load arbitrary code or code files, via Hooking, with the goal of evading Root/Jailbreak detection. Mobile device users often Root/Jailbreak their devices in order to gain administrative control over the mobile operating system and/or to install third-party mobile applications that are not provided by authorized application stores (e.g. Google Play Store and Apple App Store). Adversaries may further leverage these capabilities to escalate privileges or bypass access control on legitimate applications. Although many mobile applications check if a mobile device is Rooted/Jailbroken prior to authorized use of the application, adversaries may be able to "hook" code in order to circumvent these checks. Successfully evading Root/Jailbreak detection allows an adversary to execute administrative commands, obtain confidential data, impersonate legitimate users of the application, and more.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-829](/wiki/p/weakness/CWE-829)

**ATT&CK techniques:** [T1055](/wiki/p/technique/T1055)

## Prerequisites

- The targeted application must be non-restricted to allow code hooking.

## Skills required

- High: Knowledge about Root/Jailbreak detection and evasion techniques.
- Medium: Knowledge about code hooking.

## Consequences

- Integrity, Authorization: Execute Unauthorized Commands
- Confidentiality, Access Control, Authorization: Gain Privileges
- Confidentiality, Access Control: Read Data

## Mitigations

- Ensure mobile applications are signed appropriately to avoid code inclusion via hooking.
- Inspect the application's memory for suspicious artifacts, such as shared objects/JARs or dylibs, after other Root/Jailbreak detection methods.
- Inspect the application's stack trace for suspicious method calls.
- Allow legitimate native methods, and check for non-allowed native methods during Root/Jailbreak detection methods.
- For iOS applications, ensure application methods do not originate from outside of Apple's SDK.

## Source

- [MITRE CAPEC CAPEC-660](https://capec.mitre.org/data/definitions/660.html)
