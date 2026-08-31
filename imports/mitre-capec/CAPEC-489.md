---
slug: attack-pattern/CAPEC-489
title: "CAPEC-489 — SSL Flood"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-489]
cwe_ids: [CWE-770]
mitre_ids: [T1499.002]
related: [weakness/CWE-770, technique/T1499.002]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-489
updated_at: 2026-08-31
summary: "An adversary may execute a flooding attack using the SSL protocol with the intent to deny legitimate users access to a service by consuming all the available resources on the server side. These attacks take advantage of the asymmetric relationship between the processing power use…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/489.html
---

# CAPEC-489: SSL Flood

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | — |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary may execute a flooding attack using the SSL protocol with the intent to deny legitimate users access to a service by consuming all the available resources on the server side. These attacks take advantage of the asymmetric relationship between the processing power used by the client and the processing power used by the server to create a secure connection. In this manner the attacker can make a large number of HTTPS requests on a low provisioned machine to tie up a disproportionately large number of resources on the server. The clients then continue to keep renegotiating the SSL connection. When multiplied by a large number of attacking machines, this attack can result in a crash or loss of service to legitimate users.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-770](/wiki/p/weakness/CWE-770)

**ATT&CK techniques:** [T1499.002](/wiki/p/technique/T1499.002)

## Prerequisites

- This type of an attack requires the ability to generate a large amount of SSL traffic to send a target server.

## Mitigations

- To mitigate this type of an attack, an organization can create rule based filters to silently drop connections if too many are attempted in a certain time period.

## Source

- [MITRE CAPEC CAPEC-489](https://capec.mitre.org/data/definitions/489.html)
