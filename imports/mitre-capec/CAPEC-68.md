---
slug: attack-pattern/CAPEC-68
title: "CAPEC-68 — Subvert Code-signing Facilities"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-68]
cwe_ids: [CWE-325, CWE-328, CWE-1326]
mitre_ids: [T1553.002]
related: [weakness/CWE-325, weakness/CWE-328, weakness/CWE-1326, technique/T1553.002]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-68
updated_at: 2026-08-31
summary: "Many languages use code signing facilities to vouch for code's identity and to thus tie code to its assigned privileges within an environment. Subverting this mechanism can be instrumental in an attacker escalating privilege. Any means of subverting the way that a virtual machine…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/68.html
---

# CAPEC-68: Subvert Code-signing Facilities

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Very High |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

Many languages use code signing facilities to vouch for code's identity and to thus tie code to its assigned privileges within an environment. Subverting this mechanism can be instrumental in an attacker escalating privilege. Any means of subverting the way that a virtual machine enforces code signing classifies for this style of attack.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-325](/wiki/p/weakness/CWE-325), [CWE-328](/wiki/p/weakness/CWE-328), [CWE-1326](/wiki/p/weakness/CWE-1326)

**ATT&CK techniques:** [T1553.002](/wiki/p/technique/T1553.002)

## Prerequisites

- A framework-based language that supports code signing (such as, and most commonly, Java or .NET)
- Deployed code that has been signed by its authoring vendor, or a partner.
- The attacker will, for most circumstances, also need to be able to place code in the victim container. This does not necessarily mean that they will have to subvert host-level security, except when explicitly indicated.

## Skills required

- High: Subverting code signing is not a trivial activity. Most code signing and verification schemes are based on use of cryptography and the attacker needs to have an understanding of these cryptographic operations in good detail. Additionally the attacker also needs to be aware of the way memory is assigned and accessed by the container since, often, the only way to subvert code signing would be to patch the code in memory. Finally, a knowledge of the platform specific mechanisms of signing and verifying code is a must.

## Consequences

- Confidentiality, Access Control, Authorization: Gain Privileges

## Mitigations

- A given code signing scheme may be fallible due to improper use of cryptography. Developers must never roll out their own cryptography, nor should existing primitives be modified or ignored.
- If an attacker cannot attack the scheme directly, they might try to alter the environment that affects the signing and verification processes. A possible mitigation is to avoid reliance on flags or environment variables that are user-controllable.

## Source

- [MITRE CAPEC CAPEC-68](https://capec.mitre.org/data/definitions/68.html)
