---
slug: attack-pattern/CAPEC-572
title: "CAPEC-572 — Artificially Inflate File Sizes"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-572]
mitre_ids: [T1027.001]
related: [technique/T1027.001]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-572
updated_at: 2026-08-31
summary: "An adversary modifies file contents by adding data to files for several reasons. Many different attacks could “follow” this pattern resulting in numerous outcomes. Adding data to a file could also result in a Denial of Service condition for devices with limited storage capacity."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/572.html
---

# CAPEC-572: Artificially Inflate File Sizes

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary modifies file contents by adding data to files for several reasons. Many different attacks could “follow” this pattern resulting in numerous outcomes. Adding data to a file could also result in a Denial of Service condition for devices with limited storage capacity.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**ATT&CK techniques:** [T1027.001](/wiki/p/technique/T1027.001)

## Consequences

- Availability: Resource Consumption
- Integrity: Modify Data

## Source

- [MITRE CAPEC CAPEC-572](https://capec.mitre.org/data/definitions/572.html)
