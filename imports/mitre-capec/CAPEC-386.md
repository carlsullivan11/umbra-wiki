---
slug: attack-pattern/CAPEC-386
title: "CAPEC-386 — Application API Navigation Remapping"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-386]
cwe_ids: [CWE-311, CWE-345, CWE-346, CWE-471, CWE-602]
related: [weakness/CWE-311, weakness/CWE-345, weakness/CWE-346, weakness/CWE-471, weakness/CWE-602]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-386
updated_at: 2026-08-31
summary: "An attacker manipulates either egress or ingress data from a client within an application framework in order to change the destination and/or content of links/buttons displayed to a user within API messages. Performing this attack allows the attacker to manipulate content in such…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/386.html
---

# CAPEC-386: Application API Navigation Remapping

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker manipulates either egress or ingress data from a client within an application framework in order to change the destination and/or content of links/buttons displayed to a user within API messages. Performing this attack allows the attacker to manipulate content in such a way as to produce messages or content that looks authentic but contains links/buttons that point to an attacker controlled destination. Some applications make navigation remapping more difficult to detect because the actual HREF values of images, profile elements, and links/buttons are masked. One example would be to place an image in a user's photo gallery that when clicked upon redirected the user to an off-site location. Also, traditional web vulnerabilities (such as CSRF) can be constructed with remapped buttons or links. In some cases navigation remapping can be used for Phishing attacks or even means to artificially boost the page view, user site reputation, or click-fraud.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-311](/wiki/p/weakness/CWE-311), [CWE-345](/wiki/p/weakness/CWE-345), [CWE-346](/wiki/p/weakness/CWE-346), [CWE-471](/wiki/p/weakness/CWE-471), [CWE-602](/wiki/p/weakness/CWE-602)

## Prerequisites

- Targeted software is utilizing application framework APIs

## Source

- [MITRE CAPEC CAPEC-386](https://capec.mitre.org/data/definitions/386.html)
