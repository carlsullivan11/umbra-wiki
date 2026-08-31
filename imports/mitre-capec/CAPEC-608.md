---
slug: attack-pattern/CAPEC-608
title: "CAPEC-608 — Cryptanalysis of Cellular Encryption"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-608]
cwe_ids: [CWE-327]
related: [weakness/CWE-327]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-608
updated_at: 2026-08-31
summary: "The use of cryptanalytic techniques to derive cryptographic keys or otherwise effectively defeat cellular encryption to reveal traffic content. Some cellular encryption algorithms such as A5/1 and A5/2 (specified for GSM use) are known to be vulnerable to such attacks and commerc…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/608.html
---

# CAPEC-608: Cryptanalysis of Cellular Encryption

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

The use of cryptanalytic techniques to derive cryptographic keys or otherwise effectively defeat cellular encryption to reveal traffic content. Some cellular encryption algorithms such as A5/1 and A5/2 (specified for GSM use) are known to be vulnerable to such attacks and commercial tools are available to execute these attacks and decrypt mobile phone conversations in real-time. Newer encryption algorithms in use by UMTS and LTE are stronger and currently believed to be less vulnerable to these types of attacks. Note, however, that an attacker with a Cellular Rogue Base Station can force the use of weak cellular encryption even by newer mobile devices.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-327](/wiki/p/weakness/CWE-327)

## Prerequisites

- None

## Skills required

- Medium: Adversaries can rent commercial supercomputer time globally to conduct cryptanalysis on encrypted data captured from mobile devices. Foreign governments have their own cryptanalysis technology and capabilities. Commercial cellular standards for encryption (GSM and CDMA) are also subject to adversary cryptanalysis.

## Consequences

- Confidentiality: Other

## Mitigations

- Use of hardened baseband firmware on retransmission device to detect and prevent the use of weak cellular encryption.
- Monitor cellular RF interface to detect the usage of weaker-than-expected cellular encryption.

## Source

- [MITRE CAPEC CAPEC-608](https://capec.mitre.org/data/definitions/608.html)
