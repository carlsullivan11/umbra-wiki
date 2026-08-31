---
slug: attack-pattern/CAPEC-331
title: "CAPEC-331 — ICMP IP Total Length Field Probe"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-331]
cwe_ids: [CWE-204]
related: [weakness/CWE-204]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-331
updated_at: 2026-08-31
summary: "An adversary sends a UDP packet to a closed port on the target machine to solicit an IP Header's total length field value within the echoed 'Port Unreachable' error message. This type of behavior is useful for building a signature-base of operating system responses, particularly …"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/331.html
---

# CAPEC-331: ICMP IP Total Length Field Probe

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Low |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary sends a UDP packet to a closed port on the target machine to solicit an IP Header's total length field value within the echoed 'Port Unreachable" error message. This type of behavior is useful for building a signature-base of operating system responses, particularly when error messages contain other types of information that is useful identifying specific operating system responses.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-204](/wiki/p/weakness/CWE-204)

## Prerequisites

- The ability to monitor and interact with network communications. Access to at least one host, and the privileges to interface with the network interface card.

## Consequences

- Confidentiality: Read Data
- Confidentiality, Access Control, Authorization: Bypass Protection Mechanism, Hide Activities

## Source

- [MITRE CAPEC CAPEC-331](https://capec.mitre.org/data/definitions/331.html)
