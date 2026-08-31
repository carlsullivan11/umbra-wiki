---
slug: attack-pattern/CAPEC-92
title: "CAPEC-92 — Forced Integer Overflow"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-92]
cwe_ids: [CWE-120, CWE-122, CWE-128, CWE-190, CWE-196, CWE-680, CWE-697]
related: [weakness/CWE-120, weakness/CWE-122, weakness/CWE-128, weakness/CWE-190, weakness/CWE-196, weakness/CWE-680, weakness/CWE-697]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-92
updated_at: 2026-08-31
summary: "This attack forces an integer variable to go out of range. The integer variable is often used as an offset such as size of memory allocation or similarly. The attacker would typically control the value of such variable and try to get it out of range. For instance the integer in q…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/92.html
---

# CAPEC-92: Forced Integer Overflow

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

This attack forces an integer variable to go out of range. The integer variable is often used as an offset such as size of memory allocation or similarly. The attacker would typically control the value of such variable and try to get it out of range. For instance the integer in question is incremented past the maximum possible value, it may wrap to become a very small, or negative number, therefore providing a very incorrect value which can lead to unexpected behavior. At worst the attacker can execute arbitrary code.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-120](/wiki/p/weakness/CWE-120), [CWE-122](/wiki/p/weakness/CWE-122), [CWE-128](/wiki/p/weakness/CWE-128), [CWE-190](/wiki/p/weakness/CWE-190), [CWE-196](/wiki/p/weakness/CWE-196), [CWE-680](/wiki/p/weakness/CWE-680), [CWE-697](/wiki/p/weakness/CWE-697)

## Prerequisites

- The attacker can manipulate the value of an integer variable utilized by the target host.
- The target host does not do proper range checking on the variable before utilizing it.
- When the integer variable is incremented or decremented to an out of range value, it gets a very different value (e.g. very small or negative number)

## Skills required

- Low: An attacker can simply overflow an integer by inserting an out of range value.
- High: Exploiting a buffer overflow by injecting malicious code into the stack of a software system or even the heap can require a higher skill level.

## Consequences

- Integrity: Modify Data
- Confidentiality, Access Control, Authorization: Gain Privileges
- Confidentiality, Integrity, Availability: Execute Unauthorized Commands
- Confidentiality: Read Data
- Availability: Unreliable Execution

## Mitigations

- Use a language or compiler that performs automatic bounds checking.
- Carefully review the service's implementation before making it available to user. For instance you can use manual or automated code review to uncover vulnerabilities such as integer overflow.
- Use an abstraction library to abstract away risky APIs. Not a complete solution.
- Always do bound checking before consuming user input data.

## Source

- [MITRE CAPEC CAPEC-92](https://capec.mitre.org/data/definitions/92.html)
