---
slug: attack-pattern/CAPEC-459
title: "CAPEC-459 — Creating a Rogue Certification Authority Certificate"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-459]
cwe_ids: [CWE-290, CWE-295, CWE-327]
related: [weakness/CWE-290, weakness/CWE-295, weakness/CWE-327]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-459
updated_at: 2026-08-31
summary: "An adversary exploits a weakness resulting from using a hashing algorithm with weak collision resistance to generate certificate signing requests (CSR) that contain collision blocks in their 'to be signed' parts. The adversary submits one CSR to be signed by a trusted certificate…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/459.html
---

# CAPEC-459: Creating a Rogue Certification Authority Certificate

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Very High |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary exploits a weakness resulting from using a hashing algorithm with weak collision resistance to generate certificate signing requests (CSR) that contain collision blocks in their "to be signed" parts. The adversary submits one CSR to be signed by a trusted certificate authority then uses the signed blob to make a second certificate appear signed by said certificate authority. Due to the hash collision, both certificates, though different, hash to the same value and so the signed blob works just as well in the second certificate. The net effect is that the adversary's second X.509 certificate, which the Certification Authority has never seen, is now signed and validated by that Certification Authority.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-290](/wiki/p/weakness/CWE-290), [CWE-295](/wiki/p/weakness/CWE-295), [CWE-327](/wiki/p/weakness/CWE-327)

## Prerequisites

- Certification Authority is using a hash function with insufficient collision resistance to generate the certificate hash to be signed

## Skills required

- High: Understanding of how to force a hash collision in X.509 certificates
- High: An attacker must be able to craft two X.509 certificates that produce the same hash value
- Medium: Knowledge needed to set up a certification authority

## Consequences

- Access Control, Authentication: Gain Privileges

## Mitigations

- Certification Authorities need to stop using deprecated or cryptographically insecure hashing algorithms to hash the certificates that they are about to sign. Instead they should be using stronger hashing functions such as SHA-256 or SHA-512.

## Source

- [MITRE CAPEC CAPEC-459](https://capec.mitre.org/data/definitions/459.html)
