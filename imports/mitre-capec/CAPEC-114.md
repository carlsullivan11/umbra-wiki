---
slug: attack-pattern/CAPEC-114
title: "CAPEC-114 — Authentication Abuse"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-114]
cwe_ids: [CWE-287, CWE-1244]
mitre_ids: [T1548]
related: [weakness/CWE-287, weakness/CWE-1244, technique/T1548]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-114
updated_at: 2026-08-31
summary: "An attacker obtains unauthorized access to an application, service or device either through knowledge of the inherent weaknesses of an authentication mechanism, or by exploiting a flaw in the authentication scheme's implementation. In such an attack an authentication mechanism is…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/114.html
---

# CAPEC-114: Authentication Abuse

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker obtains unauthorized access to an application, service or device either through knowledge of the inherent weaknesses of an authentication mechanism, or by exploiting a flaw in the authentication scheme's implementation. In such an attack an authentication mechanism is functioning but a carefully controlled sequence of events causes the mechanism to grant access to the attacker.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-287](/wiki/p/weakness/CWE-287), [CWE-1244](/wiki/p/weakness/CWE-1244)

**ATT&CK techniques:** [T1548](/wiki/p/technique/T1548)

## Prerequisites

- An authentication mechanism or subsystem implementing some form of authentication such as passwords, digest authentication, security certificates, etc. which is flawed in some way.

## Source

- [MITRE CAPEC CAPEC-114](https://capec.mitre.org/data/definitions/114.html)
