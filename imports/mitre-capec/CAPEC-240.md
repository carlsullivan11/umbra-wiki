---
slug: attack-pattern/CAPEC-240
title: "CAPEC-240 — Resource Injection"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-240]
cwe_ids: [CWE-99]
related: [weakness/CWE-99]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-240
updated_at: 2026-08-31
summary: "An adversary exploits weaknesses in input validation by manipulating resource identifiers enabling the unintended modification or specification of a resource."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/240.html
---

# CAPEC-240: Resource Injection

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary exploits weaknesses in input validation by manipulating resource identifiers enabling the unintended modification or specification of a resource.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-99](/wiki/p/weakness/CWE-99)

## Prerequisites

- The target application allows the user to both specify the identifier used to access a system resource. Through this permission, the user gains the capability to perform actions on that resource (e.g., overwrite the file)

## Consequences

- Confidentiality: Read Data
- Integrity: Modify Data

## Mitigations

- Ensure all input content that is delivered to client is sanitized against an acceptable content specification.
- Perform input validation for all content.
- Enforce regular patching of software.

## Source

- [MITRE CAPEC CAPEC-240](https://capec.mitre.org/data/definitions/240.html)
