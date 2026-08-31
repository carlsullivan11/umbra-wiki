---
slug: attack-pattern/CAPEC-2
title: "CAPEC-2 — Inducing Account Lockout"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-2]
cwe_ids: [CWE-645]
mitre_ids: [T1531]
related: [weakness/CWE-645, technique/T1531]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-2
updated_at: 2026-08-31
summary: "An attacker leverages the security functionality of the system aimed at thwarting potential attacks to launch a denial of service attack against a legitimate system user. Many systems, for instance, implement a password throttling mechanism that locks an account after a certain n…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/2.html
---

# CAPEC-2: Inducing Account Lockout

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker leverages the security functionality of the system aimed at thwarting potential attacks to launch a denial of service attack against a legitimate system user. Many systems, for instance, implement a password throttling mechanism that locks an account after a certain number of incorrect log in attempts. An attacker can leverage this throttling mechanism to lock a legitimate user out of their own account. The weakness that is being leveraged by an attacker is the very security feature that has been put in place to counteract attacks.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-645](/wiki/p/weakness/CWE-645)

**ATT&CK techniques:** [T1531](/wiki/p/technique/T1531)

## Prerequisites

- The system has a lockout mechanism.
- An attacker must be able to reproduce behavior that would result in an account being locked.

## Skills required

- Low: No programming skills or computer knowledge is needed. An attacker can easily use this attack pattern following the Execution Flow above.

## Consequences

- Availability: Resource Consumption

## Mitigations

- Implement intelligent password throttling mechanisms such as those which take IP address into account, in addition to the login name.
- When implementing security features, consider how they can be misused and made to turn on themselves.

## Source

- [MITRE CAPEC CAPEC-2](https://capec.mitre.org/data/definitions/2.html)
