---
slug: attack-pattern/CAPEC-274
title: "CAPEC-274 — HTTP Verb Tampering"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-274]
cwe_ids: [CWE-302, CWE-654]
related: [weakness/CWE-302, weakness/CWE-654]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-274
updated_at: 2026-08-31
summary: "An attacker modifies the HTTP Verb (e.g. GET, PUT, TRACE, etc.) in order to bypass access restrictions. Some web environments allow administrators to restrict access based on the HTTP Verb used with requests. However, attackers can often provide a different HTTP Verb, or even pro…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/274.html
---

# CAPEC-274: HTTP Verb Tampering

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker modifies the HTTP Verb (e.g. GET, PUT, TRACE, etc.) in order to bypass access restrictions. Some web environments allow administrators to restrict access based on the HTTP Verb used with requests. However, attackers can often provide a different HTTP Verb, or even provide a random string as a verb in order to bypass these protections. This allows the attacker to access data that should otherwise be protected.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-302](/wiki/p/weakness/CWE-302), [CWE-654](/wiki/p/weakness/CWE-654)

## Prerequisites

- The targeted system must attempt to filter access based on the HTTP verb used in requests.

## Mitigations

- Design: Ensure that only legitimate HTTP verbs are allowed.
- Design: Do not use HTTP verbs as factors in access decisions.

## Source

- [MITRE CAPEC CAPEC-274](https://capec.mitre.org/data/definitions/274.html)
