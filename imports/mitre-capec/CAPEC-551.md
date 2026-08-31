---
slug: attack-pattern/CAPEC-551
title: "CAPEC-551 — Modify Existing Service"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-551]
cwe_ids: [CWE-284, CWE-522]
mitre_ids: [T1543]
related: [weakness/CWE-284, weakness/CWE-522, technique/T1543]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-551
updated_at: 2026-08-31
summary: "When an operating system starts, it also starts programs called services or daemons. Modifying existing services may break existing services or may enable services that are disabled/not commonly used."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/551.html
---

# CAPEC-551: Modify Existing Service

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | — |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

When an operating system starts, it also starts programs called services or daemons. Modifying existing services may break existing services or may enable services that are disabled/not commonly used.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-284](/wiki/p/weakness/CWE-284), [CWE-522](/wiki/p/weakness/CWE-522)

**ATT&CK techniques:** [T1543](/wiki/p/technique/T1543)

## Mitigations

- Limit privileges of user accounts so service changes can only be performed by authorized administrators. Also monitor any service changes that may occur inadvertently.

## Source

- [MITRE CAPEC CAPEC-551](https://capec.mitre.org/data/definitions/551.html)
