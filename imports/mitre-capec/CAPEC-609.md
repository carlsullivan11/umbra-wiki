---
slug: attack-pattern/CAPEC-609
title: "CAPEC-609 — Cellular Traffic Intercept"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-609]
cwe_ids: [CWE-311]
mitre_ids: [T1111]
related: [weakness/CWE-311, technique/T1111]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-609
updated_at: 2026-08-31
summary: "Cellular traffic for voice and data from mobile devices and retransmission devices can be intercepted via numerous methods. Malicious actors can deploy their own cellular tower equipment and intercept cellular traffic surreptitiously. Additionally, government agencies of adversar…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/609.html
---

# CAPEC-609: Cellular Traffic Intercept

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Low |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

Cellular traffic for voice and data from mobile devices and retransmission devices can be intercepted via numerous methods. Malicious actors can deploy their own cellular tower equipment and intercept cellular traffic surreptitiously. Additionally, government agencies of adversaries and malicious actors can intercept cellular traffic via the telecommunications backbone over which mobile traffic is transmitted.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-311](/wiki/p/weakness/CWE-311)

**ATT&CK techniques:** [T1111](/wiki/p/technique/T1111)

## Prerequisites

- None

## Skills required

- Medium: Adversaries can purchase hardware and software solutions, or create their own solutions, to capture/intercept cellular radio traffic. The cost of a basic Base Transceiver Station (BTS) to broadcast to local mobile cellular radios in mobile devices has dropped to very affordable costs. The ability of commercial cellular providers to monitor for "rogue" BTS stations is poor in many areas and it is assumed that "rogue" BTS stations exist in urban areas.

## Consequences

- Confidentiality: Read Data

## Mitigations

- Encryption of all data packets emanating from the smartphone to a retransmission device via two encrypted tunnels with Suite B cryptography, all the way to the VPN gateway at the datacenter.

## Source

- [MITRE CAPEC CAPEC-609](https://capec.mitre.org/data/definitions/609.html)
