---
slug: attack-pattern/CAPEC-562
title: "CAPEC-562 — Modify Shared File"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-562]
cwe_ids: [CWE-284]
mitre_ids: [T1080]
related: [weakness/CWE-284, technique/T1080]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-562
updated_at: 2026-08-31
summary: "An adversary manipulates the files in a shared location by adding malicious programs, scripts, or exploit code to valid content. Once a user opens the shared content, the tainted content is executed."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/562.html
---

# CAPEC-562: Modify Shared File

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | — |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary manipulates the files in a shared location by adding malicious programs, scripts, or exploit code to valid content. Once a user opens the shared content, the tainted content is executed.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-284](/wiki/p/weakness/CWE-284)

**ATT&CK techniques:** [T1080](/wiki/p/technique/T1080)

## Mitigations

- Disallow shared content. Protect shared folders by minimizing users that have write access. Use utilities that mitigate exploitation like the Microsoft Enhanced Mitigation Experience Toolkit (EMET) to prevent exploits from being run.

## Source

- [MITRE CAPEC CAPEC-562](https://capec.mitre.org/data/definitions/562.html)
