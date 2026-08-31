---
slug: attack-pattern/CAPEC-682
title: "CAPEC-682 — Exploitation of Firmware or ROM Code with Unpatchable Vulnerabilities"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-682]
cwe_ids: [CWE-1277, CWE-1310]
related: [weakness/CWE-1277, weakness/CWE-1310]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-682
updated_at: 2026-08-31
summary: "An adversary may exploit vulnerable code (i.e., firmware or ROM) that is unpatchable. Unpatchable devices exist due to manufacturers intentionally or inadvertently designing devices incapable of updating their software. Additionally, with updatable devices, the manufacturer may d…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/682.html
---

# CAPEC-682: Exploitation of Firmware or ROM Code with Unpatchable Vulnerabilities

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary may exploit vulnerable code (i.e., firmware or ROM) that is unpatchable. Unpatchable devices exist due to manufacturers intentionally or inadvertently designing devices incapable of updating their software. Additionally, with updatable devices, the manufacturer may decide not to support the device and stop making updates to their software.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-1277](/wiki/p/weakness/CWE-1277), [CWE-1310](/wiki/p/weakness/CWE-1310)

## Prerequisites

- Awareness of the hardware being leveraged.
- Access to the hardware being leveraged, either physically or remotely.

## Skills required

- Medium: Knowledge of various wireless protocols to enable remote access to vulnerable devices
- High: Ability to identify physical entry points such as debug interfaces if the device is not being accessed remotely

## Consequences

- Integrity: Modify Data
- Confidentiality: Read Data
- Access Control, Authorization: Gain Privileges

## Mitigations

- Design systems and products with the ability to patch firmware or ROM code after deployment to fix vulnerabilities.
- Make use of OTA (Over-the-air) updates so that firmware can be patched remotely either through manual or automatic means

## Source

- [MITRE CAPEC CAPEC-682](https://capec.mitre.org/data/definitions/682.html)
