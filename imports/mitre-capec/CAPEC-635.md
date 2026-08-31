---
slug: attack-pattern/CAPEC-635
title: "CAPEC-635 — Alternative Execution Due to Deceptive Filenames"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-635]
cwe_ids: [CWE-162]
mitre_ids: [T1036.007]
related: [weakness/CWE-162, technique/T1036.007]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-635
updated_at: 2026-08-31
summary: "The extension of a file name is often used in various contexts to determine the application that is used to open and use it. If an attacker can cause an alternative application to be used, it may be able to execute malicious code, cause a denial of service or expose sensitive inf…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/635.html
---

# CAPEC-635: Alternative Execution Due to Deceptive Filenames

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

The extension of a file name is often used in various contexts to determine the application that is used to open and use it. If an attacker can cause an alternative application to be used, it may be able to execute malicious code, cause a denial of service or expose sensitive information.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-162](/wiki/p/weakness/CWE-162)

**ATT&CK techniques:** [T1036.007](/wiki/p/technique/T1036.007)

## Prerequisites

- The use of the file must be controlled by the file extension.

## Mitigations

- Applications should insure that the content of the file is consistent with format it is expecting, and not depend solely on the file extension.

## Source

- [MITRE CAPEC CAPEC-635](https://capec.mitre.org/data/definitions/635.html)
