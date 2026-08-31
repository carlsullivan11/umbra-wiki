---
slug: attack-pattern/CAPEC-680
title: "CAPEC-680 — Exploitation of Improperly Controlled Registers"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-680]
cwe_ids: [CWE-1224, CWE-1231, CWE-1233, CWE-1262, CWE-1283]
related: [weakness/CWE-1224, weakness/CWE-1231, weakness/CWE-1233, weakness/CWE-1262, weakness/CWE-1283]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-680
updated_at: 2026-08-31
summary: "An adversary exploits missing or incorrectly configured access control within registers to read/write data that is not meant to be obtained or modified by a user."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/680.html
---

# CAPEC-680: Exploitation of Improperly Controlled Registers

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary exploits missing or incorrectly configured access control within registers to read/write data that is not meant to be obtained or modified by a user.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-1224](/wiki/p/weakness/CWE-1224), [CWE-1231](/wiki/p/weakness/CWE-1231), [CWE-1233](/wiki/p/weakness/CWE-1233), [CWE-1262](/wiki/p/weakness/CWE-1262), [CWE-1283](/wiki/p/weakness/CWE-1283)

## Prerequisites

- Awareness of the hardware being leveraged.
- Access to the hardware being leveraged.

## Skills required

- High: Intricate knowledge of registers.

## Consequences

- Integrity: Modify Data
- Confidentiality: Read Data

## Mitigations

- Design proper access control policies for hardware register access from software and ensure these policies are implemented in accordance with the specified design.
- Ensure security lock bit protections are reviewed for design inconsistencies and common weaknesses.
- Test security lock programming flow in both pre-silicon and post-silicon environments.
- Leverage automated tools to test that values are not reprogrammable and that write-once fields lock on writing zeros.
- Ensure that measurement data is stored in registers that are read-only or otherwise have access controls that prevent modification by an untrusted agent.

## Source

- [MITRE CAPEC CAPEC-680](https://capec.mitre.org/data/definitions/680.html)
