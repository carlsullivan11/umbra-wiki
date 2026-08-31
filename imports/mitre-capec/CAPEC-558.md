---
slug: attack-pattern/CAPEC-558
title: "CAPEC-558 — Replace Trusted Executable"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-558]
cwe_ids: [CWE-284]
mitre_ids: [T1505.005, T1546.008]
related: [weakness/CWE-284, technique/T1505.005, technique/T1546.008]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-558
updated_at: 2026-08-31
summary: "An adversary exploits weaknesses in privilege management or access control to replace a trusted executable with a malicious version and enable the execution of malware when that trusted executable is called."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/558.html
---

# CAPEC-558: Replace Trusted Executable

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | High |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary exploits weaknesses in privilege management or access control to replace a trusted executable with a malicious version and enable the execution of malware when that trusted executable is called.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-284](/wiki/p/weakness/CWE-284)

**ATT&CK techniques:** [T1505.005](/wiki/p/technique/T1505.005), [T1546.008](/wiki/p/technique/T1546.008)

## Source

- [MITRE CAPEC CAPEC-558](https://capec.mitre.org/data/definitions/558.html)
