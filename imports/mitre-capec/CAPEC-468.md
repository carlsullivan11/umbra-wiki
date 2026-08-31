---
slug: attack-pattern/CAPEC-468
title: "CAPEC-468 — Generic Cross-Browser Cross-Domain Theft"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-468]
cwe_ids: [CWE-149, CWE-177, CWE-707, CWE-838]
related: [weakness/CWE-149, weakness/CWE-177, weakness/CWE-707, weakness/CWE-838]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-468
updated_at: 2026-08-31
summary: "An attacker makes use of Cascading Style Sheets (CSS) injection to steal data cross domain from the victim's browser. The attack works by abusing the standards relating to loading of CSS: 1. Send cookies on any load of CSS (including cross-domain) 2. When parsing returned CSS ign…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/468.html
---

# CAPEC-468: Generic Cross-Browser Cross-Domain Theft

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker makes use of Cascading Style Sheets (CSS) injection to steal data cross domain from the victim's browser. The attack works by abusing the standards relating to loading of CSS: 1. Send cookies on any load of CSS (including cross-domain) 2. When parsing returned CSS ignore all data that does not make sense before a valid CSS descriptor is found by the CSS parser.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-149](/wiki/p/weakness/CWE-149), [CWE-177](/wiki/p/weakness/CWE-177), [CWE-707](/wiki/p/weakness/CWE-707), [CWE-838](/wiki/p/weakness/CWE-838)

## Prerequisites

- No new lines can be present in the injected CSS stringProper HTML or URL escaping of the " and ' characters is not presentThe attacker has control of two injection points: pre-string and post-string

## Skills required

- High: Ability to craft a CSS injection

## Mitigations

- Design: Prior to performing CSS parsing, require the CSS to start with well-formed CSS when it is a cross-domain load and the MIME type is broken. This is a browser level fix.
- Implementation: Perform proper HTML encoding and URL escaping

## Source

- [MITRE CAPEC CAPEC-468](https://capec.mitre.org/data/definitions/468.html)
