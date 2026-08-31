---
slug: attack-pattern/CAPEC-204
title: "CAPEC-204 — Lifting Sensitive Data Embedded in Cache"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-204]
cwe_ids: [CWE-311, CWE-524, CWE-1239, CWE-1258]
mitre_ids: [T1005]
related: [weakness/CWE-311, weakness/CWE-524, weakness/CWE-1239, weakness/CWE-1258, technique/T1005]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-204
updated_at: 2026-08-31
summary: "An adversary examines a target application's cache, or a browser cache, for sensitive information. Many applications that communicate with remote entities or which perform intensive calculations utilize caches to improve efficiency. However, if the application computes or receive…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/204.html
---

# CAPEC-204: Lifting Sensitive Data Embedded in Cache

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary examines a target application's cache, or a browser cache, for sensitive information. Many applications that communicate with remote entities or which perform intensive calculations utilize caches to improve efficiency. However, if the application computes or receives sensitive information and the cache is not appropriately protected, an attacker can browse the cache and retrieve this information. This can result in the disclosure of sensitive information.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-311](/wiki/p/weakness/CWE-311), [CWE-524](/wiki/p/weakness/CWE-524), [CWE-1239](/wiki/p/weakness/CWE-1239), [CWE-1258](/wiki/p/weakness/CWE-1258)

**ATT&CK techniques:** [T1005](/wiki/p/technique/T1005)

## Prerequisites

- The target application must store sensitive information in a cache.
- The cache must be inadequately protected against attacker access.

## Source

- [MITRE CAPEC CAPEC-204](https://capec.mitre.org/data/definitions/204.html)
