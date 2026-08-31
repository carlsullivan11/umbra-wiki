---
slug: attack-pattern/CAPEC-639
title: "CAPEC-639 — Probe System Files"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-639]
cwe_ids: [CWE-552]
mitre_ids: [T1039, T1552.001, T1552.003, T1552.004, T1552.006]
related: [weakness/CWE-552, technique/T1039, technique/T1552.001, technique/T1552.003, technique/T1552.004, technique/T1552.006]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-639
updated_at: 2026-08-31
summary: "An adversary obtains unauthorized information due to improperly protected files. If an application stores sensitive information in a file that is not protected by proper access control, then an adversary can access the file and search for sensitive information."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/639.html
---

# CAPEC-639: Probe System Files

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Medium |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary obtains unauthorized information due to improperly protected files. If an application stores sensitive information in a file that is not protected by proper access control, then an adversary can access the file and search for sensitive information.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-552](/wiki/p/weakness/CWE-552)

**ATT&CK techniques:** [T1039](/wiki/p/technique/T1039), [T1552.001](/wiki/p/technique/T1552.001), [T1552.003](/wiki/p/technique/T1552.003), [T1552.004](/wiki/p/technique/T1552.004), [T1552.006](/wiki/p/technique/T1552.006)

## Prerequisites

- An adversary has access to the file system of a system.

## Consequences

- Confidentiality: Read Data

## Mitigations

- Verify that files have proper access controls set, and reduce the storage of sensitive information to only what is necessary.

## Source

- [MITRE CAPEC CAPEC-639](https://capec.mitre.org/data/definitions/639.html)
