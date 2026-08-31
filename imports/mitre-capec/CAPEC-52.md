---
slug: attack-pattern/CAPEC-52
title: "CAPEC-52 — Embedding NULL Bytes"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-52]
cwe_ids: [CWE-20, CWE-74, CWE-158, CWE-172, CWE-173, CWE-697, CWE-707]
related: [weakness/CWE-20, weakness/CWE-74, weakness/CWE-158, weakness/CWE-172, weakness/CWE-173, weakness/CWE-697, weakness/CWE-707]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-52
updated_at: 2026-08-31
summary: "An adversary embeds one or more null bytes in input to the target software. This attack relies on the usage of a null-valued byte as a string terminator in many environments. The goal is for certain components of the target software to stop processing the input when it encounters…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/52.html
---

# CAPEC-52: Embedding NULL Bytes

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary embeds one or more null bytes in input to the target software. This attack relies on the usage of a null-valued byte as a string terminator in many environments. The goal is for certain components of the target software to stop processing the input when it encounters the null byte(s).

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-20](/wiki/p/weakness/CWE-20), [CWE-74](/wiki/p/weakness/CWE-74), [CWE-158](/wiki/p/weakness/CWE-158), [CWE-172](/wiki/p/weakness/CWE-172), [CWE-173](/wiki/p/weakness/CWE-173), [CWE-697](/wiki/p/weakness/CWE-697), [CWE-707](/wiki/p/weakness/CWE-707)

## Prerequisites

- The program does not properly handle postfix NULL terminators

## Skills required

- Medium: Directory traversal
- High: Execution of arbitrary code

## Consequences

- Integrity: Modify Data
- Confidentiality: Read Data
- Confidentiality, Access Control, Authorization: Gain Privileges
- Confidentiality, Integrity, Availability: Execute Unauthorized Commands

## Mitigations

- Properly handle the NULL characters supplied as part of user input prior to doing anything with the data.

## Source

- [MITRE CAPEC CAPEC-52](https://capec.mitre.org/data/definitions/52.html)
