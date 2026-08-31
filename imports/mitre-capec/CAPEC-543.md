---
slug: attack-pattern/CAPEC-543
title: "CAPEC-543 — Counterfeit Websites"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-543]
mitre_ids: [T1036.005]
related: [technique/T1036.005]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-543
updated_at: 2026-08-31
summary: "Adversary creates duplicates of legitimate websites. When users visit a counterfeit site, the site can gather information or upload malware."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/543.html
---

# CAPEC-543: Counterfeit Websites

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

Adversary creates duplicates of legitimate websites. When users visit a counterfeit site, the site can gather information or upload malware.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**ATT&CK techniques:** [T1036.005](/wiki/p/technique/T1036.005)

## Prerequisites

- None

## Source

- [MITRE CAPEC CAPEC-543](https://capec.mitre.org/data/definitions/543.html)
