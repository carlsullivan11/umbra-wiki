---
slug: attack-pattern/CAPEC-100
title: "CAPEC-100 — Overflow Buffers"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-100]
cwe_ids: [CWE-119, CWE-120, CWE-129, CWE-131, CWE-680, CWE-805]
related: [weakness/CWE-119, weakness/CWE-120, weakness/CWE-129, weakness/CWE-131, weakness/CWE-680, weakness/CWE-805]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-100
updated_at: 2026-08-31
summary: "Buffer Overflow attacks target improper or missing bounds checking on buffer operations, typically triggered by input injected by an adversary. As a consequence, an adversary is able to write past the boundaries of allocated buffer regions in memory, causing a program crash or po…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/100.html
---

# CAPEC-100: Overflow Buffers

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Very High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

Buffer Overflow attacks target improper or missing bounds checking on buffer operations, typically triggered by input injected by an adversary. As a consequence, an adversary is able to write past the boundaries of allocated buffer regions in memory, causing a program crash or potentially redirection of execution as per the adversaries' choice.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-119](/wiki/p/weakness/CWE-119), [CWE-120](/wiki/p/weakness/CWE-120), [CWE-129](/wiki/p/weakness/CWE-129), [CWE-131](/wiki/p/weakness/CWE-131), [CWE-680](/wiki/p/weakness/CWE-680), [CWE-805](/wiki/p/weakness/CWE-805)

## Prerequisites

- Targeted software performs buffer operations.
- Targeted software inadequately performs bounds-checking on buffer operations.
- Adversary has the capability to influence the input to buffer operations.

## Skills required

- Low: In most cases, overflowing a buffer does not require advanced skills beyond the ability to notice an overflow and stuff an input variable with content.
- High: In cases of directed overflows, where the motive is to divert the flow of the program or application as per the adversaries' bidding, high level skills are required. This may involve detailed knowledge of the target system architecture and kernel.

## Consequences

- Availability: Unreliable Execution
- Confidentiality, Integrity, Availability: Execute Unauthorized Commands
- Confidentiality, Access Control, Authorization: Gain Privileges

## Mitigations

- Use a language or compiler that performs automatic bounds checking.
- Use secure functions not vulnerable to buffer overflow.
- If you have to use dangerous functions, make sure that you do boundary checking.
- Compiler-based canary mechanisms such as StackGuard, ProPolice and the Microsoft Visual Studio /GS flag. Unless this provides automatic bounds checking, it is not a complete solution.
- Use OS-level preventative functionality. Not a complete solution.
- Utilize static source code analysis tools to identify potential buffer overflow weaknesses in the software.

## Source

- [MITRE CAPEC CAPEC-100](https://capec.mitre.org/data/definitions/100.html)
