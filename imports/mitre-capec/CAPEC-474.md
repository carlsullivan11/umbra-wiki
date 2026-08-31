---
slug: attack-pattern/CAPEC-474
title: "CAPEC-474 — Signature Spoofing by Key Theft"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-474]
cwe_ids: [CWE-522]
mitre_ids: [T1552.004]
related: [weakness/CWE-522, technique/T1552.004]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-474
updated_at: 2026-08-31
summary: "An attacker obtains an authoritative or reputable signer's private signature key by theft and then uses this key to forge signatures from the original signer to mislead a victim into performing actions that benefit the attacker."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/474.html
---

# CAPEC-474: Signature Spoofing by Key Theft

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker obtains an authoritative or reputable signer's private signature key by theft and then uses this key to forge signatures from the original signer to mislead a victim into performing actions that benefit the attacker.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-522](/wiki/p/weakness/CWE-522)

**ATT&CK techniques:** [T1552.004](/wiki/p/technique/T1552.004)

## Prerequisites

- An authoritative or reputable signer is storing their private signature key with insufficient protection.

## Skills required

- Low: Knowledge of common location methods and access methods to sensitive data
- High: Ability to compromise systems containing sensitive data

## Mitigations

- Restrict access to private keys from non-supervisory accounts
- Restrict access to administrative personnel and processes only
- Ensure all remote methods are secured
- Ensure all services are patched and up to date

## Source

- [MITRE CAPEC CAPEC-474](https://capec.mitre.org/data/definitions/474.html)
