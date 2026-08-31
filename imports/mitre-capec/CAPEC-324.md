---
slug: attack-pattern/CAPEC-324
title: "CAPEC-324 — TCP (ISN) Sequence Predictability Probe"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-324]
cwe_ids: [CWE-200]
related: [weakness/CWE-200]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-324
updated_at: 2026-08-31
summary: "This type of operating system probe attempts to determine an estimate for how predictable the sequence number generation algorithm is for a remote host. Statistical techniques, such as standard deviation, can be used to determine how predictable the sequence number generation is …"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/324.html
---

# CAPEC-324: TCP (ISN) Sequence Predictability Probe

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Low |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

This type of operating system probe attempts to determine an estimate for how predictable the sequence number generation algorithm is for a remote host. Statistical techniques, such as standard deviation, can be used to determine how predictable the sequence number generation is for a system. This result can then be compared to a database of operating system behaviors to determine a likely match for operating system and version.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-200](/wiki/p/weakness/CWE-200)

## Prerequisites

- The ability to monitor and interact with network communications.Access to at least one host, and the privileges to interface with the network interface card.

## Consequences

- Confidentiality: Read Data
- Confidentiality, Access Control, Authorization: Bypass Protection Mechanism, Hide Activities

## Source

- [MITRE CAPEC CAPEC-324](https://capec.mitre.org/data/definitions/324.html)
