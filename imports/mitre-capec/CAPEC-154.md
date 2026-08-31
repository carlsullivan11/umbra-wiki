---
slug: attack-pattern/CAPEC-154
title: "CAPEC-154 — Resource Location Spoofing"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-154]
cwe_ids: [CWE-451]
related: [weakness/CWE-451]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-154
updated_at: 2026-08-31
summary: "An adversary deceives an application or user and convinces them to request a resource from an unintended location. By spoofing the location, the adversary can cause an alternate resource to be used, often one that the adversary controls and can be used to help them achieve their …"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/154.html
---

# CAPEC-154: Resource Location Spoofing

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Medium |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary deceives an application or user and convinces them to request a resource from an unintended location. By spoofing the location, the adversary can cause an alternate resource to be used, often one that the adversary controls and can be used to help them achieve their malicious goals.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-451](/wiki/p/weakness/CWE-451)

## Prerequisites

- None. All applications rely on file paths and therefore, in theory, they or their resources could be affected by this type of attack.

## Consequences

- Authorization: Execute Unauthorized Commands

## Mitigations

- Monitor network activity to detect any anomalous or unauthorized communication exchanges.

## Source

- [MITRE CAPEC CAPEC-154](https://capec.mitre.org/data/definitions/154.html)
