---
slug: attack-pattern/CAPEC-319
title: "CAPEC-319 — IP (DF) 'Don't Fragment Bit' Echoing Probe"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-319]
cwe_ids: [CWE-200]
related: [weakness/CWE-200]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-319
updated_at: 2026-08-31
summary: "This OS fingerprinting probe tests to determine if the remote host echoes back the IP 'DF' (Don't Fragment) bit in a response packet. An attacker sends a UDP datagram with the DF bit set to a closed port on the remote host to observe whether the 'DF' bit is set in the response pa…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/319.html
---

# CAPEC-319: IP (DF) 'Don't Fragment Bit' Echoing Probe

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Low |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

This OS fingerprinting probe tests to determine if the remote host echoes back the IP 'DF' (Don't Fragment) bit in a response packet. An attacker sends a UDP datagram with the DF bit set to a closed port on the remote host to observe whether the 'DF' bit is set in the response packet. Some operating systems will echo the bit in the ICMP error message while others will zero out the bit in the response packet.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-200](/wiki/p/weakness/CWE-200)

## Consequences

- Confidentiality: Read Data
- Confidentiality, Access Control, Authorization: Bypass Protection Mechanism, Hide Activities

## Source

- [MITRE CAPEC CAPEC-319](https://capec.mitre.org/data/definitions/319.html)
