---
slug: attack-pattern/CAPEC-309
title: "CAPEC-309 — Network Topology Mapping"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-309]
cwe_ids: [CWE-200]
mitre_ids: [T1016, T1049, T1590]
related: [weakness/CWE-200, technique/T1016, technique/T1049, technique/T1590]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-309
updated_at: 2026-08-31
summary: "An adversary engages in scanning activities to map network nodes, hosts, devices, and routes. Adversaries usually perform this type of network reconnaissance during the early stages of attack against an external network. Many types of scanning utilities are typically employed, in…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/309.html
---

# CAPEC-309: Network Topology Mapping

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Low |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary engages in scanning activities to map network nodes, hosts, devices, and routes. Adversaries usually perform this type of network reconnaissance during the early stages of attack against an external network. Many types of scanning utilities are typically employed, including ICMP tools, network mappers, port scanners, and route testing utilities such as traceroute.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-200](/wiki/p/weakness/CWE-200)

**ATT&CK techniques:** [T1016](/wiki/p/technique/T1016), [T1049](/wiki/p/technique/T1049), [T1590](/wiki/p/technique/T1590)

## Prerequisites

- None

## Consequences

- Confidentiality: Other

## Source

- [MITRE CAPEC CAPEC-309](https://capec.mitre.org/data/definitions/309.html)
