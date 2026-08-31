---
slug: attack-pattern/CAPEC-115
title: "CAPEC-115 — Authentication Bypass"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-115]
cwe_ids: [CWE-287]
mitre_ids: [T1548]
related: [weakness/CWE-287, technique/T1548]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-115
updated_at: 2026-08-31
summary: "An attacker gains access to application, service, or device with the privileges of an authorized or privileged user by evading or circumventing an authentication mechanism. The attacker is therefore able to access protected data without authentication ever having taken place."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/115.html
---

# CAPEC-115: Authentication Bypass

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker gains access to application, service, or device with the privileges of an authorized or privileged user by evading or circumventing an authentication mechanism. The attacker is therefore able to access protected data without authentication ever having taken place.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-287](/wiki/p/weakness/CWE-287)

**ATT&CK techniques:** [T1548](/wiki/p/technique/T1548)

## Prerequisites

- An authentication mechanism or subsystem implementing some form of authentication such as passwords, digest authentication, security certificates, etc.

## Source

- [MITRE CAPEC CAPEC-115](https://capec.mitre.org/data/definitions/115.html)
