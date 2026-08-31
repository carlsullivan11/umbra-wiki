---
slug: attack-pattern/CAPEC-198
title: "CAPEC-198 — XSS Targeting Error Pages"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-198]
cwe_ids: [CWE-81]
related: [weakness/CWE-81]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-198
updated_at: 2026-08-31
summary: "An adversary distributes a link (or possibly some other query structure) with a request to a third party web server that is malformed and also contains a block of exploit code in order to have the exploit become live code in the resulting error page."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/198.html
---

# CAPEC-198: XSS Targeting Error Pages

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary distributes a link (or possibly some other query structure) with a request to a third party web server that is malformed and also contains a block of exploit code in order to have the exploit become live code in the resulting error page.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-81](/wiki/p/weakness/CWE-81)

## Prerequisites

- A third party web server which fails to adequately sanitize messages sent in error pages.
- The victim must be made to execute a query crafted by the adversary which results in the infected error report.

## Mitigations

- Design: Use libraries and templates that minimize unfiltered input.
- Implementation: Normalize, filter and use an allowlist for any input that will be used in error messages.
- Implementation: The victim should configure the browser to minimize active content from untrusted sources.

## Source

- [MITRE CAPEC CAPEC-198](https://capec.mitre.org/data/definitions/198.html)
