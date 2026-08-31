---
slug: attack-pattern/CAPEC-554
title: "CAPEC-554 — Functionality Bypass"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-554]
cwe_ids: [CWE-424, CWE-1299]
related: [weakness/CWE-424, weakness/CWE-1299]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-554
updated_at: 2026-08-31
summary: "An adversary attacks a system by bypassing some or all functionality intended to protect it. Often, a system user will think that protection is in place, but the functionality behind those protections has been disabled by the adversary."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/554.html
---

# CAPEC-554: Functionality Bypass

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary attacks a system by bypassing some or all functionality intended to protect it. Often, a system user will think that protection is in place, but the functionality behind those protections has been disabled by the adversary.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-424](/wiki/p/weakness/CWE-424), [CWE-1299](/wiki/p/weakness/CWE-1299)

## Source

- [MITRE CAPEC CAPEC-554](https://capec.mitre.org/data/definitions/554.html)
