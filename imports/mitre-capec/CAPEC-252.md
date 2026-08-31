---
slug: attack-pattern/CAPEC-252
title: "CAPEC-252 — PHP Local File Inclusion"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-252]
cwe_ids: [CWE-829]
related: [weakness/CWE-829]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-252
updated_at: 2026-08-31
summary: "The attacker loads and executes an arbitrary local PHP file on a target machine. The attacker could use this to try to load old versions of PHP files that have known vulnerabilities, to load PHP files that the attacker placed on the local machine during a prior attack, or to othe…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/252.html
---

# CAPEC-252: PHP Local File Inclusion

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

The attacker loads and executes an arbitrary local PHP file on a target machine. The attacker could use this to try to load old versions of PHP files that have known vulnerabilities, to load PHP files that the attacker placed on the local machine during a prior attack, or to otherwise change the functionality of the targeted application in unexpected ways.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-829](/wiki/p/weakness/CWE-829)

## Prerequisites

- The targeted PHP application must have a bug that allows an attacker to control which code file is loaded at some juncture.

## Source

- [MITRE CAPEC CAPEC-252](https://capec.mitre.org/data/definitions/252.html)
