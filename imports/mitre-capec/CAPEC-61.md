---
slug: attack-pattern/CAPEC-61
title: "CAPEC-61 — Session Fixation"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-61]
cwe_ids: [CWE-384, CWE-664, CWE-732]
related: [weakness/CWE-384, weakness/CWE-664, weakness/CWE-732]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-61
updated_at: 2026-08-31
summary: "The attacker induces a client to establish a session with the target software using a session identifier provided by the attacker. Once the user successfully authenticates to the target software, the attacker uses the (now privileged) session identifier in their own transactions.…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/61.html
---

# CAPEC-61: Session Fixation

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

The attacker induces a client to establish a session with the target software using a session identifier provided by the attacker. Once the user successfully authenticates to the target software, the attacker uses the (now privileged) session identifier in their own transactions. This attack leverages the fact that the target software either relies on client-generated session identifiers or maintains the same session identifiers after privilege elevation.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-384](/wiki/p/weakness/CWE-384), [CWE-664](/wiki/p/weakness/CWE-664), [CWE-732](/wiki/p/weakness/CWE-732)

## Prerequisites

- Session identifiers that remain unchanged when the privilege levels change.
- Permissive session management mechanism that accepts random user-generated session identifiers
- Predictable session identifiers

## Skills required

- Low: Only basic skills are required to determine and fixate session identifiers in a user's browser. Subsequent attacks may require greater skill levels depending on the attackers' motives.

## Consequences

- Confidentiality, Access Control, Authorization: Gain Privileges

## Mitigations

- Use a strict session management mechanism that only accepts locally generated session identifiers: This prevents attackers from fixating session identifiers of their own choice.
- Regenerate and destroy session identifiers when there is a change in the level of privilege: This ensures that even though a potential victim may have followed a link with a fixated identifier, a new one is issued when the level of privilege changes.
- Use session identifiers that are difficult to guess or brute-force: One way for the attackers to obtain valid session identifiers is by brute-forcing or guessing them. By choosing session identifiers that are sufficiently random, brute-forcing or guessing becomes very difficult.

## Source

- [MITRE CAPEC CAPEC-61](https://capec.mitre.org/data/definitions/61.html)
