---
slug: attack-pattern/CAPEC-581
title: "CAPEC-581 — Security Software Footprinting"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-581]
mitre_ids: [T1518.001]
related: [technique/T1518.001]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-581
updated_at: 2026-08-31
summary: "Adversaries may attempt to get a listing of security tools that are installed on the system and their configurations. This may include security related system features (such as a built-in firewall or anti-spyware) as well as third-party security software."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/581.html
---

# CAPEC-581: Security Software Footprinting

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | — |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

Adversaries may attempt to get a listing of security tools that are installed on the system and their configurations. This may include security related system features (such as a built-in firewall or anti-spyware) as well as third-party security software.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**ATT&CK techniques:** [T1518.001](/wiki/p/technique/T1518.001)

## Mitigations

- Identify programs that may be used to acquire security tool information and block them by using a software restriction policy or tools that restrict program execution by using a process allowlist.

## Source

- [MITRE CAPEC CAPEC-581](https://capec.mitre.org/data/definitions/581.html)
