---
slug: attack-pattern/CAPEC-584
title: "CAPEC-584 — BGP Route Disabling"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-584]
related: []
provenance: imported
import_source: mitre-capec
import_id: CAPEC-584
updated_at: 2026-08-31
summary: "An adversary suppresses the Border Gateway Protocol (BGP) advertisement for a route so as to render the underlying network inaccessible. The BGP protocol helps traffic move throughout the Internet by selecting the most efficient route between Autonomous Systems (AS), or routing d…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/584.html
---

# CAPEC-584: BGP Route Disabling

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | — |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary suppresses the Border Gateway Protocol (BGP) advertisement for a route so as to render the underlying network inaccessible. The BGP protocol helps traffic move throughout the Internet by selecting the most efficient route between Autonomous Systems (AS), or routing domains. BGP is the basis for interdomain routing infrastructure, providing connections between these ASs. By suppressing the intended AS routing advertisements and/or forcing less effective routes for traffic to ASs, the adversary can deny availability for the target network.

## Prerequisites

- The adversary must have control of a router that can modify, drop, or introduce spoofed BGP updates.The adversary can convince

## Consequences

- Availability: Other

## Mitigations

- Implement Ingress filters to check the validity of received routes. However, this relies on the accuracy of Internet Routing Registries (IRRs) databases which are often not well-maintained.
- Implement Secure BGP (S-BGP protocol), which improves authorization and authentication capabilities based on public-key cryptography.

## Source

- [MITRE CAPEC CAPEC-584](https://capec.mitre.org/data/definitions/584.html)
