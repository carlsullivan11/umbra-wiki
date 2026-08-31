---
slug: attack-pattern/CAPEC-701
title: "CAPEC-701 — Browser in the Middle (BiTM)"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-701]
cwe_ids: [CWE-294, CWE-345]
related: [weakness/CWE-294, weakness/CWE-345]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-701
updated_at: 2026-08-31
summary: "An adversary exploits the inherent functionalities of a web browser, in order to establish an unnoticed remote desktop connection in the victim's browser to the adversary's system. The adversary must deploy a web client with a remote desktop session that the victim can access."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/701.html
---

# CAPEC-701: Browser in the Middle (BiTM)

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary exploits the inherent functionalities of a web browser, in order to establish an unnoticed remote desktop connection in the victim's browser to the adversary's system. The adversary must deploy a web client with a remote desktop session that the victim can access.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-294](/wiki/p/weakness/CWE-294), [CWE-345](/wiki/p/weakness/CWE-345)

## Prerequisites

- The adversary must create a convincing web client to establish the connection. The victim then needs to be lured onto the adversary's webpage. In addition, the victim's machine must not use local authentication APIs, a hardware token, or a Trusted Platform Module (TPM) to authenticate.

## Skills required

- Medium: 

## Consequences

- Confidentiality, Access Control, Authentication: Gain Privileges
- Confidentiality, Authorization: Read Data
- Integrity: Modify Data

## Mitigations

- Implementation: Use strong, mutual authentication to fully authenticate with both ends of any communications channel

## Source

- [MITRE CAPEC CAPEC-701](https://capec.mitre.org/data/definitions/701.html)
