---
slug: attack-pattern/CAPEC-463
title: "CAPEC-463 — Padding Oracle Crypto Attack"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-463]
cwe_ids: [CWE-209, CWE-347, CWE-354, CWE-514, CWE-649, CWE-696]
related: [weakness/CWE-209, weakness/CWE-347, weakness/CWE-354, weakness/CWE-514, weakness/CWE-649, weakness/CWE-696]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-463
updated_at: 2026-08-31
summary: "An adversary is able to efficiently decrypt data without knowing the decryption key if a target system leaks data on whether or not a padding error happened while decrypting the ciphertext. A target system that leaks this type of information becomes the padding oracle and an adve…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/463.html
---

# CAPEC-463: Padding Oracle Crypto Attack

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary is able to efficiently decrypt data without knowing the decryption key if a target system leaks data on whether or not a padding error happened while decrypting the ciphertext. A target system that leaks this type of information becomes the padding oracle and an adversary is able to make use of that oracle to efficiently decrypt data without knowing the decryption key by issuing on average 128*b calls to the padding oracle (where b is the number of bytes in the ciphertext block). In addition to performing decryption, an adversary is also able to produce valid ciphertexts (i.e., perform encryption) by using the padding oracle, all without knowing the encryption key.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-209](/wiki/p/weakness/CWE-209), [CWE-347](/wiki/p/weakness/CWE-347), [CWE-354](/wiki/p/weakness/CWE-354), [CWE-514](/wiki/p/weakness/CWE-514), [CWE-649](/wiki/p/weakness/CWE-649), [CWE-696](/wiki/p/weakness/CWE-696)

## Prerequisites

- The decryption routine does not properly authenticate the message / does not verify its integrity prior to performing the decryption operation
- The target system leaks data (in some way) on whether a padding error has occurred when attempting to decrypt the ciphertext.
- The padding oracle remains available for enough time / for as many requests as needed for the adversary to decrypt the ciphertext.

## Mitigations

- Design: Use a message authentication code (MAC) or another mechanism to perform verification of message authenticity / integrity prior to decryption
- Implementation: Do not leak information back to the user as to any cryptography (e.g., padding) encountered during decryption.

## Source

- [MITRE CAPEC CAPEC-463](https://capec.mitre.org/data/definitions/463.html)
