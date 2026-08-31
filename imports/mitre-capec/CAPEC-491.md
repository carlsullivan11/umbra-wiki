---
slug: attack-pattern/CAPEC-491
title: "CAPEC-491 — Quadratic Data Expansion"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-491]
cwe_ids: [CWE-770]
related: [weakness/CWE-770]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-491
updated_at: 2026-08-31
summary: "An adversary exploits macro-like substitution to cause a denial of service situation due to excessive memory being allocated to fully expand the data. The result of this denial of service could cause the application to freeze or crash. This involves defining a very large entity a…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/491.html
---

# CAPEC-491: Quadratic Data Expansion

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | — |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary exploits macro-like substitution to cause a denial of service situation due to excessive memory being allocated to fully expand the data. The result of this denial of service could cause the application to freeze or crash. This involves defining a very large entity and using it multiple times in a single entity substitution. CAPEC-197 is a similar attack pattern, but it is easier to discover and defend against. This attack pattern does not perform multi-level substitution and therefore does not obviously appear to consume extensive resources.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-770](/wiki/p/weakness/CWE-770)

## Prerequisites

- This type of attack requires a server that accepts serialization data which supports substitution and parses the data.

## Consequences

- Availability: Unreliable Execution, Resource Consumption

## Mitigations

- Design: Use libraries and templates that minimize unfiltered input. Use methods that limit entity expansion and throw exceptions on attempted entity expansion.
- Implementation: For XML based data - disable altogether the use of inline DTD schemas when parsing XML objects. If a DTD must be used, normalize, filter and use an allowlist and parse with methods and routines that will detect entity expansion from untrusted sources.

## Source

- [MITRE CAPEC CAPEC-491](https://capec.mitre.org/data/definitions/491.html)
