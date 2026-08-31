---
slug: attack-pattern/CAPEC-694
title: "CAPEC-694 — System Location Discovery"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-694]
cwe_ids: [CWE-497]
mitre_ids: [T1614]
related: [weakness/CWE-497, technique/T1614]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-694
updated_at: 2026-08-31
summary: "An adversary collects information about the target system in an attempt to identify the system's geographical location. Information gathered could include keyboard layout, system language, and timezone. This information may benefit an adversary in confirming the desired target an…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/694.html
---

# CAPEC-694: System Location Discovery

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Very Low |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary collects information about the target system in an attempt to identify the system's geographical location. Information gathered could include keyboard layout, system language, and timezone. This information may benefit an adversary in confirming the desired target and/or tailoring further attacks.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-497](/wiki/p/weakness/CWE-497)

**ATT&CK techniques:** [T1614](/wiki/p/technique/T1614)

## Prerequisites

- The adversary must have some level of access to the system and have a basic understanding of the operating system in order to query the appropriate sources for relevant information.

## Skills required

- Low: The adversary must know how to query various system sources of information respective of the system's operating system to obtain the relevant information.

## Consequences

- Confidentiality: Read Data

## Mitigations

- To reduce the amount of information gathered, one could disable various geolocation features of the operating system not required for system operation.

## Source

- [MITRE CAPEC CAPEC-694](https://capec.mitre.org/data/definitions/694.html)
