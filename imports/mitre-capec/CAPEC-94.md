---
slug: attack-pattern/CAPEC-94
title: "CAPEC-94 — Adversary in the Middle (AiTM)"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-94]
cwe_ids: [CWE-287, CWE-290, CWE-294, CWE-300, CWE-593]
mitre_ids: [T1557]
related: [weakness/CWE-287, weakness/CWE-290, weakness/CWE-294, weakness/CWE-300, weakness/CWE-593, technique/T1557]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-94
updated_at: 2026-08-31
summary: "An adversary targets the communication between two components (typically client and server), in order to alter or obtain data from transactions. A general approach entails the adversary placing themself within the communication channel between the two components."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/94.html
---

# CAPEC-94: Adversary in the Middle (AiTM)

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Very High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary targets the communication between two components (typically client and server), in order to alter or obtain data from transactions. A general approach entails the adversary placing themself within the communication channel between the two components.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-287](/wiki/p/weakness/CWE-287), [CWE-290](/wiki/p/weakness/CWE-290), [CWE-294](/wiki/p/weakness/CWE-294), [CWE-300](/wiki/p/weakness/CWE-300), [CWE-593](/wiki/p/weakness/CWE-593)

**ATT&CK techniques:** [T1557](/wiki/p/technique/T1557)

## Prerequisites

- There are two components communicating with each other.
- An attacker is able to identify the nature and mechanism of communication between the two target components.
- An attacker can eavesdrop on the communication between the target components.
- Strong mutual authentication is not used between the two target components yielding opportunity for attacker interposition.
- The communication occurs in clear (not encrypted) or with insufficient and spoofable encryption.

## Skills required

- Medium: This attack can get sophisticated since the attack may use cryptography.

## Consequences

- Integrity: Modify Data
- Confidentiality, Access Control, Authorization: Gain Privileges
- Confidentiality: Read Data

## Mitigations

- Ensure Public Keys are signed by a Certificate Authority
- Encrypt communications using cryptography (e.g., SSL/TLS)
- Use Strong mutual authentication to always fully authenticate both ends of any communications channel.
- Exchange public keys using a secure channel

## Source

- [MITRE CAPEC CAPEC-94](https://capec.mitre.org/data/definitions/94.html)
