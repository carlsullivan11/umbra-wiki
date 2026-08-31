---
slug: attack-pattern/CAPEC-307
title: "CAPEC-307 — TCP RPC Scan"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-307]
cwe_ids: [CWE-200]
related: [weakness/CWE-200]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-307
updated_at: 2026-08-31
summary: "An adversary scans for RPC services listing on a Unix/Linux host."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/307.html
---

# CAPEC-307: TCP RPC Scan

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Low |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary scans for RPC services listing on a Unix/Linux host.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-200](/wiki/p/weakness/CWE-200)

## Prerequisites

- RPC scanning requires no special privileges when it is performed via a native system utility.

## Consequences

- Confidentiality: Other
- Confidentiality, Access Control, Authorization: Bypass Protection Mechanism, Hide Activities

## Mitigations

- Typically, an IDS/IPS system is very effective against this type of attack.

## Source

- [MITRE CAPEC CAPEC-307](https://capec.mitre.org/data/definitions/307.html)
