---
slug: attack-pattern/CAPEC-596
title: "CAPEC-596 — TCP RST Injection"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-596]
cwe_ids: [CWE-940]
related: [weakness/CWE-940]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-596
updated_at: 2026-08-31
summary: "An adversary injects one or more TCP RST packets to a target after the target has made a HTTP GET request. The goal of this attack is to have the target and/or destination web server terminate the TCP connection."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/596.html
---

# CAPEC-596: TCP RST Injection

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | — |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary injects one or more TCP RST packets to a target after the target has made a HTTP GET request. The goal of this attack is to have the target and/or destination web server terminate the TCP connection.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-940](/wiki/p/weakness/CWE-940)

## Prerequisites

- An On/In Path Device

## Source

- [MITRE CAPEC CAPEC-596](https://capec.mitre.org/data/definitions/596.html)
