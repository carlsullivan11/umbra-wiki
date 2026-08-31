---
slug: attack-pattern/CAPEC-247
title: "CAPEC-247 — XSS Using Invalid Characters"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-247]
cwe_ids: [CWE-86]
related: [weakness/CWE-86]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-247
updated_at: 2026-08-31
summary: "An adversary inserts invalid characters in identifiers to bypass application filtering of input. Filters may not scan beyond invalid characters but during later stages of processing content that follows these invalid characters may still be processed. This allows the adversary to…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/247.html
---

# CAPEC-247: XSS Using Invalid Characters

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary inserts invalid characters in identifiers to bypass application filtering of input. Filters may not scan beyond invalid characters but during later stages of processing content that follows these invalid characters may still be processed. This allows the adversary to sneak prohibited commands past filters and perform normally prohibited operations. Invalid characters may include null, carriage return, line feed or tab in an identifier. Successful bypassing of the filter can result in a XSS attack, resulting in the disclosure of web cookies or possibly other results.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-86](/wiki/p/weakness/CWE-86)

## Prerequisites

- The target must fail to remove invalid characters from input and fail to adequately scan beyond these characters.

## Mitigations

- Design: Use libraries and templates that minimize unfiltered input.
- Implementation: Normalize, filter and use an allowlist for any input that will be included in any subsequent web pages or back end operations.
- Implementation: The victim should configure the browser to minimize active content from untrusted sources.

## Source

- [MITRE CAPEC CAPEC-247](https://capec.mitre.org/data/definitions/247.html)
