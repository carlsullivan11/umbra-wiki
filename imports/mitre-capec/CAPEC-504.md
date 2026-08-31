---
slug: attack-pattern/CAPEC-504
title: "CAPEC-504 — Task Impersonation"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-504]
cwe_ids: [CWE-1021]
mitre_ids: [T1036.004]
related: [weakness/CWE-1021, technique/T1036.004]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-504
updated_at: 2026-08-31
summary: "An adversary, through a previously installed malicious application, impersonates an expected or routine task in an attempt to steal sensitive information or leverage a user's privileges."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/504.html
---

# CAPEC-504: Task Impersonation

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | High |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary, through a previously installed malicious application, impersonates an expected or routine task in an attempt to steal sensitive information or leverage a user's privileges.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-1021](/wiki/p/weakness/CWE-1021)

**ATT&CK techniques:** [T1036.004](/wiki/p/technique/T1036.004)

## Prerequisites

- The adversary must already have access to the target system via some means.
- A legitimate task must exist that an adversary can impersonate to glean credentials.
- The user's privileges allow them to execute certain tasks with elevated privileges.

## Skills required

- Low: Once an adversary has gained access to the target system, impersonating a task is trivial.

## Consequences

- Access Control, Authentication: Gain Privileges

## Mitigations

- The only known mitigation to this attack is to avoid installing the malicious application on the device. However, to impersonate a running task the malicious application does need the GET_TASKS permission to be able to query the task list, and being suspicious of applications with that permission can help.

## Source

- [MITRE CAPEC CAPEC-504](https://capec.mitre.org/data/definitions/504.html)
