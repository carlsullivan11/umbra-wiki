---
slug: attack-pattern/CAPEC-272
title: "CAPEC-272 — Protocol Manipulation"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-272]
related: []
provenance: imported
import_source: mitre-capec
import_id: CAPEC-272
updated_at: 2026-08-31
summary: "An adversary subverts a communications protocol to perform an attack. This type of attack can allow an adversary to impersonate others, discover sensitive information, control the outcome of a session, or perform other attacks. This type of attack targets invalid assumptions that…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/272.html
---

# CAPEC-272: Protocol Manipulation

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary subverts a communications protocol to perform an attack. This type of attack can allow an adversary to impersonate others, discover sensitive information, control the outcome of a session, or perform other attacks. This type of attack targets invalid assumptions that may be inherent in implementers of the protocol, incorrect implementations of the protocol, or vulnerabilities in the protocol itself.

## Prerequisites

- The protocol or implementations thereof must contain bugs that an adversary can exploit.

## Source

- [MITRE CAPEC CAPEC-272](https://capec.mitre.org/data/definitions/272.html)
