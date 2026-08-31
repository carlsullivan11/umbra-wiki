---
slug: attack-pattern/CAPEC-176
title: "CAPEC-176 — Configuration/Environment Manipulation"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-176]
cwe_ids: [CWE-15, CWE-1233, CWE-1234, CWE-1304, CWE-1328]
related: [weakness/CWE-15, weakness/CWE-1233, weakness/CWE-1234, weakness/CWE-1304, weakness/CWE-1328]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-176
updated_at: 2026-08-31
summary: "An attacker manipulates files or settings external to a target application which affect the behavior of that application. For example, many applications use external configuration files and libraries - modification of these entities or otherwise affecting the application's abilit…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/176.html
---

# CAPEC-176: Configuration/Environment Manipulation

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker manipulates files or settings external to a target application which affect the behavior of that application. For example, many applications use external configuration files and libraries - modification of these entities or otherwise affecting the application's ability to use them would constitute a configuration/environment manipulation attack.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-15](/wiki/p/weakness/CWE-15), [CWE-1233](/wiki/p/weakness/CWE-1233), [CWE-1234](/wiki/p/weakness/CWE-1234), [CWE-1304](/wiki/p/weakness/CWE-1304), [CWE-1328](/wiki/p/weakness/CWE-1328)

## Prerequisites

- The target application must consult external files or configuration controls to control its execution. All but the very simplest applications meet this requirement.

## Source

- [MITRE CAPEC CAPEC-176](https://capec.mitre.org/data/definitions/176.html)
