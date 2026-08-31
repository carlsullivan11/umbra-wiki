---
slug: attack-pattern/CAPEC-296
title: "CAPEC-296 — ICMP Information Request"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-296]
cwe_ids: [CWE-200]
related: [weakness/CWE-200]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-296
updated_at: 2026-08-31
summary: "An adversary sends an ICMP Information Request to a host to determine if it will respond to this deprecated mechanism. ICMP Information Requests are a deprecated message type. Information Requests were originally used for diskless machines to automatically obtain their network co…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/296.html
---

# CAPEC-296: ICMP Information Request

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Low |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary sends an ICMP Information Request to a host to determine if it will respond to this deprecated mechanism. ICMP Information Requests are a deprecated message type. Information Requests were originally used for diskless machines to automatically obtain their network configuration, but this message type has been superseded by more robust protocol implementations like DHCP.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-200](/wiki/p/weakness/CWE-200)

## Prerequisites

- The ability to send an ICMP Type 15 Information Request and receive an ICMP Type 16 Information Reply in response.

## Skills required

- Low: The adversary needs to know certain linux commands for this type of attack.

## Consequences

- Confidentiality: Other

## Source

- [MITRE CAPEC CAPEC-296](https://capec.mitre.org/data/definitions/296.html)
