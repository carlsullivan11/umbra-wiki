---
slug: attack-pattern/CAPEC-590
title: "CAPEC-590 — IP Address Blocking"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-590]
cwe_ids: [CWE-300]
related: [weakness/CWE-300]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-590
updated_at: 2026-08-31
summary: "An adversary performing this type of attack drops packets destined for a target IP address. The aim is to prevent access to the service hosted at the target IP address."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/590.html
---

# CAPEC-590: IP Address Blocking

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary performing this type of attack drops packets destined for a target IP address. The aim is to prevent access to the service hosted at the target IP address.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-300](/wiki/p/weakness/CWE-300)

## Prerequisites

- This attack requires the ability to conduct deep packet inspection with an In-Path device that can drop the targeted traffic and/or connection.

## Consequences

- Availability: Other

## Mitigations

- Have a large pool of backup IPs built into the application and support proxy capability in the application.

## Source

- [MITRE CAPEC CAPEC-590](https://capec.mitre.org/data/definitions/590.html)
