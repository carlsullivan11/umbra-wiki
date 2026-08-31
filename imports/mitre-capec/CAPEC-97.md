---
slug: attack-pattern/CAPEC-97
title: "CAPEC-97 — Cryptanalysis"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-97]
cwe_ids: [CWE-327, CWE-1204, CWE-1240, CWE-1241, CWE-1279]
related: [weakness/CWE-327, weakness/CWE-1204, weakness/CWE-1240, weakness/CWE-1241, weakness/CWE-1279]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-97
updated_at: 2026-08-31
summary: "Cryptanalysis is a process of finding weaknesses in cryptographic algorithms and using these weaknesses to decipher the ciphertext without knowing the secret key (instance deduction). Sometimes the weakness is not in the cryptographic algorithm itself, but rather in how it is app…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/97.html
---

# CAPEC-97: Cryptanalysis

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Very High |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

Cryptanalysis is a process of finding weaknesses in cryptographic algorithms and using these weaknesses to decipher the ciphertext without knowing the secret key (instance deduction). Sometimes the weakness is not in the cryptographic algorithm itself, but rather in how it is applied that makes cryptanalysis successful. An attacker may have other goals as well, such as: Total Break (finding the secret key), Global Deduction (finding a functionally equivalent algorithm for encryption and decryption that does not require knowledge of the secret key), Information Deduction (gaining some information about plaintexts or ciphertexts that was not previously known) and Distinguishing Algorithm (the attacker has the ability to distinguish the output of the encryption (ciphertext) from a random permutation of bits).

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-327](/wiki/p/weakness/CWE-327), [CWE-1204](/wiki/p/weakness/CWE-1204), [CWE-1240](/wiki/p/weakness/CWE-1240), [CWE-1241](/wiki/p/weakness/CWE-1241), [CWE-1279](/wiki/p/weakness/CWE-1279)

## Prerequisites

- The target software utilizes some sort of cryptographic algorithm.
- An underlying weaknesses exists either in the cryptographic algorithm used or in the way that it was applied to a particular chunk of plaintext.
- The encryption algorithm is known to the attacker.
- An attacker has access to the ciphertext.

## Skills required

- High: Cryptanalysis generally requires a very significant level of understanding of mathematics and computation.

## Consequences

- Confidentiality: Read Data

## Mitigations

- Use proven cryptographic algorithms with recommended key sizes.
- Ensure that the algorithms are used properly. That means: 1. Not rolling out your own crypto; Use proven algorithms and implementations. 2. Choosing initialization vectors with sufficiently random numbers 3. Generating key material using good sources of randomness and avoiding known weak keys 4. Using proven protocols and their implementations. 5. Picking the most appropriate cryptographic algorithm for your usage context and data

## Source

- [MITRE CAPEC CAPEC-97](https://capec.mitre.org/data/definitions/97.html)
