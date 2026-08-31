---
slug: attack-pattern/CAPEC-216
title: "CAPEC-216 — Communication Channel Manipulation"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-216]
cwe_ids: [CWE-306]
related: [weakness/CWE-306]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-216
updated_at: 2026-08-31
summary: "An adversary manipulates a setting or parameter on communications channel in order to compromise its security. This can result in information exposure, insertion/removal of information from the communications stream, and/or potentially system compromise."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/216.html
---

# CAPEC-216: Communication Channel Manipulation

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | — |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary manipulates a setting or parameter on communications channel in order to compromise its security. This can result in information exposure, insertion/removal of information from the communications stream, and/or potentially system compromise.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-306](/wiki/p/weakness/CWE-306)

## Prerequisites

- The target application must leverage an open communications channel.
- The channel on which the target communicates must be vulnerable to interception (e.g., adversary in the middle attack - CAPEC-94).

## Consequences

- Integrity: Read Data, Modify Data, Other
- Confidentiality: Read Data

## Mitigations

- Encrypt all sensitive communications using properly-configured cryptography.
- Design the communication system such that it associates proper authentication/authorization with each channel/message.

## Source

- [MITRE CAPEC CAPEC-216](https://capec.mitre.org/data/definitions/216.html)
