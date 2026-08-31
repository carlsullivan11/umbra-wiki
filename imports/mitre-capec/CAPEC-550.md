---
slug: attack-pattern/CAPEC-550
title: "CAPEC-550 — Install New Service"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-550]
cwe_ids: [CWE-284]
mitre_ids: [T1543]
related: [weakness/CWE-284, technique/T1543]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-550
updated_at: 2026-08-31
summary: "When an operating system starts, it also starts programs called services or daemons. Adversaries may install a new service which will be executed at startup (on a Windows system, by modifying the registry). The service name may be disguised by using a name from a related operatin…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/550.html
---

# CAPEC-550: Install New Service

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | — |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

When an operating system starts, it also starts programs called services or daemons. Adversaries may install a new service which will be executed at startup (on a Windows system, by modifying the registry). The service name may be disguised by using a name from a related operating system or benign software. Services are usually run with elevated privileges.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-284](/wiki/p/weakness/CWE-284)

**ATT&CK techniques:** [T1543](/wiki/p/technique/T1543)

## Mitigations

- Limit privileges of user accounts so new service creation can only be performed by authorized administrators.

## Source

- [MITRE CAPEC CAPEC-550](https://capec.mitre.org/data/definitions/550.html)
