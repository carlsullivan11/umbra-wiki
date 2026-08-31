---
slug: attack-pattern/CAPEC-485
title: "CAPEC-485 — Signature Spoofing by Key Recreation"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-485]
cwe_ids: [CWE-330]
mitre_ids: [T1552.004]
related: [weakness/CWE-330, technique/T1552.004]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-485
updated_at: 2026-08-31
summary: "An attacker obtains an authoritative or reputable signer's private signature key by exploiting a cryptographic weakness in the signature algorithm or pseudorandom number generation and then uses this key to forge signatures from the original signer to mislead a victim into perfor…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/485.html
---

# CAPEC-485: Signature Spoofing by Key Recreation

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker obtains an authoritative or reputable signer's private signature key by exploiting a cryptographic weakness in the signature algorithm or pseudorandom number generation and then uses this key to forge signatures from the original signer to mislead a victim into performing actions that benefit the attacker.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-330](/wiki/p/weakness/CWE-330)

**ATT&CK techniques:** [T1552.004](/wiki/p/technique/T1552.004)

## Prerequisites

- An authoritative signer is using a weak method of random number generation or weak signing software that causes key leakage or permits key inference.
- An authoritative signer is using a signature algorithm with a direct weakness or with poorly chosen parameters that enable the key to be recovered using signatures from that signer.

## Skills required

- High: Cryptanalysis of signature generation algorithm
- High: Reverse engineering and cryptanalysis of signature generation algorithm implementation and random number generation
- High: Ability to create malformed data blobs and know how to present them directly or indirectly to a victim.

## Mitigations

- Ensure cryptographic elements have been sufficiently tested for weaknesses.

## Source

- [MITRE CAPEC CAPEC-485](https://capec.mitre.org/data/definitions/485.html)
