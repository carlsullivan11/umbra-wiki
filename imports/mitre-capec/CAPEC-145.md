---
slug: attack-pattern/CAPEC-145
title: "CAPEC-145 — Checksum Spoofing"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-145]
cwe_ids: [CWE-354]
related: [weakness/CWE-354]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-145
updated_at: 2026-08-31
summary: "An adversary spoofs a checksum message for the purpose of making a payload appear to have a valid corresponding checksum. Checksums are used to verify message integrity. They consist of some value based on the value of the message they are protecting. Hash codes are a common chec…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/145.html
---

# CAPEC-145: Checksum Spoofing

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary spoofs a checksum message for the purpose of making a payload appear to have a valid corresponding checksum. Checksums are used to verify message integrity. They consist of some value based on the value of the message they are protecting. Hash codes are a common checksum mechanism. Both the sender and recipient are able to compute the checksum based on the contents of the message. If the message contents change between the sender and recipient, the sender and recipient will compute different checksum values. Since the sender's checksum value is transmitted with the message, the recipient would know that a modification occurred. In checksum spoofing an adversary modifies the message body and then modifies the corresponding checksum so that the recipient's checksum calculation will match the checksum (created by the adversary) in the message. This would prevent the recipient from realizing that a change occurred.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-354](/wiki/p/weakness/CWE-354)

## Prerequisites

- The adversary must be able to intercept a message from the sender (keeping the recipient from getting it), modify it, and send the modified message to the recipient.
- The sender and recipient must use a checksum to protect the integrity of their message and transmit this checksum in a manner where the adversary can intercept and modify it.
- The checksum value must be computable using information known to the adversary. A cryptographic checksum, which uses a key known only to the sender and recipient, would thwart this attack.

## Source

- [MITRE CAPEC CAPEC-145](https://capec.mitre.org/data/definitions/145.html)
