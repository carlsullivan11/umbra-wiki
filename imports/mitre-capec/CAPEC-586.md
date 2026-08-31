---
slug: attack-pattern/CAPEC-586
title: "CAPEC-586 — Object Injection"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-586]
cwe_ids: [CWE-502]
related: [weakness/CWE-502]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-586
updated_at: 2026-08-31
summary: "An adversary attempts to exploit an application by injecting additional, malicious content during its processing of serialized objects. Developers leverage serialization in order to convert data or state into a static, binary format for saving to disk or transferring over a netwo…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/586.html
---

# CAPEC-586: Object Injection

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary attempts to exploit an application by injecting additional, malicious content during its processing of serialized objects. Developers leverage serialization in order to convert data or state into a static, binary format for saving to disk or transferring over a network. These objects are then deserialized when needed to recover the data/state. By injecting a malformed object into a vulnerable application, an adversary can potentially compromise the application by manipulating the deserialization process. This can result in a number of unwanted outcomes, including remote code execution.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-502](/wiki/p/weakness/CWE-502)

## Prerequisites

- The target application must unserialize data before validation.

## Consequences

- Availability: Resource Consumption
- Integrity: Modify Data
- Authorization: Execute Unauthorized Commands

## Mitigations

- Implementation: Validate object before deserialization process
- Design: Limit which types can be deserialized.
- Implementation: Avoid having unnecessary types or gadgets available that can be leveraged for malicious ends. Use an allowlist of acceptable classes.
- Implementation: Keep session state on the server, when possible.

## Source

- [MITRE CAPEC CAPEC-586](https://capec.mitre.org/data/definitions/586.html)
