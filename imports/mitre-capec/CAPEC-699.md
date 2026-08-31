---
slug: attack-pattern/CAPEC-699
title: "CAPEC-699 — Eavesdropping on a Monitor"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-699]
cwe_ids: [CWE-1300]
related: [weakness/CWE-1300]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-699
updated_at: 2026-08-31
summary: "An Adversary can eavesdrop on the content of an external monitor through the air without modifying any cable or installing software, just capturing this signal emitted by the cable or video port, with this the attacker will be able to impact the confidentiality of the data withou…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/699.html
---

# CAPEC-699: Eavesdropping on a Monitor

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An Adversary can eavesdrop on the content of an external monitor through the air without modifying any cable or installing software, just capturing this signal emitted by the cable or video port, with this the attacker will be able to impact the confidentiality of the data without being detected by traditional security tools

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-1300](/wiki/p/weakness/CWE-1300)

## Prerequisites

- Victim should use an external monitor device
- Physical access to the target location and devices

## Skills required

- Medium: Knowledge of how to use the SDR and related software: With this knowledge, the adversary will find the correct frequency where the signal is being leaked
- Low: Understanding of computing hardware, to identify the video cable and video ports

## Consequences

- Confidentiality: Read Data

## Mitigations

- Enhance: Increase the number of electromagnetic shield layers in the display ports and cables to contain or reduce the intensity of the leaked signal.
- Implement: Use a protocol that encrypts the video signal; in case the signal is intercepted the signal is protected by the encryption.
- Design: Lock away the video cables, making it difficult for the attacker to access the cables and place the antenna near them (If the distance condition between the antenna and display port/cable is not satisfied, the attack will not be possible).
- Implement: Use wireless technologies to connect to external display devices.

## Source

- [MITRE CAPEC CAPEC-699](https://capec.mitre.org/data/definitions/699.html)
