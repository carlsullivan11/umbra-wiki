---
slug: attack-pattern/CAPEC-179
title: "CAPEC-179 — Calling Micro-Services Directly"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-179]
related: []
provenance: imported
import_source: mitre-capec
import_id: CAPEC-179
updated_at: 2026-08-31
summary: "An attacker is able to discover and query Micro-services at a web location and thereby expose the Micro-services to further exploitation by gathering information about their implementation and function. Micro-services in web pages allow portions of a page to connect to the server…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/179.html
---

# CAPEC-179: Calling Micro-Services Directly

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker is able to discover and query Micro-services at a web location and thereby expose the Micro-services to further exploitation by gathering information about their implementation and function. Micro-services in web pages allow portions of a page to connect to the server and update content without needing to cause the entire page to update. This allows user activity to change portions of the page more quickly without causing disruptions elsewhere.

## Prerequisites

- The target site must use micro-services that interact with the server and one or more of these micro-services must be vulnerable to some other attack pattern.

## Source

- [MITRE CAPEC CAPEC-179](https://capec.mitre.org/data/definitions/179.html)
