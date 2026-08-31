---
slug: attack-pattern/CAPEC-495
title: "CAPEC-495 — UDP Fragmentation"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-495]
cwe_ids: [CWE-404, CWE-770]
related: [weakness/CWE-404, weakness/CWE-770]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-495
updated_at: 2026-08-31
summary: "An attacker may execute a UDP Fragmentation attack against a target server in an attempt to consume resources such as bandwidth and CPU. IP fragmentation occurs when an IP datagram is larger than the MTU of the route the datagram has to traverse. Typically the attacker will use l…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/495.html
---

# CAPEC-495: UDP Fragmentation

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | — |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker may execute a UDP Fragmentation attack against a target server in an attempt to consume resources such as bandwidth and CPU. IP fragmentation occurs when an IP datagram is larger than the MTU of the route the datagram has to traverse. Typically the attacker will use large UDP packets over 1500 bytes of data which forces fragmentation as ethernet MTU is 1500 bytes. This attack is a variation on a typical UDP flood but it enables more network bandwidth to be consumed with fewer packets. Additionally it has the potential to consume server CPU resources and fill memory buffers associated with the processing and reassembling of fragmented packets.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-404](/wiki/p/weakness/CWE-404), [CWE-770](/wiki/p/weakness/CWE-770)

## Prerequisites

- This type of an attack requires the attacker to be able to generate fragmented IP traffic containing crafted data.

## Mitigations

- This attack may be mitigated by changing default cache sizes to be larger at the OS level. Additionally rules can be enforced to prune the cache with shorter timeouts for packet reassembly as the cache nears capacity.

## Source

- [MITRE CAPEC CAPEC-495](https://capec.mitre.org/data/definitions/495.html)
