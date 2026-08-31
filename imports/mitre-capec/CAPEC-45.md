---
slug: attack-pattern/CAPEC-45
title: "CAPEC-45 — Buffer Overflow via Symbolic Links"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-45]
cwe_ids: [CWE-20, CWE-74, CWE-118, CWE-119, CWE-120, CWE-285, CWE-302, CWE-680, CWE-697]
related: [weakness/CWE-20, weakness/CWE-74, weakness/CWE-118, weakness/CWE-119, weakness/CWE-120, weakness/CWE-285, weakness/CWE-302, weakness/CWE-680, weakness/CWE-697]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-45
updated_at: 2026-08-31
summary: "This type of attack leverages the use of symbolic links to cause buffer overflows. An adversary can try to create or manipulate a symbolic link file such that its contents result in out of bounds data. When the target software processes the symbolic link file, it could potentiall…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/45.html
---

# CAPEC-45: Buffer Overflow via Symbolic Links

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

This type of attack leverages the use of symbolic links to cause buffer overflows. An adversary can try to create or manipulate a symbolic link file such that its contents result in out of bounds data. When the target software processes the symbolic link file, it could potentially overflow internal buffers with insufficient bounds checking.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-20](/wiki/p/weakness/CWE-20), [CWE-74](/wiki/p/weakness/CWE-74), [CWE-118](/wiki/p/weakness/CWE-118), [CWE-119](/wiki/p/weakness/CWE-119), [CWE-120](/wiki/p/weakness/CWE-120), [CWE-285](/wiki/p/weakness/CWE-285), [CWE-302](/wiki/p/weakness/CWE-302), [CWE-680](/wiki/p/weakness/CWE-680), [CWE-697](/wiki/p/weakness/CWE-697)

## Prerequisites

- The adversary can create symbolic link on the target host.
- The target host does not perform correct boundary checking while consuming data from a resources.

## Skills required

- Low: An adversary can simply overflow a buffer by inserting a long string into an adversary-modifiable injection vector. The result can be a DoS.
- High: Exploiting a buffer overflow to inject malicious code into the stack of a software system or even the heap can require a higher skill level.

## Consequences

- Availability: Unreliable Execution
- Confidentiality, Integrity, Availability: Execute Unauthorized Commands
- Confidentiality: Read Data
- Integrity: Modify Data

## Mitigations

- Pay attention to the fact that the resource you read from can be a replaced by a Symbolic link. You can do a Symlink check before reading the file and decide that this is not a legitimate way of accessing the resource.
- Because Symlink can be modified by an adversary, make sure that the ones you read are located in protected directories.
- Pay attention to the resource pointed to by your symlink links (See attack pattern named "Forced Symlink race"), they can be replaced by malicious resources.
- Always check the size of the input data before copying to a buffer.
- Use a language or compiler that performs automatic bounds checking.
- Use an abstraction library to abstract away risky APIs. Not a complete solution.
- Compiler-based canary mechanisms such as StackGuard, ProPolice and the Microsoft Visual Studio /GS flag. Unless this provides automatic bounds checking, it is not a complete solution.
- Use OS-level preventative functionality. Not a complete solution.

## Source

- [MITRE CAPEC CAPEC-45](https://capec.mitre.org/data/definitions/45.html)
