---
slug: attack-pattern/CAPEC-245
title: "CAPEC-245 — XSS Using Doubled Characters"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-245]
cwe_ids: [CWE-85]
related: [weakness/CWE-85]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-245
updated_at: 2026-08-31
summary: "The adversary bypasses input validation by using doubled characters in order to perform a cross-site scripting attack. Some filters fail to recognize dangerous sequences if they are preceded by repeated characters. For example, by doubling the < before a script command, (<<script…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/245.html
---

# CAPEC-245: XSS Using Doubled Characters

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

The adversary bypasses input validation by using doubled characters in order to perform a cross-site scripting attack. Some filters fail to recognize dangerous sequences if they are preceded by repeated characters. For example, by doubling the < before a script command, (<<script or %3C%3script using URI encoding) the filters of some web applications may fail to recognize the presence of a script tag. If the targeted server is vulnerable to this type of bypass, the adversary can create a crafted URL or other trap to cause a victim to view a page on the targeted server where the malicious content is executed, as per a normal XSS attack.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-85](/wiki/p/weakness/CWE-85)

## Prerequisites

- The targeted web application does not fully normalize input before checking for prohibited syntax. In particular, it must fail to recognize prohibited methods preceded by certain sequences of repeated characters.

## Mitigations

- Design: Use libraries and templates that minimize unfiltered input.
- Implementation: Normalize, filter and sanitize all user supplied fields.
- Implementation: The victim should configure the browser to minimize active content from untrusted sources.

## Source

- [MITRE CAPEC CAPEC-245](https://capec.mitre.org/data/definitions/245.html)
