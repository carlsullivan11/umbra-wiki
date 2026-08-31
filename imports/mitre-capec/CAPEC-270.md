---
slug: attack-pattern/CAPEC-270
title: "CAPEC-270 — Modification of Registry Run Keys"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-270]
cwe_ids: [CWE-15]
mitre_ids: [T1547.001, T1547.014]
related: [weakness/CWE-15, technique/T1547.001, technique/T1547.014]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-270
updated_at: 2026-08-31
summary: "An adversary adds a new entry to the 'run keys' in the Windows registry so that an application of their choosing is executed when a user logs in. In this way, the adversary can get their executable to operate and run on the target system with the authorized user's level of permis…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/270.html
---

# CAPEC-270: Modification of Registry Run Keys

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Medium |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary adds a new entry to the "run keys" in the Windows registry so that an application of their choosing is executed when a user logs in. In this way, the adversary can get their executable to operate and run on the target system with the authorized user's level of permissions. This attack is a good way for an adversary to run persistent spyware on a user's machine, such as a keylogger.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-15](/wiki/p/weakness/CWE-15)

**ATT&CK techniques:** [T1547.001](/wiki/p/technique/T1547.001), [T1547.014](/wiki/p/technique/T1547.014)

## Prerequisites

- The adversary must have gained access to the target system via physical or logical means in order to carry out this attack.

## Consequences

- Integrity: Modify Data, Gain Privileges

## Mitigations

- Identify programs that may be used to acquire process information and block them by using a software restriction policy or tools that restrict program execution by using a process allowlist.

## Source

- [MITRE CAPEC CAPEC-270](https://capec.mitre.org/data/definitions/270.html)
