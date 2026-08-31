---
slug: attack-pattern/CAPEC-475
title: "CAPEC-475 — Signature Spoofing by Improper Validation"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-475]
cwe_ids: [CWE-295, CWE-327, CWE-347]
related: [weakness/CWE-295, weakness/CWE-327, weakness/CWE-347]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-475
updated_at: 2026-08-31
summary: "An adversary exploits a cryptographic weakness in the signature verification algorithm implementation to generate a valid signature without knowing the key."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/475.html
---

# CAPEC-475: Signature Spoofing by Improper Validation

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary exploits a cryptographic weakness in the signature verification algorithm implementation to generate a valid signature without knowing the key.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-295](/wiki/p/weakness/CWE-295), [CWE-327](/wiki/p/weakness/CWE-327), [CWE-347](/wiki/p/weakness/CWE-347)

## Prerequisites

- Recipient is using a weak cryptographic signature verification algorithm or a weak implementation of a cryptographic signature verification algorithm, or the configuration of the recipient's application accepts the use of keys generated using cryptographically weak signature verification algorithms.

## Skills required

- High: Cryptanalysis of signature verification algorithm
- High: Reverse engineering and cryptanalysis of signature verification algorithm implementation

## Mitigations

- Use programs and products that contain cryptographic elements that have been thoroughly tested for flaws in the signature verification routines.

## Source

- [MITRE CAPEC CAPEC-475](https://capec.mitre.org/data/definitions/475.html)
