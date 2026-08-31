---
slug: attack-pattern/CAPEC-332
title: "CAPEC-332 — ICMP IP 'ID' Field Error Message Probe"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-332]
cwe_ids: [CWE-204]
related: [weakness/CWE-204]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-332
updated_at: 2026-08-31
summary: "An adversary sends a UDP datagram having an assigned value to its internet identification field (ID) to a closed port on a target to observe the manner in which this bit is echoed back in the ICMP error message. This allows the attacker to construct a fingerprint of specific OS b…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/332.html
---

# CAPEC-332: ICMP IP 'ID' Field Error Message Probe

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Low |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary sends a UDP datagram having an assigned value to its internet identification field (ID) to a closed port on a target to observe the manner in which this bit is echoed back in the ICMP error message. This allows the attacker to construct a fingerprint of specific OS behaviors.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-204](/wiki/p/weakness/CWE-204)

## Prerequisites

- The ability to monitor and interact with network communications. Access to at least one host, and the privileges to interface with the network interface card.

## Consequences

- Confidentiality: Read Data
- Confidentiality, Access Control, Authorization: Bypass Protection Mechanism, Hide Activities

## Source

- [MITRE CAPEC CAPEC-332](https://capec.mitre.org/data/definitions/332.html)
