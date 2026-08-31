---
slug: attack-pattern/CAPEC-612
title: "CAPEC-612 — WiFi MAC Address Tracking"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-612]
cwe_ids: [CWE-201, CWE-300]
related: [weakness/CWE-201, weakness/CWE-300]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-612
updated_at: 2026-08-31
summary: "In this attack scenario, the attacker passively listens for WiFi messages and logs the associated Media Access Control (MAC) addresses. These addresses are intended to be unique to each wireless device (although they can be configured and changed by software). Once the attacker i…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/612.html
---

# CAPEC-612: WiFi MAC Address Tracking

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Low |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

In this attack scenario, the attacker passively listens for WiFi messages and logs the associated Media Access Control (MAC) addresses. These addresses are intended to be unique to each wireless device (although they can be configured and changed by software). Once the attacker is able to associate a MAC address with a particular user or set of users (for example, when attending a public event), the attacker can then scan for that MAC address to track that user in the future.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-201](/wiki/p/weakness/CWE-201), [CWE-300](/wiki/p/weakness/CWE-300)

## Prerequisites

- None

## Skills required

- Low: Open source and commercial software tools are available and several commercial advertising companies routinely set up tools to collect and monitor MAC addresses.

## Mitigations

- Automatic randomization of WiFi MAC addresses
- Frequent changing of handset and retransmission device

## Source

- [MITRE CAPEC CAPEC-612](https://capec.mitre.org/data/definitions/612.html)
