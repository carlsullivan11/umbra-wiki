---
slug: attack-pattern/CAPEC-10
title: "CAPEC-10 — Buffer Overflow via Environment Variables"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-10]
cwe_ids: [CWE-20, CWE-74, CWE-99, CWE-118, CWE-119, CWE-120, CWE-302, CWE-680, CWE-697, CWE-733]
related: [weakness/CWE-20, weakness/CWE-74, weakness/CWE-99, weakness/CWE-118, weakness/CWE-119, weakness/CWE-120, weakness/CWE-302, weakness/CWE-680, weakness/CWE-697, weakness/CWE-733]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-10
updated_at: 2026-08-31
summary: "This attack pattern involves causing a buffer overflow through manipulation of environment variables. Once the adversary finds that they can modify an environment variable, they may try to overflow associated buffers. This attack leverages implicit trust often placed in environme…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/10.html
---

# CAPEC-10: Buffer Overflow via Environment Variables

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

This attack pattern involves causing a buffer overflow through manipulation of environment variables. Once the adversary finds that they can modify an environment variable, they may try to overflow associated buffers. This attack leverages implicit trust often placed in environment variables.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-20](/wiki/p/weakness/CWE-20), [CWE-74](/wiki/p/weakness/CWE-74), [CWE-99](/wiki/p/weakness/CWE-99), [CWE-118](/wiki/p/weakness/CWE-118), [CWE-119](/wiki/p/weakness/CWE-119), [CWE-120](/wiki/p/weakness/CWE-120), [CWE-302](/wiki/p/weakness/CWE-302), [CWE-680](/wiki/p/weakness/CWE-680), [CWE-697](/wiki/p/weakness/CWE-697), [CWE-733](/wiki/p/weakness/CWE-733)

## Prerequisites

- The application uses environment variables.
- An environment variable exposed to the user is vulnerable to a buffer overflow.
- The vulnerable environment variable uses untrusted data.
- Tainted data used in the environment variables is not properly validated. For instance boundary checking is not done before copying the input data to a buffer.

## Skills required

- Low: An attacker can simply overflow a buffer by inserting a long string into an attacker-modifiable injection vector. The result can be a DoS.
- High: Exploiting a buffer overflow to inject malicious code into the stack of a software system or even the heap can require a higher skill level.

## Consequences

- Availability: Unreliable Execution
- Confidentiality, Integrity, Availability: Execute Unauthorized Commands
- Confidentiality: Read Data
- Integrity: Modify Data
- Confidentiality, Access Control, Authorization: Gain Privileges

## Mitigations

- Do not expose environment variable to the user.
- Do not use untrusted data in your environment variables.
- Use a language or compiler that performs automatic bounds checking
- There are tools such as Sharefuzz [REF-2] which is an environment variable fuzzer for Unix that support loading a shared library. You can use Sharefuzz to determine if you are exposing an environment variable vulnerable to buffer overflow.

## Source

- [MITRE CAPEC CAPEC-10](https://capec.mitre.org/data/definitions/10.html)
