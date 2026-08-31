---
slug: attack-pattern/CAPEC-389
title: "CAPEC-389 — Content Spoofing Via Application API Manipulation"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-389]
cwe_ids: [CWE-353]
related: [weakness/CWE-353]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-389
updated_at: 2026-08-31
summary: "An attacker manipulates either egress or ingress data from a client within an application framework in order to change the content of messages. Performing this attack allows the attacker to manipulate content in such a way as to produce messages or content that look authentic but…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/389.html
---

# CAPEC-389: Content Spoofing Via Application API Manipulation

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Low |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker manipulates either egress or ingress data from a client within an application framework in order to change the content of messages. Performing this attack allows the attacker to manipulate content in such a way as to produce messages or content that look authentic but may contain deceptive links, spam-like content, or links to the attackers' code. In general, content-spoofing within an application API can be employed to stage many different types of attacks varied based on the attackers' intent. The techniques require use of specialized software that allow the attacker to use adversary-in-the-middle (CAPEC-94) communications between the web browser and the remote system.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-353](/wiki/p/weakness/CWE-353)

## Prerequisites

- Targeted software is utilizing application framework APIs

## Source

- [MITRE CAPEC CAPEC-389](https://capec.mitre.org/data/definitions/389.html)
