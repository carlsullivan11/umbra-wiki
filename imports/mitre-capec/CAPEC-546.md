---
slug: attack-pattern/CAPEC-546
title: "CAPEC-546 — Incomplete Data Deletion in a Multi-Tenant Environment"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-546]
cwe_ids: [CWE-284, CWE-1266, CWE-1272]
related: [weakness/CWE-284, weakness/CWE-1266, weakness/CWE-1272]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-546
updated_at: 2026-08-31
summary: "An adversary obtains unauthorized information due to insecure or incomplete data deletion in a multi-tenant environment. If a cloud provider fails to completely delete storage and data from former cloud tenants' systems/resources, once these resources are allocated to new, potent…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/546.html
---

# CAPEC-546: Incomplete Data Deletion in a Multi-Tenant Environment

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary obtains unauthorized information due to insecure or incomplete data deletion in a multi-tenant environment. If a cloud provider fails to completely delete storage and data from former cloud tenants' systems/resources, once these resources are allocated to new, potentially malicious tenants, the latter can probe the provided resources for sensitive information still there.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-284](/wiki/p/weakness/CWE-284), [CWE-1266](/wiki/p/weakness/CWE-1266), [CWE-1272](/wiki/p/weakness/CWE-1272)

## Prerequisites

- The cloud provider must not assuredly delete part or all of the sensitive data for which they are responsible.The adversary must have the ability to interact with the system.

## Skills required

- Low: The adversary requires the ability to traverse directory structure.

## Consequences

- Confidentiality: Read Data

## Mitigations

- Cloud providers should completely delete data to render it irrecoverable and inaccessible from any layer and component of infrastructure resources.
- Deletion of data should be completed promptly when requested.

## Source

- [MITRE CAPEC CAPEC-546](https://capec.mitre.org/data/definitions/546.html)
