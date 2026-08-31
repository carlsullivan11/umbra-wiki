---
slug: attack-pattern/CAPEC-300
title: "CAPEC-300 — Port Scanning"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-300]
cwe_ids: [CWE-200]
mitre_ids: [T1046]
related: [weakness/CWE-200, technique/T1046]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-300
updated_at: 2026-08-31
summary: "An adversary uses a combination of techniques to determine the state of the ports on a remote target. Any service or application available for TCP or UDP networking will have a port open for communications over the network."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/300.html
---

# CAPEC-300: Port Scanning

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Low |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary uses a combination of techniques to determine the state of the ports on a remote target. Any service or application available for TCP or UDP networking will have a port open for communications over the network.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-200](/wiki/p/weakness/CWE-200)

**ATT&CK techniques:** [T1046](/wiki/p/technique/T1046)

## Prerequisites

- The adversary requires logical access to the target's network in order to carry out this type of attack.

## Consequences

- Confidentiality: Other
- Confidentiality, Access Control, Authorization: Bypass Protection Mechanism, Hide Activities

## Source

- [MITRE CAPEC CAPEC-300](https://capec.mitre.org/data/definitions/300.html)
