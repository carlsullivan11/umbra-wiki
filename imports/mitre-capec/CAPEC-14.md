---
slug: attack-pattern/CAPEC-14
title: "CAPEC-14 — Client-side Injection-induced Buffer Overflow"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-14]
cwe_ids: [CWE-20, CWE-74, CWE-118, CWE-119, CWE-120, CWE-353, CWE-680, CWE-697]
related: [weakness/CWE-20, weakness/CWE-74, weakness/CWE-118, weakness/CWE-119, weakness/CWE-120, weakness/CWE-353, weakness/CWE-680, weakness/CWE-697]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-14
updated_at: 2026-08-31
summary: "This type of attack exploits a buffer overflow vulnerability in targeted client software through injection of malicious content from a custom-built hostile service. This hostile service is created to deliver the correct content to the client software. For example, if the client-s…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/14.html
---

# CAPEC-14: Client-side Injection-induced Buffer Overflow

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

This type of attack exploits a buffer overflow vulnerability in targeted client software through injection of malicious content from a custom-built hostile service. This hostile service is created to deliver the correct content to the client software. For example, if the client-side application is a browser, the service will host a webpage that the browser loads.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-20](/wiki/p/weakness/CWE-20), [CWE-74](/wiki/p/weakness/CWE-74), [CWE-118](/wiki/p/weakness/CWE-118), [CWE-119](/wiki/p/weakness/CWE-119), [CWE-120](/wiki/p/weakness/CWE-120), [CWE-353](/wiki/p/weakness/CWE-353), [CWE-680](/wiki/p/weakness/CWE-680), [CWE-697](/wiki/p/weakness/CWE-697)

## Prerequisites

- The targeted client software communicates with an external server.
- The targeted client software has a buffer overflow vulnerability.

## Skills required

- Low: To achieve a denial of service, an attacker can simply overflow a buffer by inserting a long string into an attacker-modifiable injection vector.
- High: Exploiting a buffer overflow to inject malicious code into the stack of a software system or even the heap requires a more in-depth knowledge and higher skill level.

## Consequences

- Confidentiality: Read Data
- Integrity: Modify Data
- Availability: Resource Consumption
- Confidentiality, Integrity, Availability: Execute Unauthorized Commands

## Mitigations

- The client software should not install untrusted code from a non-authenticated server.
- The client software should have the latest patches and should be audited for vulnerabilities before being used to communicate with potentially hostile servers.
- Perform input validation for length of buffer inputs.
- Use a language or compiler that performs automatic bounds checking.
- Use an abstraction library to abstract away risky APIs. Not a complete solution.
- Compiler-based canary mechanisms such as StackGuard, ProPolice and the Microsoft Visual Studio /GS flag. Unless this provides automatic bounds checking, it is not a complete solution.
- Ensure all buffer uses are consistently bounds-checked.
- Use OS-level preventative functionality. Not a complete solution.

## Source

- [MITRE CAPEC CAPEC-14](https://capec.mitre.org/data/definitions/14.html)
