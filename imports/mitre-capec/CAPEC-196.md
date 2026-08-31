---
slug: attack-pattern/CAPEC-196
title: "CAPEC-196 — Session Credential Falsification through Forging"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-196]
cwe_ids: [CWE-384, CWE-664]
mitre_ids: [T1134.002, T1134.003, T1606]
related: [weakness/CWE-384, weakness/CWE-664, technique/T1134.002, technique/T1134.003, technique/T1606]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-196
updated_at: 2026-08-31
summary: "An attacker creates a false but functional session credential in order to gain or usurp access to a service. Session credentials allow users to identify themselves to a service after an initial authentication without needing to resend the authentication information (usually a use…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/196.html
---

# CAPEC-196: Session Credential Falsification through Forging

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker creates a false but functional session credential in order to gain or usurp access to a service. Session credentials allow users to identify themselves to a service after an initial authentication without needing to resend the authentication information (usually a username and password) with every message. If an attacker is able to forge valid session credentials they may be able to bypass authentication or piggy-back off some other authenticated user's session. This attack differs from Reuse of Session IDs and Session Sidejacking attacks in that in the latter attacks an attacker uses a previous or existing credential without modification while, in a forging attack, the attacker must create their own credential, although it may be based on previously observed credentials.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-384](/wiki/p/weakness/CWE-384), [CWE-664](/wiki/p/weakness/CWE-664)

**ATT&CK techniques:** [T1134.002](/wiki/p/technique/T1134.002), [T1134.003](/wiki/p/technique/T1134.003), [T1606](/wiki/p/technique/T1606)

## Prerequisites

- The targeted application must use session credentials to identify legitimate users. Session identifiers that remains unchanged when the privilege levels change. Predictable session identifiers.

## Skills required

- Medium: Forge the session credential and reply the request.

## Consequences

- Integrity: Modify Data
- Confidentiality: Read Data
- Authorization: Execute Unauthorized Commands
- Accountability, Authentication, Authorization, Non-Repudiation: Gain Privileges
- Access Control, Authorization: Bypass Protection Mechanism

## Mitigations

- Implementation: Use session IDs that are difficult to guess or brute-force: One way for the attackers to obtain valid session IDs is by brute-forcing or guessing them. By choosing session identifiers that are sufficiently random, brute-forcing or guessing becomes very difficult.
- Implementation: Regenerate and destroy session identifiers when there is a change in the level of privilege: This ensures that even though a potential victim may have followed a link with a fixated identifier, a new one is issued when the level of privilege changes.

## Source

- [MITRE CAPEC CAPEC-196](https://capec.mitre.org/data/definitions/196.html)
