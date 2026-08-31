---
slug: attack-pattern/CAPEC-476
title: "CAPEC-476 — Signature Spoofing by Misrepresentation"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-476]
cwe_ids: [CWE-290]
related: [weakness/CWE-290]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-476
updated_at: 2026-08-31
summary: "An attacker exploits a weakness in the parsing or display code of the recipient software to generate a data blob containing a supposedly valid signature, but the signer's identity is falsely represented, which can lead to the attacker manipulating the recipient software or its vi…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/476.html
---

# CAPEC-476: Signature Spoofing by Misrepresentation

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker exploits a weakness in the parsing or display code of the recipient software to generate a data blob containing a supposedly valid signature, but the signer's identity is falsely represented, which can lead to the attacker manipulating the recipient software or its victim user to perform compromising actions.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-290](/wiki/p/weakness/CWE-290)

## Prerequisites

- Recipient is using signature verification software that does not clearly indicate potential homographs in the signer identity.Recipient is using signature verification software that contains a parsing vulnerability, or allows control characters in the signer identity field, such that a signature is mistakenly displayed as valid and from a known or authoritative signer.

## Skills required

- High: Attacker needs to understand the layout and composition of data blobs used by the target application.
- High: To discover a specific vulnerability, attacker needs to reverse engineer signature parsing, signature verification and signer representation code.
- High: Attacker may be required to create malformed data blobs and know how to insert them in a location that the recipient will visit.

## Mitigations

- Ensure the application is using parsing and data display techniques that will accurately display control characters, international symbols and markings, and ultimately recognize potential homograph attacks.

## Source

- [MITRE CAPEC CAPEC-476](https://capec.mitre.org/data/definitions/476.html)
