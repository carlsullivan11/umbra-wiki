---
slug: attack-pattern/CAPEC-633
title: "CAPEC-633 — Token Impersonation"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-633]
cwe_ids: [CWE-287, CWE-1270]
mitre_ids: [T1134]
related: [weakness/CWE-287, weakness/CWE-1270, technique/T1134]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-633
updated_at: 2026-08-31
summary: "An adversary exploits a weakness in authentication to create an access token (or equivalent) that impersonates a different entity, and then associates a process/thread to that that impersonated token. This action causes a downstream user to make a decision or take action that is …"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/633.html
---

# CAPEC-633: Token Impersonation

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Medium |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary exploits a weakness in authentication to create an access token (or equivalent) that impersonates a different entity, and then associates a process/thread to that that impersonated token. This action causes a downstream user to make a decision or take action that is based on the assumed identity, and not the response that blocks the adversary.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-287](/wiki/p/weakness/CWE-287), [CWE-1270](/wiki/p/weakness/CWE-1270)

**ATT&CK techniques:** [T1134](/wiki/p/technique/T1134)

## Prerequisites

- This pattern of attack is only applicable when a downstream user leverages tokens to verify identity, and then takes action based on that identity.

## Consequences

- Integrity: Alter Execution Logic
- Integrity: Gain Privileges
- Integrity: Hide Activities

## Source

- [MITRE CAPEC CAPEC-633](https://capec.mitre.org/data/definitions/633.html)
