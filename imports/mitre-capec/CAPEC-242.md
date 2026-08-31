---
slug: attack-pattern/CAPEC-242
title: "CAPEC-242 — Code Injection"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-242]
cwe_ids: [CWE-94]
related: [weakness/CWE-94]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-242
updated_at: 2026-08-31
summary: "An adversary exploits a weakness in input validation on the target to inject new code into that which is currently executing. This differs from code inclusion in that code inclusion involves the addition or replacement of a reference to a code file, which is subsequently loaded b…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/242.html
---

# CAPEC-242: Code Injection

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary exploits a weakness in input validation on the target to inject new code into that which is currently executing. This differs from code inclusion in that code inclusion involves the addition or replacement of a reference to a code file, which is subsequently loaded by the target and used as part of the code of some application.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-94](/wiki/p/weakness/CWE-94)

## Prerequisites

- The target software does not validate user-controlled input such that the execution of a process may be altered by sending code in through legitimate data channels, using no other mechanism.

## Consequences

- Confidentiality, Integrity, Availability: Other

## Mitigations

- Utilize strict type, character, and encoding enforcement
- Ensure all input content that is delivered to client is sanitized against an acceptable content specification.
- Perform input validation for all content.
- Enforce regular patching of software.

## Source

- [MITRE CAPEC CAPEC-242](https://capec.mitre.org/data/definitions/242.html)
