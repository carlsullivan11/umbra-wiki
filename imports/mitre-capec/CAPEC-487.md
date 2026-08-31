---
slug: attack-pattern/CAPEC-487
title: "CAPEC-487 — ICMP Flood"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-487]
cwe_ids: [CWE-770]
related: [weakness/CWE-770]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-487
updated_at: 2026-08-31
summary: "An adversary may execute a flooding attack using the ICMP protocol with the intent to deny legitimate users access to a service by consuming the available network bandwidth. A typical attack involves a victim server receiving ICMP packets at a high rate from a wide range of sourc…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/487.html
---

# CAPEC-487: ICMP Flood

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | — |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary may execute a flooding attack using the ICMP protocol with the intent to deny legitimate users access to a service by consuming the available network bandwidth. A typical attack involves a victim server receiving ICMP packets at a high rate from a wide range of source addresses. Additionally, due to the session-less nature of the ICMP protocol, the source of a packet is easily spoofed making it difficult to find the source of the attack.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-770](/wiki/p/weakness/CWE-770)

## Prerequisites

- This type of an attack requires the ability to generate a large amount of ICMP traffic to send to the target server.

## Mitigations

- To mitigate this type of an attack, an organization can enable ingress filtering. Additionally modifications to BGP like black hole routing and sinkhole routing(RFC3882) help mitigate the spoofed source IP nature of these attacks.

## Source

- [MITRE CAPEC CAPEC-487](https://capec.mitre.org/data/definitions/487.html)
