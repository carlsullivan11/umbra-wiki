---
slug: attack-pattern/CAPEC-228
title: "CAPEC-228 — DTD Injection"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-228]
cwe_ids: [CWE-829]
related: [weakness/CWE-829]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-228
updated_at: 2026-08-31
summary: "An attacker injects malicious content into an application's DTD in an attempt to produce a negative technical impact. DTDs are used to describe how XML documents are processed. Certain malformed DTDs (for example, those with excessive entity expansion as described in CAPEC 197) c…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/228.html
---

# CAPEC-228: DTD Injection

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker injects malicious content into an application's DTD in an attempt to produce a negative technical impact. DTDs are used to describe how XML documents are processed. Certain malformed DTDs (for example, those with excessive entity expansion as described in CAPEC 197) can cause the XML parsers that process the DTDs to consume excessive resources resulting in resource depletion.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-829](/wiki/p/weakness/CWE-829)

## Prerequisites

- The target must be running an XML based application that leverages DTDs.

## Mitigations

- Design: Sanitize incoming DTDs to prevent excessive expansion or other actions that could result in impacts like resource depletion.
- Implementation: Disallow the inclusion of DTDs as part of incoming messages.
- Implementation: Use XML parsing tools that protect against DTD attacks.

## Source

- [MITRE CAPEC CAPEC-228](https://capec.mitre.org/data/definitions/228.html)
