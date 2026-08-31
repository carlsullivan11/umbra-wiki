---
slug: attack-pattern/CAPEC-197
title: "CAPEC-197 — Exponential Data Expansion"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-197]
cwe_ids: [CWE-770, CWE-776]
related: [weakness/CWE-770, weakness/CWE-776]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-197
updated_at: 2026-08-31
summary: "An adversary submits data to a target application which contains nested exponential data expansion to produce excessively large output. Many data format languages allow the definition of macro-like structures that can be used to simplify the creation of complex structures. Howeve…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/197.html
---

# CAPEC-197: Exponential Data Expansion

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary submits data to a target application which contains nested exponential data expansion to produce excessively large output. Many data format languages allow the definition of macro-like structures that can be used to simplify the creation of complex structures. However, this capability can be abused to create excessive demands on a processor's CPU and memory. A small number of nested expansions can result in an exponential growth in demands on memory.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-770](/wiki/p/weakness/CWE-770), [CWE-776](/wiki/p/weakness/CWE-776)

## Prerequisites

- This type of attack requires that the target must receive input but either fail to provide an upper limit for entity expansion or provide a limit that is so large that it does not preclude significant resource consumption.

## Skills required

- Low: Ability to craft nested data expansion messages.

## Consequences

- Availability: Unreliable Execution, Resource Consumption

## Mitigations

- Design: Use libraries and templates that minimize unfiltered input. Use methods that limit entity expansion and throw exceptions on attempted entity expansion.
- Implementation: For XML based data - disable altogether the use of inline DTD schemas when parsing XML objects. If a DTD must be used, normalize, filter and use an allowlist and parse with methods and routines that will detect entity expansion from untrusted sources.

## Source

- [MITRE CAPEC CAPEC-197](https://capec.mitre.org/data/definitions/197.html)
