---
slug: attack-pattern/CAPEC-482
title: "CAPEC-482 — TCP Flood"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-482]
cwe_ids: [CWE-770]
mitre_ids: [T1498.001, T1499.001, T1499.002]
related: [weakness/CWE-770, technique/T1498.001, technique/T1499.001, technique/T1499.002]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-482
updated_at: 2026-08-31
summary: "An adversary may execute a flooding attack using the TCP protocol with the intent to deny legitimate users access to a service. These attacks exploit the weakness within the TCP protocol where there is some state information for the connection the server needs to maintain. This o…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/482.html
---

# CAPEC-482: TCP Flood

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | — |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary may execute a flooding attack using the TCP protocol with the intent to deny legitimate users access to a service. These attacks exploit the weakness within the TCP protocol where there is some state information for the connection the server needs to maintain. This often involves the use of TCP SYN messages.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-770](/wiki/p/weakness/CWE-770)

**ATT&CK techniques:** [T1498.001](/wiki/p/technique/T1498.001), [T1499.001](/wiki/p/technique/T1499.001), [T1499.002](/wiki/p/technique/T1499.002)

## Prerequisites

- This type of an attack requires the ability to generate a large amount of TCP traffic to send to the target port of a functioning server.

## Mitigations

- To mitigate this type of an attack, an organization can monitor incoming packets and look for patterns in the TCP traffic to determine if the network is under an attack. The potential target may implement a rate limit on TCP SYN messages which would provide limited capabilities while under attack.

## Source

- [MITRE CAPEC CAPEC-482](https://capec.mitre.org/data/definitions/482.html)
