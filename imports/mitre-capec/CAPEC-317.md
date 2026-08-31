---
slug: attack-pattern/CAPEC-317
title: "CAPEC-317 — IP ID Sequencing Probe"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-317]
cwe_ids: [CWE-200]
related: [weakness/CWE-200]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-317
updated_at: 2026-08-31
summary: "This OS fingerprinting probe analyzes the IP 'ID' field sequence number generation algorithm of a remote host. Operating systems generate IP 'ID' numbers differently, allowing an attacker to identify the operating system of the host by examining how is assigns ID numbers when gen…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/317.html
---

# CAPEC-317: IP ID Sequencing Probe

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Low |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

This OS fingerprinting probe analyzes the IP 'ID' field sequence number generation algorithm of a remote host. Operating systems generate IP 'ID' numbers differently, allowing an attacker to identify the operating system of the host by examining how is assigns ID numbers when generating response packets. RFC 791 does not specify how ID numbers are chosen or their ranges, so ID sequence generation differs from implementation to implementation. There are two kinds of IP 'ID' sequence number analysis - IP 'ID' Sequencing: analyzing the IP 'ID' sequence generation algorithm for one protocol used by a host and Shared IP 'ID' Sequencing: analyzing the packet ordering via IP 'ID' values spanning multiple protocols, such as between ICMP and TCP.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-200](/wiki/p/weakness/CWE-200)

## Consequences

- Confidentiality: Read Data
- Confidentiality, Access Control, Authorization: Bypass Protection Mechanism, Hide Activities

## Source

- [MITRE CAPEC CAPEC-317](https://capec.mitre.org/data/definitions/317.html)
