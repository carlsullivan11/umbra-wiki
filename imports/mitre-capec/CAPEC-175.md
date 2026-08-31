---
slug: attack-pattern/CAPEC-175
title: "CAPEC-175 — Code Inclusion"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-175]
cwe_ids: [CWE-829]
related: [weakness/CWE-829]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-175
updated_at: 2026-08-31
summary: "An adversary exploits a weakness on the target to force arbitrary code to be retrieved locally or from a remote location and executed. This differs from code injection in that code injection involves the direct inclusion of code while code inclusion involves the addition or repla…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/175.html
---

# CAPEC-175: Code Inclusion

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Very High |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary exploits a weakness on the target to force arbitrary code to be retrieved locally or from a remote location and executed. This differs from code injection in that code injection involves the direct inclusion of code while code inclusion involves the addition or replacement of a reference to a code file, which is subsequently loaded by the target and used as part of the code of some application.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-829](/wiki/p/weakness/CWE-829)

## Prerequisites

- The target application must include external code/libraries that are executed when the application runs and the adversary must be able to influence the specific files that get included.
- The victim must run the targeted application, possibly using the crafted parameters that the adversary uses to identify the code to include.

## Source

- [MITRE CAPEC CAPEC-175](https://capec.mitre.org/data/definitions/175.html)
