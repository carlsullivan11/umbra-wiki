---
slug: attack-pattern/CAPEC-231
title: "CAPEC-231 — Oversized Serialized Data Payloads"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-231]
cwe_ids: [CWE-20, CWE-112, CWE-674, CWE-770]
related: [weakness/CWE-20, weakness/CWE-112, weakness/CWE-674, weakness/CWE-770]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-231
updated_at: 2026-08-31
summary: "An adversary injects oversized serialized data payloads into a parser during data processing to produce adverse effects upon the parser such as exhausting system resources and arbitrary code execution."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/231.html
---

# CAPEC-231: Oversized Serialized Data Payloads

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary injects oversized serialized data payloads into a parser during data processing to produce adverse effects upon the parser such as exhausting system resources and arbitrary code execution.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-20](/wiki/p/weakness/CWE-20), [CWE-112](/wiki/p/weakness/CWE-112), [CWE-674](/wiki/p/weakness/CWE-674), [CWE-770](/wiki/p/weakness/CWE-770)

## Prerequisites

- An application uses an parser for serialized data to perform transformation on user-controllable data.
- An application does not perform sufficient validation to ensure that user-controllable data is safe for a data parser.

## Skills required

- Low: Denial of service
- High: Arbitrary code execution

## Consequences

- Availability: Resource Consumption
- Confidentiality: Read Data
- Confidentiality, Integrity, Availability: Execute Unauthorized Commands
- Confidentiality, Access Control, Authorization: Gain Privileges

## Mitigations

- Carefully validate and sanitize all user-controllable serialized data prior to passing it to the parser routine. Ensure that the resultant data is safe to pass to the parser.
- Perform validation on canonical data.
- Pick a robust implementation of the serialized data parser.
- Validate data against a valid schema or DTD prior to parsing.

## Source

- [MITRE CAPEC CAPEC-231](https://capec.mitre.org/data/definitions/231.html)
