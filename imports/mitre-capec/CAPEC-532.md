---
slug: attack-pattern/CAPEC-532
title: "CAPEC-532 — Altered Installed BIOS"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-532]
mitre_ids: [T1495, T1542.001]
related: [technique/T1495, technique/T1542.001]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-532
updated_at: 2026-08-31
summary: "An attacker with access to download and update system software sends a maliciously altered BIOS to the victim or victim supplier/integrator, which when installed allows for future exploitation."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/532.html
---

# CAPEC-532: Altered Installed BIOS

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | High |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker with access to download and update system software sends a maliciously altered BIOS to the victim or victim supplier/integrator, which when installed allows for future exploitation.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**ATT&CK techniques:** [T1495](/wiki/p/technique/T1495), [T1542.001](/wiki/p/technique/T1542.001)

## Prerequisites

- Advanced knowledge about the installed target system design.
- Advanced knowledge about the download and update installation processes.
- Access to the download and update system(s) used to deliver BIOS images.

## Skills required

- High: Able to develop a malicious BIOS image with the original functionality as a normal BIOS image, but with added functionality that allows for later compromise and/or disruption.

## Mitigations

- Deploy strong code integrity policies to allow only authorized apps to run.
- Use endpoint detection and response solutions that can automaticalkly detect and remediate suspicious activities.
- Maintain a highly secure build and update infrastructure by immediately applying security patches for OS and software, implementing mandatory integrity controls to ensure only trusted tools run, and requiring multi-factor authentication for admins.
- Require SSL for update channels and implement certificate transparency based verification.
- Sign update packages and BIOS patches.
- Use hardware security modules/trusted platform modules to verify authenticity using hardware-based cryptography.

## Source

- [MITRE CAPEC CAPEC-532](https://capec.mitre.org/data/definitions/532.html)
