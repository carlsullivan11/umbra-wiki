---
slug: attack-pattern/CAPEC-96
title: "CAPEC-96 — Block Access to Libraries"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-96]
cwe_ids: [CWE-589]
related: [weakness/CWE-589]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-96
updated_at: 2026-08-31
summary: "An application typically makes calls to functions that are a part of libraries external to the application. These libraries may be part of the operating system or they may be third party libraries. It is possible that the application does not handle situations properly where acce…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/96.html
---

# CAPEC-96: Block Access to Libraries

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An application typically makes calls to functions that are a part of libraries external to the application. These libraries may be part of the operating system or they may be third party libraries. It is possible that the application does not handle situations properly where access to these libraries has been blocked. Depending on the error handling within the application, blocked access to libraries may leave the system in an insecure state that could be leveraged by an attacker.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-589](/wiki/p/weakness/CWE-589)

## Prerequisites

- An application requires access to external libraries.
- An attacker has the privileges to block application access to external libraries.

## Skills required

- Low: Knowledge of how to block access to libraries, as well as knowledge of how to leverage the resulting state of the application based on the failed call.

## Consequences

- Availability: Alter Execution Logic
- Confidentiality: Other
- Confidentiality, Access Control, Authorization: Bypass Protection Mechanism

## Mitigations

- Ensure that application handles situations where access to APIs in external libraries is not available securely. If the application cannot continue its execution safely it should fail in a consistent and secure fashion.

## Source

- [MITRE CAPEC CAPEC-96](https://capec.mitre.org/data/definitions/96.html)
