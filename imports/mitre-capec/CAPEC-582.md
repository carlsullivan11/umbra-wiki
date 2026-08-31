---
slug: attack-pattern/CAPEC-582
title: "CAPEC-582 — Route Disabling"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-582]
related: []
provenance: imported
import_source: mitre-capec
import_id: CAPEC-582
updated_at: 2026-08-31
summary: "An adversary disables the network route between two targets. The goal is to completely sever the communications channel between two entities. This is often the result of a major error or the use of an 'Internet kill switch' by those in control of critical infrastructure. This att…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/582.html
---

# CAPEC-582: Route Disabling

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary disables the network route between two targets. The goal is to completely sever the communications channel between two entities. This is often the result of a major error or the use of an "Internet kill switch" by those in control of critical infrastructure. This attack pattern differs from most other obstruction patterns by targeting the route itself, as opposed to the data passed over the route.

## Prerequisites

- The adversary requires knowledge of and access to network route.

## Consequences

- Availability: Other

## Source

- [MITRE CAPEC CAPEC-582](https://capec.mitre.org/data/definitions/582.html)
