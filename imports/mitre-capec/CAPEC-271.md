---
slug: attack-pattern/CAPEC-271
title: "CAPEC-271 — Schema Poisoning"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-271]
cwe_ids: [CWE-15]
related: [weakness/CWE-15]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-271
updated_at: 2026-08-31
summary: "An adversary corrupts or modifies the content of a schema for the purpose of undermining the security of the target. Schemas provide the structure and content definitions for resources used by an application. By replacing or modifying a schema, the adversary can affect how the ap…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/271.html
---

# CAPEC-271: Schema Poisoning

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary corrupts or modifies the content of a schema for the purpose of undermining the security of the target. Schemas provide the structure and content definitions for resources used by an application. By replacing or modifying a schema, the adversary can affect how the application handles or interprets a resource, often leading to possible denial of service, entering into an unexpected state, or recording incomplete data.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-15](/wiki/p/weakness/CWE-15)

## Prerequisites

- Some level of access to modify the target schema.
- The schema used by the target application must be improperly secured against unauthorized modification and manipulation.

## Consequences

- Availability: Unreliable Execution, Resource Consumption
- Integrity: Modify Data
- Confidentiality: Read Data

## Mitigations

- Design: Protect the schema against unauthorized modification.
- Implementation: For applications that use a known schema, use a local copy or a known good repository instead of the schema reference supplied in the schema document.
- Implementation: For applications that leverage remote schemas, use the HTTPS protocol to prevent modification of traffic in transit and to avoid unauthorized modification.

## Source

- [MITRE CAPEC CAPEC-271](https://capec.mitre.org/data/definitions/271.html)
