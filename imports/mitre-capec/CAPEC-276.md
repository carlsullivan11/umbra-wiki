---
slug: attack-pattern/CAPEC-276
title: "CAPEC-276 — Inter-component Protocol Manipulation"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-276]
cwe_ids: [CWE-707]
related: [weakness/CWE-707]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-276
updated_at: 2026-08-31
summary: "Inter-component protocols are used to communicate between different software and hardware modules within a single computer. Common examples are: interrupt signals and data pipes. Subverting the protocol can allow an adversary to impersonate others, discover sensitive information,…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/276.html
---

# CAPEC-276: Inter-component Protocol Manipulation

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | — |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

Inter-component protocols are used to communicate between different software and hardware modules within a single computer. Common examples are: interrupt signals and data pipes. Subverting the protocol can allow an adversary to impersonate others, discover sensitive information, control the outcome of a session, or perform other attacks. This type of attack targets invalid assumptions that may be inherent in implementers of the protocol, incorrect implementations of the protocol, or vulnerabilities in the protocol itself.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-707](/wiki/p/weakness/CWE-707)

## Source

- [MITRE CAPEC CAPEC-276](https://capec.mitre.org/data/definitions/276.html)
