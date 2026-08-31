---
slug: attack-pattern/CAPEC-661
title: "CAPEC-661 — Root/Jailbreak Detection Evasion via Debugging"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-661]
cwe_ids: [CWE-489]
related: [weakness/CWE-489]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-661
updated_at: 2026-08-31
summary: "An adversary inserts a debugger into the program entry point of a mobile application to modify the application binary, with the goal of evading Root/Jailbreak detection. Mobile device users often Root/Jailbreak their devices in order to gain administrative control over the mobile…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/661.html
---

# CAPEC-661: Root/Jailbreak Detection Evasion via Debugging

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Very High |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary inserts a debugger into the program entry point of a mobile application to modify the application binary, with the goal of evading Root/Jailbreak detection. Mobile device users often Root/Jailbreak their devices in order to gain administrative control over the mobile operating system and/or to install third-party mobile applications that are not provided by authorized application stores (e.g. Google Play Store and Apple App Store). Rooting/Jailbreaking a mobile device also provides users with access to system debuggers and disassemblers, which can be leveraged to exploit applications by dumping the application's memory at runtime in order to remove or bypass signature verification methods. This further allows the adversary to evade Root/Jailbreak detection mechanisms, which can result in execution of administrative commands, obtaining confidential data, impersonating legitimate users of the application, and more.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-489](/wiki/p/weakness/CWE-489)

## Prerequisites

- A debugger must be able to be inserted into the targeted application.

## Skills required

- High: Knowledge about Root/Jailbreak detection and evasion techniques.
- Medium: Knowledge about runtime debugging.

## Consequences

- Integrity, Authorization: Execute Unauthorized Commands
- Confidentiality, Access Control, Authorization: Gain Privileges
- Confidentiality, Access Control: Read Data

## Mitigations

- Instantiate checks within the application code that ensures debuggers are not attached.

## Source

- [MITRE CAPEC CAPEC-661](https://capec.mitre.org/data/definitions/661.html)
