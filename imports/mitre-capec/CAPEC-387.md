---
slug: attack-pattern/CAPEC-387
title: "CAPEC-387 — Navigation Remapping To Propagate Malicious Content"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-387]
cwe_ids: [CWE-311, CWE-345, CWE-346, CWE-471, CWE-602]
related: [weakness/CWE-311, weakness/CWE-345, weakness/CWE-346, weakness/CWE-471, weakness/CWE-602]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-387
updated_at: 2026-08-31
summary: "An adversary manipulates either egress or ingress data from a client within an application framework in order to change the content of messages and thereby circumvent the expected application logic."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/387.html
---

# CAPEC-387: Navigation Remapping To Propagate Malicious Content

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary manipulates either egress or ingress data from a client within an application framework in order to change the content of messages and thereby circumvent the expected application logic.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-311](/wiki/p/weakness/CWE-311), [CWE-345](/wiki/p/weakness/CWE-345), [CWE-346](/wiki/p/weakness/CWE-346), [CWE-471](/wiki/p/weakness/CWE-471), [CWE-602](/wiki/p/weakness/CWE-602)

## Prerequisites

- Targeted software is utilizing application framework APIs

## Source

- [MITRE CAPEC CAPEC-387](https://capec.mitre.org/data/definitions/387.html)
