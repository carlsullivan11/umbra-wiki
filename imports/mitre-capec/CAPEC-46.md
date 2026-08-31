---
slug: attack-pattern/CAPEC-46
title: "CAPEC-46 — Overflow Variables and Tags"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-46]
cwe_ids: [CWE-20, CWE-74, CWE-118, CWE-119, CWE-120, CWE-680, CWE-697, CWE-733]
related: [weakness/CWE-20, weakness/CWE-74, weakness/CWE-118, weakness/CWE-119, weakness/CWE-120, weakness/CWE-680, weakness/CWE-697, weakness/CWE-733]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-46
updated_at: 2026-08-31
summary: "This type of attack leverages the use of tags or variables from a formatted configuration data to cause buffer overflow. The adversary crafts a malicious HTML page or configuration file that includes oversized strings, thus causing an overflow."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/46.html
---

# CAPEC-46: Overflow Variables and Tags

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

This type of attack leverages the use of tags or variables from a formatted configuration data to cause buffer overflow. The adversary crafts a malicious HTML page or configuration file that includes oversized strings, thus causing an overflow.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-20](/wiki/p/weakness/CWE-20), [CWE-74](/wiki/p/weakness/CWE-74), [CWE-118](/wiki/p/weakness/CWE-118), [CWE-119](/wiki/p/weakness/CWE-119), [CWE-120](/wiki/p/weakness/CWE-120), [CWE-680](/wiki/p/weakness/CWE-680), [CWE-697](/wiki/p/weakness/CWE-697), [CWE-733](/wiki/p/weakness/CWE-733)

## Prerequisites

- The target program consumes user-controllable data in the form of tags or variables.
- The target program does not perform sufficient boundary checking.

## Skills required

- Low: An adversary can simply overflow a buffer by inserting a long string into an adversary-modifiable injection vector. The result can be a DoS.
- High: Exploiting a buffer overflow to inject malicious code into the stack of a software system or even the heap can require a higher skill level.

## Consequences

- Availability: Unreliable Execution
- Confidentiality, Integrity, Availability: Execute Unauthorized Commands
- Confidentiality: Read Data
- Integrity: Modify Data

## Mitigations

- Use a language or compiler that performs automatic bounds checking.
- Use an abstraction library to abstract away risky APIs. Not a complete solution.
- Compiler-based canary mechanisms such as StackGuard, ProPolice and the Microsoft Visual Studio /GS flag. Unless this provides automatic bounds checking, it is not a complete solution.
- Use OS-level preventative functionality. Not a complete solution.
- Do not trust input data from user. Validate all user input.

## Source

- [MITRE CAPEC CAPEC-46](https://capec.mitre.org/data/definitions/46.html)
