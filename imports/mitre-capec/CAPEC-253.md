---
slug: attack-pattern/CAPEC-253
title: "CAPEC-253 — Remote Code Inclusion"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-253]
cwe_ids: [CWE-829]
related: [weakness/CWE-829]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-253
updated_at: 2026-08-31
summary: "The attacker forces an application to load arbitrary code files from a remote location. The attacker could use this to try to load old versions of library files that have known vulnerabilities, to load malicious files that the attacker placed on the remote machine, or to otherwis…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/253.html
---

# CAPEC-253: Remote Code Inclusion

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | — |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

The attacker forces an application to load arbitrary code files from a remote location. The attacker could use this to try to load old versions of library files that have known vulnerabilities, to load malicious files that the attacker placed on the remote machine, or to otherwise change the functionality of the targeted application in unexpected ways.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-829](/wiki/p/weakness/CWE-829)

## Prerequisites

- Target application server must allow remote files to be included.The malicious file must be placed on the remote machine previously.

## Mitigations

- Minimize attacks by input validation and sanitization of any user data that will be used by the target application to locate a remote file to be included.

## Source

- [MITRE CAPEC CAPEC-253](https://capec.mitre.org/data/definitions/253.html)
