---
slug: attack-pattern/CAPEC-221
title: "CAPEC-221 — Data Serialization External Entities Blowup"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-221]
cwe_ids: [CWE-611]
related: [weakness/CWE-611]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-221
updated_at: 2026-08-31
summary: "This attack takes advantage of the entity replacement property of certain data serialization languages (e.g., XML, YAML, etc.) where the value of the replacement is a URI. A well-crafted file could have the entity refer to a URI that consumes a large amount of resources to create…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/221.html
---

# CAPEC-221: Data Serialization External Entities Blowup

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | — |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

This attack takes advantage of the entity replacement property of certain data serialization languages (e.g., XML, YAML, etc.) where the value of the replacement is a URI. A well-crafted file could have the entity refer to a URI that consumes a large amount of resources to create a denial of service condition. This can cause the system to either freeze, crash, or execute arbitrary code depending on the URI.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-611](/wiki/p/weakness/CWE-611)

## Prerequisites

- A server that has an implementation that accepts entities containing URI values.

## Consequences

- Availability: Resource Consumption
- Confidentiality, Integrity, Availability: Execute Unauthorized Commands

## Mitigations

- This attack may be mitigated by tweaking the XML parser to not resolve external entities. If external entities are needed, then implement a custom XmlResolver that has a request timeout, data retrieval limit, and restrict resources it can retrieve locally.
- This attack may be mitigated by tweaking the serialized data parser to not resolve external entities. If external entities are needed, then implement a custom resolver that has a request timeout, data retrieval limit, and restrict resources it can retrieve locally.

## Source

- [MITRE CAPEC CAPEC-221](https://capec.mitre.org/data/definitions/221.html)
