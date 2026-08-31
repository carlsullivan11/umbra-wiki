---
slug: attack-pattern/CAPEC-598
title: "CAPEC-598 — DNS Spoofing"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-598]
related: []
provenance: imported
import_source: mitre-capec
import_id: CAPEC-598
updated_at: 2026-08-31
summary: "An adversary sends a malicious ('NXDOMAIN' ('No such domain') code, or DNS A record) response to a target's route request before a legitimate resolver can. This technique requires an On-path or In-path device that can monitor and respond to the target's DNS requests. This attack …"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/598.html
---

# CAPEC-598: DNS Spoofing

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | — |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary sends a malicious ("NXDOMAIN" ("No such domain") code, or DNS A record) response to a target's route request before a legitimate resolver can. This technique requires an On-path or In-path device that can monitor and respond to the target's DNS requests. This attack differs from BGP Tampering in that it directly responds to requests made by the target instead of polluting the routing the target's infrastructure uses.

## Prerequisites

- On/In Path Device

## Skills required

- Low: To distribute email

## Mitigations

- Design: Avoid dependence on DNS
- Design: Include "hosts file"/IP address in the application
- Implementation: Utilize a .onion domain with Tor support
- Implementation: DNSSEC
- Implementation: DNS-hold-open

## Source

- [MITRE CAPEC CAPEC-598](https://capec.mitre.org/data/definitions/598.html)
