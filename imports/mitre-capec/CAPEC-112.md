---
slug: attack-pattern/CAPEC-112
title: "CAPEC-112 — Brute Force"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-112]
cwe_ids: [CWE-326, CWE-330, CWE-521]
mitre_ids: [T1110]
related: [weakness/CWE-326, weakness/CWE-330, weakness/CWE-521, technique/T1110]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-112
updated_at: 2026-08-31
summary: "In this attack, some asset (information, functionality, identity, etc.) is protected by a finite secret value. The attacker attempts to gain access to this asset by using trial-and-error to exhaustively explore all the possible secret values in the hope of finding the secret (or …"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/112.html
---

# CAPEC-112: Brute Force

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

In this attack, some asset (information, functionality, identity, etc.) is protected by a finite secret value. The attacker attempts to gain access to this asset by using trial-and-error to exhaustively explore all the possible secret values in the hope of finding the secret (or a value that is functionally equivalent) that will unlock the asset.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-326](/wiki/p/weakness/CWE-326), [CWE-330](/wiki/p/weakness/CWE-330), [CWE-521](/wiki/p/weakness/CWE-521)

**ATT&CK techniques:** [T1110](/wiki/p/technique/T1110)

## Prerequisites

- The attacker must be able to determine when they have successfully guessed the secret. As such, one-time pads are immune to this type of attack since there is no way to determine when a guess is correct.

## Skills required

- Low: The attack simply requires basic scripting ability to automate the exploration of the search space. More sophisticated attackers may be able to use more advanced methods to reduce the search space and increase the speed with which the secret is located.

## Consequences

- Confidentiality: Read Data
- Confidentiality, Access Control, Authorization: Gain Privileges

## Mitigations

- Select a provably large secret space for selection of the secret. Provably large means that the procedure by which the secret is selected does not have artifacts that significantly reduce the size of the total secret space.
- Use a secret space that is well known and with no known patterns that may reduce functional size.
- Do not provide the means for an attacker to determine success independently. This forces the attacker to check their guesses against an external authority, which can slow the attack and warn the defender. This mitigation may not be possible if testing material must appear externally, such as with a transmitted cryptotext.

## Source

- [MITRE CAPEC CAPEC-112](https://capec.mitre.org/data/definitions/112.html)
