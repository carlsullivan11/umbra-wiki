---
slug: attack-pattern/CAPEC-497
title: "CAPEC-497 — File Discovery"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-497]
cwe_ids: [CWE-200]
mitre_ids: [T1083]
related: [weakness/CWE-200, technique/T1083]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-497
updated_at: 2026-08-31
summary: "An adversary engages in probing and exploration activities to determine if common key files exists. Such files often contain configuration and security parameters of the targeted application, system or network. Using this knowledge may often pave the way for more damaging attacks…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/497.html
---

# CAPEC-497: File Discovery

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Very Low |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary engages in probing and exploration activities to determine if common key files exists. Such files often contain configuration and security parameters of the targeted application, system or network. Using this knowledge may often pave the way for more damaging attacks.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-200](/wiki/p/weakness/CWE-200)

**ATT&CK techniques:** [T1083](/wiki/p/technique/T1083)

## Prerequisites

- The adversary must know the location of these common key files.

## Consequences

- Confidentiality: Read Data

## Mitigations

- Leverage file protection mechanisms to render these files accessible only to authorized parties.

## Source

- [MITRE CAPEC CAPEC-497](https://capec.mitre.org/data/definitions/497.html)
