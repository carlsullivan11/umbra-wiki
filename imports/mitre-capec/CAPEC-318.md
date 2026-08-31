---
slug: attack-pattern/CAPEC-318
title: "CAPEC-318 — IP 'ID' Echoed Byte-Order Probe"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-318]
cwe_ids: [CWE-200]
related: [weakness/CWE-200]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-318
updated_at: 2026-08-31
summary: "This OS fingerprinting probe tests to determine if the remote host echoes back the IP 'ID' value from the probe packet. An attacker sends a UDP datagram with an arbitrary IP 'ID' value to a closed port on the remote host to observe the manner in which this bit is echoed back in t…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/318.html
---

# CAPEC-318: IP 'ID' Echoed Byte-Order Probe

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Low |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

This OS fingerprinting probe tests to determine if the remote host echoes back the IP 'ID' value from the probe packet. An attacker sends a UDP datagram with an arbitrary IP 'ID' value to a closed port on the remote host to observe the manner in which this bit is echoed back in the ICMP error message. The identification field (ID) is typically utilized for reassembling a fragmented packet. Some operating systems or router firmware reverse the bit order of the ID field when echoing the IP Header portion of the original datagram within an ICMP error message.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-200](/wiki/p/weakness/CWE-200)

## Consequences

- Confidentiality: Read Data
- Confidentiality, Access Control, Authorization: Bypass Protection Mechanism, Hide Activities

## Source

- [MITRE CAPEC CAPEC-318](https://capec.mitre.org/data/definitions/318.html)
