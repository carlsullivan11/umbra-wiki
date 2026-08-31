---
slug: attack-pattern/CAPEC-460
title: "CAPEC-460 — HTTP Parameter Pollution (HPP)"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-460]
cwe_ids: [CWE-88, CWE-147, CWE-235]
related: [weakness/CWE-88, weakness/CWE-147, weakness/CWE-235]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-460
updated_at: 2026-08-31
summary: "An adversary adds duplicate HTTP GET/POST parameters by injecting query string delimiters. Via HPP it may be possible to override existing hardcoded HTTP parameters, modify the application behaviors, access and, potentially exploit, uncontrollable variables, and bypass input vali…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/460.html
---

# CAPEC-460: HTTP Parameter Pollution (HPP)

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary adds duplicate HTTP GET/POST parameters by injecting query string delimiters. Via HPP it may be possible to override existing hardcoded HTTP parameters, modify the application behaviors, access and, potentially exploit, uncontrollable variables, and bypass input validation checkpoints and WAF rules.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-88](/wiki/p/weakness/CWE-88), [CWE-147](/wiki/p/weakness/CWE-147), [CWE-235](/wiki/p/weakness/CWE-235)

## Prerequisites

- HTTP protocol is used with some GET/POST parameters passed

## Mitigations

- Configuration: If using a Web Application Firewall (WAF), filters should be carefully configured to detect abnormal HTTP requests
- Design: Perform URL encoding
- Implementation: Use strict regular expressions in URL rewriting
- Implementation: Beware of multiple occurrences of a parameter in a Query String

## Source

- [MITRE CAPEC CAPEC-460](https://capec.mitre.org/data/definitions/460.html)
