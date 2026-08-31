---
slug: attack-pattern/CAPEC-293
title: "CAPEC-293 — Traceroute Route Enumeration"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-293]
cwe_ids: [CWE-200]
related: [weakness/CWE-200]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-293
updated_at: 2026-08-31
summary: "An adversary uses a traceroute utility to map out the route which data flows through the network in route to a target destination. Tracerouting can allow the adversary to construct a working topology of systems and routers by listing the systems through which data passes through …"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/293.html
---

# CAPEC-293: Traceroute Route Enumeration

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Low |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary uses a traceroute utility to map out the route which data flows through the network in route to a target destination. Tracerouting can allow the adversary to construct a working topology of systems and routers by listing the systems through which data passes through on their way to the targeted machine. This attack can return varied results depending upon the type of traceroute that is performed. Traceroute works by sending packets to a target while incrementing the Time-to-Live field in the packet header. As the packet traverses each hop along its way to the destination, its TTL expires generating an ICMP diagnostic message that identifies where the packet expired. Traditional techniques for tracerouting involved the use of ICMP and UDP, but as more firewalls began to filter ingress ICMP, methods of traceroute using TCP were developed.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-200](/wiki/p/weakness/CWE-200)

## Prerequisites

- A network capable of routing the attackers' packets to the destination network.

## Consequences

- Confidentiality: Other

## Source

- [MITRE CAPEC CAPEC-293](https://capec.mitre.org/data/definitions/293.html)
