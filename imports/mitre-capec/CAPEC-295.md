---
slug: attack-pattern/CAPEC-295
title: "CAPEC-295 — Timestamp Request"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-295]
cwe_ids: [CWE-200]
mitre_ids: [T1124]
related: [weakness/CWE-200, technique/T1124]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-295
updated_at: 2026-08-31
summary: "This pattern of attack leverages standard requests to learn the exact time associated with a target system. An adversary may be able to use the timestamp returned from the target to attack time-based security algorithms, such as random number generators, or time-based authenticat…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/295.html
---

# CAPEC-295: Timestamp Request

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Low |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

This pattern of attack leverages standard requests to learn the exact time associated with a target system. An adversary may be able to use the timestamp returned from the target to attack time-based security algorithms, such as random number generators, or time-based authentication mechanisms.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-200](/wiki/p/weakness/CWE-200)

**ATT&CK techniques:** [T1124](/wiki/p/technique/T1124)

## Prerequisites

- The ability to send a timestamp request to a remote target and receive a response.

## Consequences

- Confidentiality: Other

## Source

- [MITRE CAPEC CAPEC-295](https://capec.mitre.org/data/definitions/295.html)
