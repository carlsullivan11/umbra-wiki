---
slug: attack-pattern/CAPEC-234
title: "CAPEC-234 — Hijacking a privileged process"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-234]
cwe_ids: [CWE-648, CWE-732]
related: [weakness/CWE-648, weakness/CWE-732]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-234
updated_at: 2026-08-31
summary: "An adversary gains control of a process that is assigned elevated privileges in order to execute arbitrary code with those privileges. Some processes are assigned elevated privileges on an operating system, usually through association with a particular user, group, or role. If an…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/234.html
---

# CAPEC-234: Hijacking a privileged process

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary gains control of a process that is assigned elevated privileges in order to execute arbitrary code with those privileges. Some processes are assigned elevated privileges on an operating system, usually through association with a particular user, group, or role. If an attacker can hijack this process, they will be able to assume its level of privilege in order to execute their own code.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-648](/wiki/p/weakness/CWE-648), [CWE-732](/wiki/p/weakness/CWE-732)

## Prerequisites

- The targeted process or operating system must contain a bug that allows attackers to hijack the targeted process.

## Source

- [MITRE CAPEC CAPEC-234](https://capec.mitre.org/data/definitions/234.html)
