---
slug: attack-pattern/CAPEC-237
title: "CAPEC-237 — Escaping a Sandbox by Calling Code in Another Language"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-237]
cwe_ids: [CWE-693]
related: [weakness/CWE-693]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-237
updated_at: 2026-08-31
summary: "The attacker may submit malicious code of another language to obtain access to privileges that were not intentionally exposed by the sandbox, thus escaping the sandbox. For instance, Java code cannot perform unsafe operations, such as modifying arbitrary memory locations, due to …"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/237.html
---

# CAPEC-237: Escaping a Sandbox by Calling Code in Another Language

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Very High |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

The attacker may submit malicious code of another language to obtain access to privileges that were not intentionally exposed by the sandbox, thus escaping the sandbox. For instance, Java code cannot perform unsafe operations, such as modifying arbitrary memory locations, due to restrictions placed on it by the Byte code Verifier and the JVM. If allowed, Java code can call directly into native C code, which may perform unsafe operations, such as call system calls and modify arbitrary memory locations on their behalf. To provide isolation, Java does not grant untrusted code with unmediated access to native C code. Instead, the sandboxed code is typically allowed to call some subset of the pre-existing native code that is part of standard libraries.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-693](/wiki/p/weakness/CWE-693)

## Skills required

- High: The attacker must have a good knowledge of the platform specific mechanisms of signing and verifying code. Most code signing and verification schemes are based on use of cryptography, the attacker needs to have an understand of these cryptographic operations in good detail.

## Consequences

- Access Control, Authorization: Bypass Protection Mechanism
- Authorization: Execute Unauthorized Commands
- Accountability, Authentication, Authorization, Non-Repudiation: Gain Privileges

## Mitigations

- Assurance: Sanitize the code of the standard libraries to make sure there is no security weaknesses in them.
- Design: Use obfuscation and other techniques to prevent reverse engineering the standard libraries.
- Assurance: Use static analysis tool to do code review and dynamic tool to do penetration test on the standard library.
- Configuration: Get latest updates for the computer.

## Source

- [MITRE CAPEC CAPEC-237](https://capec.mitre.org/data/definitions/237.html)
