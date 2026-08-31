---
slug: attack-pattern/CAPEC-614
title: "CAPEC-614 — Rooting SIM Cards"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-614]
cwe_ids: [CWE-327]
related: [weakness/CWE-327]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-614
updated_at: 2026-08-31
summary: "SIM cards are the de facto trust anchor of mobile devices worldwide. The cards protect the mobile identity of subscribers, associate devices with phone numbers, and increasingly store payment credentials, for example in NFC-enabled phones with mobile wallets. This attack leverage…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/614.html
---

# CAPEC-614: Rooting SIM Cards

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

SIM cards are the de facto trust anchor of mobile devices worldwide. The cards protect the mobile identity of subscribers, associate devices with phone numbers, and increasingly store payment credentials, for example in NFC-enabled phones with mobile wallets. This attack leverages over-the-air (OTA) updates deployed via cryptographically-secured SMS messages to deliver executable code to the SIM. By cracking the DES key, an attacker can send properly signed binary SMS messages to a device, which are treated as Java applets and are executed on the SIM. These applets are allowed to send SMS, change voicemail numbers, and query the phone location, among many other predefined functions. These capabilities alone provide plenty of potential for abuse.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-327](/wiki/p/weakness/CWE-327)

## Prerequisites

- A SIM card that relies on the DES cipher.

## Skills required

- Medium: This is a sophisticated attack, but detailed techniques are published in open literature.

## Consequences

- Confidentiality, Integrity: Execute Unauthorized Commands

## Mitigations

- Upgrade the SIM card to use the state-of-the-art AES or the somewhat outdated 3DES algorithm for OTA.

## Source

- [MITRE CAPEC CAPEC-614](https://capec.mitre.org/data/definitions/614.html)
