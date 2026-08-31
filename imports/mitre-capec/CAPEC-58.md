---
slug: attack-pattern/CAPEC-58
title: "CAPEC-58 — Restful Privilege Elevation"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-58]
cwe_ids: [CWE-267, CWE-269]
related: [weakness/CWE-267, weakness/CWE-269]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-58
updated_at: 2026-08-31
summary: "An adversary identifies a Rest HTTP (Get, Put, Delete) style permission method allowing them to perform various malicious actions upon server data due to lack of access control mechanisms implemented within the application service accepting HTTP messages."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/58.html
---

# CAPEC-58: Restful Privilege Elevation

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary identifies a Rest HTTP (Get, Put, Delete) style permission method allowing them to perform various malicious actions upon server data due to lack of access control mechanisms implemented within the application service accepting HTTP messages.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-267](/wiki/p/weakness/CWE-267), [CWE-269](/wiki/p/weakness/CWE-269)

## Prerequisites

- The attacker needs to be able to identify HTTP Get URLs. The Get methods must be set to call applications that perform operations other than get such as update and delete.

## Skills required

- Low: It is relatively straightforward to identify an HTTP Get method that changes state on the server side and executes against an over-privileged system interface

## Consequences

- Integrity: Modify Data
- Confidentiality, Access Control, Authorization: Gain Privileges

## Mitigations

- Design: Enforce principle of least privilege
- Implementation: Ensure that HTTP Get methods only retrieve state and do not alter state on the server side
- Implementation: Ensure that HTTP methods have proper ACLs based on what the functionality they expose

## Source

- [MITRE CAPEC CAPEC-58](https://capec.mitre.org/data/definitions/58.html)
