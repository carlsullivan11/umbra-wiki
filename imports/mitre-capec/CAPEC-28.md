---
slug: attack-pattern/CAPEC-28
title: "CAPEC-28 — Fuzzing"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-28]
cwe_ids: [CWE-20, CWE-74]
related: [weakness/CWE-20, weakness/CWE-74]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-28
updated_at: 2026-08-31
summary: "In this attack pattern, the adversary leverages fuzzing to try to identify weaknesses in the system. Fuzzing is a software security and functionality testing method that feeds randomly constructed input to the system and looks for an indication that a failure in response to that …"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/28.html
---

# CAPEC-28: Fuzzing

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

In this attack pattern, the adversary leverages fuzzing to try to identify weaknesses in the system. Fuzzing is a software security and functionality testing method that feeds randomly constructed input to the system and looks for an indication that a failure in response to that input has occurred. Fuzzing treats the system as a black box and is totally free from any preconceptions or assumptions about the system. Fuzzing can help an attacker discover certain assumptions made about user input in the system. Fuzzing gives an attacker a quick way of potentially uncovering some of these assumptions despite not necessarily knowing anything about the internals of the system. These assumptions can then be turned against the system by specially crafting user input that may allow an attacker to achieve their goals.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-20](/wiki/p/weakness/CWE-20), [CWE-74](/wiki/p/weakness/CWE-74)

## Skills required

- Low: There is a wide variety of fuzzing tools available.

## Consequences

- Integrity: Modify Data
- Availability: Unreliable Execution
- Confidentiality: Read Data
- Confidentiality, Access Control, Authorization: Gain Privileges
- Confidentiality, Integrity, Availability: Alter Execution Logic

## Mitigations

- Test to ensure that the software behaves as per specification and that there are no unintended side effects. Ensure that no assumptions about the validity of data are made.
- Use fuzz testing during the software QA process to uncover any surprises, uncover any assumptions or unexpected behavior.

## Source

- [MITRE CAPEC CAPEC-28](https://capec.mitre.org/data/definitions/28.html)
