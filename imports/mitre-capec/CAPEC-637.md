---
slug: attack-pattern/CAPEC-637
title: "CAPEC-637 — Collect Data from Clipboard"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-637]
cwe_ids: [CWE-267]
mitre_ids: [T1115]
related: [weakness/CWE-267, technique/T1115]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-637
updated_at: 2026-08-31
summary: "The adversary exploits an application that allows for the copying of sensitive data or information by collecting information copied to the clipboard. Data copied to the clipboard can be accessed by other applications, such as malware built to exfiltrate or log clipboard contents …"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/637.html
---

# CAPEC-637: Collect Data from Clipboard

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Low |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

The adversary exploits an application that allows for the copying of sensitive data or information by collecting information copied to the clipboard. Data copied to the clipboard can be accessed by other applications, such as malware built to exfiltrate or log clipboard contents on a periodic basis. In this way, the adversary aims to garner information to which they are unauthorized.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-267](/wiki/p/weakness/CWE-267)

**ATT&CK techniques:** [T1115](/wiki/p/technique/T1115)

## Prerequisites

- The adversary must have a means (i.e., a pre-installed tool or background process) by which to collect data from the clipboard and store it. That is, when the target copies data to the clipboard (e.g., to paste into another application), the adversary needs some means of capturing that data in a third location.

## Skills required

- High: To deploy a hidden process or malware on the system to automatically collect clipboard data.

## Consequences

- Confidentiality: Read Data

## Mitigations

- While copying and pasting of data with the clipboard is a legitimate and practical function, certain situations and context may require the disabling of this feature. Just as certain applications disable screenshot capability, applications that handle highly sensitive information should consider disabling copy and paste functionality.
- Employ a robust identification and audit/blocking via using an allowlist of applications on your system. Malware may contain the functionality associated with this attack pattern.

## Source

- [MITRE CAPEC CAPEC-637](https://capec.mitre.org/data/definitions/637.html)
