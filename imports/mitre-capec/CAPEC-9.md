---
slug: attack-pattern/CAPEC-9
title: "CAPEC-9 — Buffer Overflow in Local Command-Line Utilities"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-9]
cwe_ids: [CWE-20, CWE-74, CWE-118, CWE-119, CWE-120, CWE-680, CWE-697, CWE-733]
related: [weakness/CWE-20, weakness/CWE-74, weakness/CWE-118, weakness/CWE-119, weakness/CWE-120, weakness/CWE-680, weakness/CWE-697, weakness/CWE-733]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-9
updated_at: 2026-08-31
summary: "This attack targets command-line utilities available in a number of shells. An adversary can leverage a vulnerability found in a command-line utility to escalate privilege to root."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/9.html
---

# CAPEC-9: Buffer Overflow in Local Command-Line Utilities

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

This attack targets command-line utilities available in a number of shells. An adversary can leverage a vulnerability found in a command-line utility to escalate privilege to root.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-20](/wiki/p/weakness/CWE-20), [CWE-74](/wiki/p/weakness/CWE-74), [CWE-118](/wiki/p/weakness/CWE-118), [CWE-119](/wiki/p/weakness/CWE-119), [CWE-120](/wiki/p/weakness/CWE-120), [CWE-680](/wiki/p/weakness/CWE-680), [CWE-697](/wiki/p/weakness/CWE-697), [CWE-733](/wiki/p/weakness/CWE-733)

## Prerequisites

- The target host exposes a command-line utility to the user.
- The command-line utility exposed by the target host has a buffer overflow vulnerability that can be exploited.

## Skills required

- Low: An adversary can simply overflow a buffer by inserting a long string into an adversary-modifiable injection vector. The result can be a DoS.
- High: Exploiting a buffer overflow to inject malicious code into the stack of a software system or even the heap can require a higher skill level.

## Consequences

- Confidentiality, Access Control, Authorization: Gain Privileges
- Confidentiality, Integrity, Availability: Execute Unauthorized Commands
- Integrity: Modify Data
- Availability: Unreliable Execution
- Confidentiality: Read Data

## Mitigations

- Carefully review the service's implementation before making it available to user. For instance you can use manual or automated code review to uncover vulnerabilities such as buffer overflow.
- Use a language or compiler that performs automatic bounds checking.
- Use an abstraction library to abstract away risky APIs. Not a complete solution.
- Compiler-based canary mechanisms such as StackGuard, ProPolice and the Microsoft Visual Studio /GS flag. Unless this provides automatic bounds checking, it is not a complete solution.
- Operational: Use OS-level preventative functionality. Not a complete solution.
- Apply the latest patches to your user exposed services. This may not be a complete solution, especially against a zero day attack.
- Do not unnecessarily expose services.

## Source

- [MITRE CAPEC CAPEC-9](https://capec.mitre.org/data/definitions/9.html)
