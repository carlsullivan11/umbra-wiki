---
slug: attack-pattern/CAPEC-634
title: "CAPEC-634 — Probe Audio and Video Peripherals"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-634]
cwe_ids: [CWE-267]
mitre_ids: [T1123, T1125]
related: [weakness/CWE-267, technique/T1123, technique/T1125]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-634
updated_at: 2026-08-31
summary: "The adversary exploits the target system's audio and video functionalities through malware or scheduled tasks. The goal is to capture sensitive information about the target for financial, personal, political, or other gains which is accomplished by collecting communication data b…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/634.html
---

# CAPEC-634: Probe Audio and Video Peripherals

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | High |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

The adversary exploits the target system's audio and video functionalities through malware or scheduled tasks. The goal is to capture sensitive information about the target for financial, personal, political, or other gains which is accomplished by collecting communication data between two parties via the use of peripheral devices (e.g. microphones and webcams) or applications with audio and video capabilities (e.g. Skype) on a system.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-267](/wiki/p/weakness/CWE-267)

**ATT&CK techniques:** [T1123](/wiki/p/technique/T1123), [T1125](/wiki/p/technique/T1125)

## Prerequisites

- Knowledge of the target device's or application’s vulnerabilities that can be capitalized on with malicious code. The adversary must be able to place the malicious code on the target device.

## Skills required

- High: To deploy a hidden process or malware on the system to automatically collect audio and video data.

## Consequences

- Confidentiality: Read Data

## Mitigations

- Prevent unknown code from executing on a system through the use of an allowlist policy.
- Patch installed applications as soon as new updates become available.

## Source

- [MITRE CAPEC CAPEC-634](https://capec.mitre.org/data/definitions/634.html)
