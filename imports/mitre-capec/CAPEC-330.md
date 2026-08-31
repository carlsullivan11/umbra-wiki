---
slug: attack-pattern/CAPEC-330
title: "CAPEC-330 — ICMP Error Message Echoing Integrity Probe"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-330]
cwe_ids: [CWE-200]
related: [weakness/CWE-200]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-330
updated_at: 2026-08-31
summary: "An adversary uses a technique to generate an ICMP Error message (Port Unreachable, Destination Unreachable, Redirect, Source Quench, Time Exceeded, Parameter Problem) from a target and then analyze the integrity of data returned or 'Quoted' from the originating request that gener…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/330.html
---

# CAPEC-330: ICMP Error Message Echoing Integrity Probe

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Low |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary uses a technique to generate an ICMP Error message (Port Unreachable, Destination Unreachable, Redirect, Source Quench, Time Exceeded, Parameter Problem) from a target and then analyze the integrity of data returned or "Quoted" from the originating request that generated the error message.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-200](/wiki/p/weakness/CWE-200)

## Prerequisites

- The ability to monitor and interact with network communications.Access to at least one host, and the privileges to interface with the network interface card.

## Consequences

- Confidentiality: Read Data
- Confidentiality, Access Control, Authorization: Bypass Protection Mechanism, Hide Activities

## Source

- [MITRE CAPEC CAPEC-330](https://capec.mitre.org/data/definitions/330.html)
