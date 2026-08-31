---
slug: attack-pattern/CAPEC-250
title: "CAPEC-250 — XML Injection"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-250]
cwe_ids: [CWE-20, CWE-74, CWE-91, CWE-707]
related: [weakness/CWE-20, weakness/CWE-74, weakness/CWE-91, weakness/CWE-707]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-250
updated_at: 2026-08-31
summary: "An attacker utilizes crafted XML user-controllable input to probe, attack, and inject data into the XML database, using techniques similar to SQL injection. The user-controllable input can allow for unauthorized viewing of data, bypassing authentication or the front-end applicati…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/250.html
---

# CAPEC-250: XML Injection

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | — |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker utilizes crafted XML user-controllable input to probe, attack, and inject data into the XML database, using techniques similar to SQL injection. The user-controllable input can allow for unauthorized viewing of data, bypassing authentication or the front-end application for direct XML database access, and possibly altering database information.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-20](/wiki/p/weakness/CWE-20), [CWE-74](/wiki/p/weakness/CWE-74), [CWE-91](/wiki/p/weakness/CWE-91), [CWE-707](/wiki/p/weakness/CWE-707)

## Prerequisites

- XML queries used to process user input and retrieve information stored in XML documents
- User-controllable input not properly sanitized

## Skills required

- Low: An attacker must have knowledge of XML syntax and constructs in order to successfully leverage XML Injection

## Consequences

- Confidentiality, Access Control, Authorization: Gain Privileges
- Confidentiality: Read Data

## Mitigations

- Strong input validation - All user-controllable input must be validated and filtered for illegal characters as well as content that can be interpreted in the context of an XML data or a query.
- Use of custom error pages - Attackers can glean information about the nature of queries from descriptive error messages. Input validation must be coupled with customized error pages that inform about an error without disclosing information about the database or application.

## Source

- [MITRE CAPEC CAPEC-250](https://capec.mitre.org/data/definitions/250.html)
