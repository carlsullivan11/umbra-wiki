---
slug: attack-pattern/CAPEC-294
title: "CAPEC-294 — ICMP Address Mask Request"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-294]
cwe_ids: [CWE-200]
related: [weakness/CWE-200]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-294
updated_at: 2026-08-31
summary: "An adversary sends an ICMP Type 17 Address Mask Request to gather information about a target's networking configuration. ICMP Address Mask Requests are defined by RFC-950, 'Internet Standard Subnetting Procedure.' An Address Mask Request is an ICMP type 17 message that triggers a…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/294.html
---

# CAPEC-294: ICMP Address Mask Request

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Low |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary sends an ICMP Type 17 Address Mask Request to gather information about a target's networking configuration. ICMP Address Mask Requests are defined by RFC-950, "Internet Standard Subnetting Procedure." An Address Mask Request is an ICMP type 17 message that triggers a remote system to respond with a list of its related subnets, as well as its default gateway and broadcast address via an ICMP type 18 Address Mask Reply datagram. Gathering this type of information helps the adversary plan router-based attacks as well as denial-of-service attacks against the broadcast address.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-200](/wiki/p/weakness/CWE-200)

## Prerequisites

- The ability to send an ICMP type 17 query (Address Mask Request) to a remote target and receive an ICMP type 18 message (ICMP Address Mask Reply) in response. Generally, modern operating systems will ignore ICMP type 17 messages, however, routers will commonly respond to this request.

## Consequences

- Confidentiality: Other
- Confidentiality, Access Control, Authorization: Hide Activities

## Source

- [MITRE CAPEC CAPEC-294](https://capec.mitre.org/data/definitions/294.html)
