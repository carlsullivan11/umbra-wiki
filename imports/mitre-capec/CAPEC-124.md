---
slug: attack-pattern/CAPEC-124
title: "CAPEC-124 — Shared Resource Manipulation"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-124]
cwe_ids: [CWE-1189, CWE-1331]
related: [weakness/CWE-1189, weakness/CWE-1331]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-124
updated_at: 2026-08-31
summary: "An adversary exploits a resource shared between multiple applications, an application pool or hardware pin multiplexing to affect behavior. Resources may be shared between multiple applications or between multiple threads of a single application. Resource sharing is usually accom…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/124.html
---

# CAPEC-124: Shared Resource Manipulation

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary exploits a resource shared between multiple applications, an application pool or hardware pin multiplexing to affect behavior. Resources may be shared between multiple applications or between multiple threads of a single application. Resource sharing is usually accomplished through mutual access to a single memory location or multiplexed hardware pins. If an adversary can manipulate this shared resource (usually by co-opting one of the applications or threads) the other applications or threads using the shared resource will often continue to trust the validity of the compromised shared resource and use it in their calculations. This can result in invalid trust assumptions, corruption of additional data through the normal operations of the other users of the shared resource, or even cause a crash or compromise of the sharing applications.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-1189](/wiki/p/weakness/CWE-1189), [CWE-1331](/wiki/p/weakness/CWE-1331)

## Prerequisites

- The target applications, threads or functions must share resources between themselves.
- The adversary must be able to manipulate some piece of the shared resource either directly or indirectly and the other users of the data must accept the changed data as valid. Usually this requires that the adversary be able to compromise one of the sharing applications or threads in order to manipulate the shared data.

## Source

- [MITRE CAPEC CAPEC-124](https://capec.mitre.org/data/definitions/124.html)
