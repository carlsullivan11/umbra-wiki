---
slug: attack-pattern/CAPEC-571
title: "CAPEC-571 — Block Logging to Central Repository"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-571]
mitre_ids: [T1562.002, T1562.006, T1562.008]
related: []
provenance: imported
import_source: mitre-capec
import_id: CAPEC-571
updated_at: 2026-08-31
summary: "An adversary prevents host-generated logs being delivered to a central location in an attempt to hide indicators of compromise."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/571.html
---

# CAPEC-571: Block Logging to Central Repository

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Low |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary prevents host-generated logs being delivered to a central location in an attempt to hide indicators of compromise.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**ATT&CK techniques:** [T1562.002](/wiki/p/technique/T1562.002), [T1562.006](/wiki/p/technique/T1562.006), [T1562.008](/wiki/p/technique/T1562.008)

## Mappings that no longer resolve

CAPEC 3.9 (2023-01-24) maps this pattern to `T1562.002`, `T1562.006`, `T1562.008`, which the current ATT&CK corpus does not carry — MITRE has revoked or relocated them since CAPEC was last published. The mapping is recorded here rather than dropped, because a stale cross-reference is a fact about the taxonomies, not a gap in this page.

## Source

- [MITRE CAPEC CAPEC-571](https://capec.mitre.org/data/definitions/571.html)
