---
slug: attack-pattern/CAPEC-121
title: "CAPEC-121 — Exploit Non-Production Interfaces"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-121]
cwe_ids: [CWE-489, CWE-1209, CWE-1259, CWE-1267, CWE-1270, CWE-1294, CWE-1295, CWE-1296, CWE-1302, CWE-1313]
related: [weakness/CWE-489, weakness/CWE-1209, weakness/CWE-1259, weakness/CWE-1267, weakness/CWE-1270, weakness/CWE-1294, weakness/CWE-1295, weakness/CWE-1296, weakness/CWE-1302, weakness/CWE-1313]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-121
updated_at: 2026-08-31
summary: "An adversary exploits a sample, demonstration, test, or debug interface that is unintentionally enabled on a production system, with the goal of gleaning information or leveraging functionality that would otherwise be unavailable."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/121.html
---

# CAPEC-121: Exploit Non-Production Interfaces

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | High |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary exploits a sample, demonstration, test, or debug interface that is unintentionally enabled on a production system, with the goal of gleaning information or leveraging functionality that would otherwise be unavailable.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-489](/wiki/p/weakness/CWE-489), [CWE-1209](/wiki/p/weakness/CWE-1209), [CWE-1259](/wiki/p/weakness/CWE-1259), [CWE-1267](/wiki/p/weakness/CWE-1267), [CWE-1270](/wiki/p/weakness/CWE-1270), [CWE-1294](/wiki/p/weakness/CWE-1294), [CWE-1295](/wiki/p/weakness/CWE-1295), [CWE-1296](/wiki/p/weakness/CWE-1296), [CWE-1302](/wiki/p/weakness/CWE-1302), [CWE-1313](/wiki/p/weakness/CWE-1313)

## Prerequisites

- The target must have configured non-production interfaces and failed to secure or remove them when brought into a production environment.

## Skills required

- High: Exploiting non-production interfaces requires significant skill and knowledge about the potential non-production interfaces left enabled in production.

## Consequences

- Confidentiality, Access Control, Authentication: Gain Privileges, Bypass Protection Mechanism
- Confidentiality, Access Control, Authorization: Read Data, Execute Unauthorized Commands
- Access Control, Integrity: Modify Data, Alter Execution Logic

## Mitigations

- Ensure that production systems do not contain non-production interfaces and that these interfaces are only used in development environments.

## Source

- [MITRE CAPEC CAPEC-121](https://capec.mitre.org/data/definitions/121.html)
