---
slug: attack-pattern/CAPEC-278
title: "CAPEC-278 — Web Services Protocol Manipulation"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-278]
cwe_ids: [CWE-707]
related: [weakness/CWE-707]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-278
updated_at: 2026-08-31
summary: "An adversary manipulates a web service related protocol to cause a web application or service to react differently than intended. This can either be performed through the manipulation of call parameters to include unexpected values, or by changing the called function to one that …"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/278.html
---

# CAPEC-278: Web Services Protocol Manipulation

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | — |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary manipulates a web service related protocol to cause a web application or service to react differently than intended. This can either be performed through the manipulation of call parameters to include unexpected values, or by changing the called function to one that should normally be restricted or limited. By leveraging this pattern of attack, the adversary is able to gain access to data or resources normally restricted, or to cause the application or service to crash.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-707](/wiki/p/weakness/CWE-707)

## Prerequisites

- The targeted application or service must rely on web service protocols in such a way that malicious manipulation of them can alter functionality.

## Mitigations

- Design: Range, size and value and consistency verification for any arguments supplied to applications and services from external sources and devise appropriate error response.
- Design: Ensure that function calls that should not be called by an unprivileged user are not accessible to them.

## Source

- [MITRE CAPEC CAPEC-278](https://capec.mitre.org/data/definitions/278.html)
