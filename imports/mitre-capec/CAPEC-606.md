---
slug: attack-pattern/CAPEC-606
title: "CAPEC-606 — Weakening of Cellular Encryption"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-606]
cwe_ids: [CWE-757]
related: [weakness/CWE-757]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-606
updated_at: 2026-08-31
summary: "An attacker, with control of a Cellular Rogue Base Station or through cooperation with a Malicious Mobile Network Operator can force the mobile device (e.g., the retransmission device) to use no encryption (A5/0 mode) or to use easily breakable encryption (A5/1 or A5/2 mode)."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/606.html
---

# CAPEC-606: Weakening of Cellular Encryption

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker, with control of a Cellular Rogue Base Station or through cooperation with a Malicious Mobile Network Operator can force the mobile device (e.g., the retransmission device) to use no encryption (A5/0 mode) or to use easily breakable encryption (A5/1 or A5/2 mode).

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-757](/wiki/p/weakness/CWE-757)

## Prerequisites

- Cellular devices that allow negotiating security modes to facilitate backwards compatibility and roaming on legacy networks.

## Skills required

- Medium: Adversaries can purchase and implement rogue BTS stations at a cost effective rate, and can push a mobile device to downgrade to a non-secure cellular protocol like 2G over GSM or CDMA.

## Consequences

- Confidentiality: Other

## Mitigations

- Use of hardened baseband firmware on retransmission device to detect and prevent the use of weak cellular encryption.
- Monitor cellular RF interface to detect the usage of weaker-than-expected cellular encryption.

## Source

- [MITRE CAPEC CAPEC-606](https://capec.mitre.org/data/definitions/606.html)
