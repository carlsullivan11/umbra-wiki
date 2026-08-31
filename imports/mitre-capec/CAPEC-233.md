---
slug: attack-pattern/CAPEC-233
title: "CAPEC-233 — Privilege Escalation"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-233]
cwe_ids: [CWE-269, CWE-1264, CWE-1311]
mitre_ids: [T1548]
related: [weakness/CWE-269, weakness/CWE-1264, weakness/CWE-1311, technique/T1548]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-233
updated_at: 2026-08-31
summary: "An adversary exploits a weakness enabling them to elevate their privilege and perform an action that they are not supposed to be authorized to perform."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/233.html
---

# CAPEC-233: Privilege Escalation

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | — |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary exploits a weakness enabling them to elevate their privilege and perform an action that they are not supposed to be authorized to perform.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-269](/wiki/p/weakness/CWE-269), [CWE-1264](/wiki/p/weakness/CWE-1264), [CWE-1311](/wiki/p/weakness/CWE-1311)

**ATT&CK techniques:** [T1548](/wiki/p/technique/T1548)

## Source

- [MITRE CAPEC CAPEC-233](https://capec.mitre.org/data/definitions/233.html)
