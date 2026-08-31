---
slug: attack-pattern/CAPEC-224
title: "CAPEC-224 — Fingerprinting"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-224]
cwe_ids: [CWE-200]
related: [weakness/CWE-200]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-224
updated_at: 2026-08-31
summary: "An adversary compares output from a target system to known indicators that uniquely identify specific details about the target. Most commonly, fingerprinting is done to determine operating system and application versions. Fingerprinting can be done passively as well as actively. …"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/224.html
---

# CAPEC-224: Fingerprinting

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Very Low |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary compares output from a target system to known indicators that uniquely identify specific details about the target. Most commonly, fingerprinting is done to determine operating system and application versions. Fingerprinting can be done passively as well as actively. Fingerprinting by itself is not usually detrimental to the target. However, the information gathered through fingerprinting often enables an adversary to discover existing weaknesses in the target.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-200](/wiki/p/weakness/CWE-200)

## Prerequisites

- A means by which to interact with the target system directly.

## Skills required

- Medium: Some fingerprinting activity requires very specific knowledge of how different operating systems respond to various TCP/IP requests. Application fingerprinting can be as easy as envoking the application with the correct command line argument, or mouse clicking in the appropriate place on the screen.

## Consequences

- Confidentiality: Read Data

## Mitigations

- While some information is shared by systems automatically based on standards and protocols, remove potentially sensitive information that is not necessary for the application's functionality as much as possible.

## Source

- [MITRE CAPEC CAPEC-224](https://capec.mitre.org/data/definitions/224.html)
