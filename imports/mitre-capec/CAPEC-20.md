---
slug: attack-pattern/CAPEC-20
title: "CAPEC-20 — Encryption Brute Forcing"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-20]
cwe_ids: [CWE-326, CWE-327, CWE-693, CWE-1204]
related: [weakness/CWE-326, weakness/CWE-327, weakness/CWE-693, weakness/CWE-1204]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-20
updated_at: 2026-08-31
summary: "An attacker, armed with the cipher text and the encryption algorithm used, performs an exhaustive (brute force) search on the key space to determine the key that decrypts the cipher text to obtain the plaintext."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/20.html
---

# CAPEC-20: Encryption Brute Forcing

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Low |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker, armed with the cipher text and the encryption algorithm used, performs an exhaustive (brute force) search on the key space to determine the key that decrypts the cipher text to obtain the plaintext.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-326](/wiki/p/weakness/CWE-326), [CWE-327](/wiki/p/weakness/CWE-327), [CWE-693](/wiki/p/weakness/CWE-693), [CWE-1204](/wiki/p/weakness/CWE-1204)

## Prerequisites

- Ciphertext is known.
- Encryption algorithm and key size are known.

## Skills required

- Low: Brute forcing encryption does not require much skill.

## Consequences

- Confidentiality: Read Data

## Mitigations

- Use commonly accepted algorithms and recommended key sizes. The key size used will depend on how important it is to keep the data confidential and for how long.
- In theory a brute force attack performing an exhaustive key space search will always succeed, so the goal is to have computational security. Moore's law needs to be taken into account that suggests that computing resources double every eighteen months.

## Source

- [MITRE CAPEC CAPEC-20](https://capec.mitre.org/data/definitions/20.html)
