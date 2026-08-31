---
slug: attack-pattern/CAPEC-589
title: "CAPEC-589 — DNS Blocking"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-589]
cwe_ids: [CWE-300]
related: [weakness/CWE-300]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-589
updated_at: 2026-08-31
summary: "An adversary intercepts traffic and intentionally drops DNS requests based on content in the request. In this way, the adversary can deny the availability of specific services or content to the user even if the IP address is changed."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/589.html
---

# CAPEC-589: DNS Blocking

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | — |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary intercepts traffic and intentionally drops DNS requests based on content in the request. In this way, the adversary can deny the availability of specific services or content to the user even if the IP address is changed.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-300](/wiki/p/weakness/CWE-300)

## Prerequisites

- This attack requires the ability to conduct deep packet inspection with an In-Path device that can drop the targeted traffic and/or connection.

## Consequences

- Availability: Other

## Mitigations

- Hard Coded Alternate DNS server in applications
- Avoid dependence on DNS
- Include "hosts file"/IP address in the application.
- Ensure best practices with respect to communications channel protections.
- Use a .onion domain with Tor support

## Source

- [MITRE CAPEC CAPEC-589](https://capec.mitre.org/data/definitions/589.html)
