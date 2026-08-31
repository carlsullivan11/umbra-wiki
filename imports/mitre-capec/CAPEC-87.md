---
slug: attack-pattern/CAPEC-87
title: "CAPEC-87 — Forceful Browsing"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-87]
cwe_ids: [CWE-285, CWE-425, CWE-693]
related: [weakness/CWE-285, weakness/CWE-425, weakness/CWE-693]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-87
updated_at: 2026-08-31
summary: "An attacker employs forceful browsing (direct URL entry) to access portions of a website that are otherwise unreachable. Usually, a front controller or similar design pattern is employed to protect access to portions of a web application. Forceful browsing enables an attacker to …"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/87.html
---

# CAPEC-87: Forceful Browsing

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker employs forceful browsing (direct URL entry) to access portions of a website that are otherwise unreachable. Usually, a front controller or similar design pattern is employed to protect access to portions of a web application. Forceful browsing enables an attacker to access information, perform privileged operations and otherwise reach sections of the web application that have been improperly protected.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-285](/wiki/p/weakness/CWE-285), [CWE-425](/wiki/p/weakness/CWE-425), [CWE-693](/wiki/p/weakness/CWE-693)

## Prerequisites

- The forcibly browseable pages or accessible resources must be discoverable and improperly protected.

## Skills required

- Low: Forcibly browseable pages can be discovered by using a number of automated tools. Doing the same manually is tedious but by no means difficult.

## Consequences

- Confidentiality: Read Data
- Confidentiality, Access Control, Authorization: Bypass Protection Mechanism

## Mitigations

- Authenticate request to every resource. In addition, every page or resource must ensure that the request it is handling has been made in an authorized context.
- Forceful browsing can also be made difficult to a large extent by not hard-coding names of application pages or resources. This way, the attacker cannot figure out, from the application alone, the resources available from the present context.

## Source

- [MITRE CAPEC CAPEC-87](https://capec.mitre.org/data/definitions/87.html)
