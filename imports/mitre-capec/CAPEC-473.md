---
slug: attack-pattern/CAPEC-473
title: "CAPEC-473 — Signature Spoof"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-473]
cwe_ids: [CWE-20, CWE-290, CWE-327]
mitre_ids: [T1036.001, T1553.002]
related: [weakness/CWE-20, weakness/CWE-290, weakness/CWE-327, technique/T1036.001, technique/T1553.002]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-473
updated_at: 2026-08-31
summary: "An attacker generates a message or datablock that causes the recipient to believe that the message or datablock was generated and cryptographically signed by an authoritative or reputable source, misleading a victim or victim operating system into performing malicious actions."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/473.html
---

# CAPEC-473: Signature Spoof

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | — |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker generates a message or datablock that causes the recipient to believe that the message or datablock was generated and cryptographically signed by an authoritative or reputable source, misleading a victim or victim operating system into performing malicious actions.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-20](/wiki/p/weakness/CWE-20), [CWE-290](/wiki/p/weakness/CWE-290), [CWE-327](/wiki/p/weakness/CWE-327)

**ATT&CK techniques:** [T1036.001](/wiki/p/technique/T1036.001), [T1553.002](/wiki/p/technique/T1553.002)

## Prerequisites

- The victim or victim system is dependent upon a cryptographic signature-based verification system for validation of one or more security events or actions.
- The validation can be bypassed via an attacker-provided signature that makes it appear that the legitimate authoritative or reputable source provided the signature.

## Skills required

- High: Technical understanding of how signature verification algorithms work with data and applications

## Consequences

- Access Control, Authentication: Gain Privileges

## Source

- [MITRE CAPEC CAPEC-473](https://capec.mitre.org/data/definitions/473.html)
