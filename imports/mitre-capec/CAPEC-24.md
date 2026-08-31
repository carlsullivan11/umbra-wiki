---
slug: attack-pattern/CAPEC-24
title: "CAPEC-24 — Filter Failure through Buffer Overflow"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-24]
cwe_ids: [CWE-20, CWE-74, CWE-118, CWE-119, CWE-120, CWE-680, CWE-697, CWE-733]
related: [weakness/CWE-20, weakness/CWE-74, weakness/CWE-118, weakness/CWE-119, weakness/CWE-120, weakness/CWE-680, weakness/CWE-697, weakness/CWE-733]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-24
updated_at: 2026-08-31
summary: "In this attack, the idea is to cause an active filter to fail by causing an oversized transaction. An attacker may try to feed overly long input strings to the program in an attempt to overwhelm the filter (by causing a buffer overflow) and hoping that the filter does not fail se…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/24.html
---

# CAPEC-24: Filter Failure through Buffer Overflow

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

In this attack, the idea is to cause an active filter to fail by causing an oversized transaction. An attacker may try to feed overly long input strings to the program in an attempt to overwhelm the filter (by causing a buffer overflow) and hoping that the filter does not fail securely (i.e. the user input is let into the system unfiltered).

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-20](/wiki/p/weakness/CWE-20), [CWE-74](/wiki/p/weakness/CWE-74), [CWE-118](/wiki/p/weakness/CWE-118), [CWE-119](/wiki/p/weakness/CWE-119), [CWE-120](/wiki/p/weakness/CWE-120), [CWE-680](/wiki/p/weakness/CWE-680), [CWE-697](/wiki/p/weakness/CWE-697), [CWE-733](/wiki/p/weakness/CWE-733)

## Prerequisites

- Ability to control the length of data passed to an active filter.

## Skills required

- Low: An attacker can simply overflow a buffer by inserting a long string into an attacker-modifiable injection vector. The result can be a DoS.
- High: Exploiting a buffer overflow to inject malicious code into the stack of a software system or even the heap can require a higher skill level.

## Consequences

- Integrity: Modify Data
- Confidentiality, Integrity, Availability: Execute Unauthorized Commands
- Confidentiality, Access Control, Authorization: Bypass Protection Mechanism
- Availability: Unreliable Execution

## Mitigations

- Make sure that ANY failure occurring in the filtering or input validation routine is properly handled and that offending input is NOT allowed to go through. Basically make sure that the vault is closed when failure occurs.
- Pre-design: Use a language or compiler that performs automatic bounds checking.
- Pre-design through Build: Compiler-based canary mechanisms such as StackGuard, ProPolice and the Microsoft Visual Studio /GS flag. Unless this provides automatic bounds checking, it is not a complete solution.
- Operational: Use OS-level preventative functionality. Not a complete solution.
- Design: Use an abstraction library to abstract away risky APIs. Not a complete solution.

## Source

- [MITRE CAPEC CAPEC-24](https://capec.mitre.org/data/definitions/24.html)
