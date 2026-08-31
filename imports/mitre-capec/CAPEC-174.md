---
slug: attack-pattern/CAPEC-174
title: "CAPEC-174 — Flash Parameter Injection"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-174]
cwe_ids: [CWE-88]
related: [weakness/CWE-88]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-174
updated_at: 2026-08-31
summary: "An adversary takes advantage of improper data validation to inject malicious global parameters into a Flash file embedded within an HTML document. Flash files can leverage user-submitted data to configure the Flash document and access the embedding HTML document."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/174.html
---

# CAPEC-174: Flash Parameter Injection

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary takes advantage of improper data validation to inject malicious global parameters into a Flash file embedded within an HTML document. Flash files can leverage user-submitted data to configure the Flash document and access the embedding HTML document.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-88](/wiki/p/weakness/CWE-88)

## Skills required

- Medium: The adversary need inject values into the global parameters to the Flash file and understand the parent HTML document DOM structure. The adversary needs to be smart enough to convince the victim to click on their crafted link.

## Consequences

- Confidentiality: Other
- Authorization: Execute Unauthorized Commands

## Mitigations

- User input must be sanitized according to context before reflected back to the user. The JavaScript function 'encodeURI' is not always sufficient for sanitizing input intended for global Flash parameters. Extreme caution should be taken when saving user input in Flash cookies. In such cases the Flash file itself will need to be fixed and recompiled, changing the name of the local shared objects (Flash cookies).

## Source

- [MITRE CAPEC CAPEC-174](https://capec.mitre.org/data/definitions/174.html)
