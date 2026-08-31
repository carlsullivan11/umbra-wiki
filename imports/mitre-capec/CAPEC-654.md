---
slug: attack-pattern/CAPEC-654
title: "CAPEC-654 — Credential Prompt Impersonation"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-654]
cwe_ids: [CWE-1021]
mitre_ids: [T1056, T1548.004]
related: [weakness/CWE-1021, technique/T1056, technique/T1548.004]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-654
updated_at: 2026-08-31
summary: "An adversary, through a previously installed malicious application, impersonates a credential prompt in an attempt to steal a user's credentials."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/654.html
---

# CAPEC-654: Credential Prompt Impersonation

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | High |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary, through a previously installed malicious application, impersonates a credential prompt in an attempt to steal a user's credentials.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-1021](/wiki/p/weakness/CWE-1021)

**ATT&CK techniques:** [T1056](/wiki/p/technique/T1056), [T1548.004](/wiki/p/technique/T1548.004)

## Prerequisites

- The adversary must already have access to the target system via some means.
- A legitimate task must exist that an adversary can impersonate to glean credentials.

## Skills required

- Low: Once an adversary has gained access to the target system, impersonating a credential prompt is not difficult.

## Consequences

- Access Control, Authentication: Gain Privileges

## Mitigations

- The only known mitigation to this attack is to avoid installing the malicious application on the device. However, to impersonate a running task the malicious application does need the GET_TASKS permission to be able to query the task list, and being suspicious of applications with that permission can help.

## Source

- [MITRE CAPEC CAPEC-654](https://capec.mitre.org/data/definitions/654.html)
