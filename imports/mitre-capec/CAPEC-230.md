---
slug: attack-pattern/CAPEC-230
title: "CAPEC-230 — Serialized Data with Nested Payloads"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-230]
cwe_ids: [CWE-20, CWE-112, CWE-674, CWE-770]
related: [weakness/CWE-20, weakness/CWE-112, weakness/CWE-674, weakness/CWE-770]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-230
updated_at: 2026-08-31
summary: "Applications often need to transform data in and out of a data format (e.g., XML and YAML) by using a parser. It may be possible for an adversary to inject data that may have an adverse effect on the parser when it is being processed. Many data format languages allow the definiti…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/230.html
---

# CAPEC-230: Serialized Data with Nested Payloads

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

Applications often need to transform data in and out of a data format (e.g., XML and YAML) by using a parser. It may be possible for an adversary to inject data that may have an adverse effect on the parser when it is being processed. Many data format languages allow the definition of macro-like structures that can be used to simplify the creation of complex structures. By nesting these structures, causing the data to be repeatedly substituted, an adversary can cause the parser to consume more resources while processing, causing excessive memory consumption and CPU utilization.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-20](/wiki/p/weakness/CWE-20), [CWE-112](/wiki/p/weakness/CWE-112), [CWE-674](/wiki/p/weakness/CWE-674), [CWE-770](/wiki/p/weakness/CWE-770)

## Prerequisites

- An application's user-controllable data is expressed in a language that supports subsitution.
- An application does not perform sufficient validation to ensure that user-controllable data is not malicious.

## Consequences

- Availability: Resource Consumption
- Confidentiality: Read Data
- Confidentiality, Integrity, Availability: Execute Unauthorized Commands
- Confidentiality, Access Control, Authorization: Gain Privileges

## Mitigations

- Carefully validate and sanitize all user-controllable data prior to passing it to the data parser routine. Ensure that the resultant data is safe to pass to the data parser.
- Perform validation on canonical data.
- Pick a robust implementation of the data parser.

## Source

- [MITRE CAPEC CAPEC-230](https://capec.mitre.org/data/definitions/230.html)
