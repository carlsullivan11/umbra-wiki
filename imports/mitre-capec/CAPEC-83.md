---
slug: attack-pattern/CAPEC-83
title: "CAPEC-83 — XPath Injection"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-83]
cwe_ids: [CWE-20, CWE-74, CWE-91, CWE-707]
related: [weakness/CWE-20, weakness/CWE-74, weakness/CWE-91, weakness/CWE-707]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-83
updated_at: 2026-08-31
summary: "An attacker can craft special user-controllable input consisting of XPath expressions to inject the XML database and bypass authentication or glean information that they normally would not be able to. XPath Injection enables an attacker to talk directly to the XML database, thus …"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/83.html
---

# CAPEC-83: XPath Injection

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker can craft special user-controllable input consisting of XPath expressions to inject the XML database and bypass authentication or glean information that they normally would not be able to. XPath Injection enables an attacker to talk directly to the XML database, thus bypassing the application completely. XPath Injection results from the failure of an application to properly sanitize input used as part of dynamic XPath expressions used to query an XML database.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-20](/wiki/p/weakness/CWE-20), [CWE-74](/wiki/p/weakness/CWE-74), [CWE-91](/wiki/p/weakness/CWE-91), [CWE-707](/wiki/p/weakness/CWE-707)

## Prerequisites

- XPath queries used to retrieve information stored in XML documents
- User-controllable input not properly sanitized before being used as part of XPath queries

## Skills required

- Low: XPath Injection shares the same basic premises with SQL Injection. An attacker must have knowledge of XPath syntax and constructs in order to successfully leverage XPath Injection

## Consequences

- Confidentiality, Access Control, Authorization: Gain Privileges
- Confidentiality: Read Data

## Mitigations

- Strong input validation - All user-controllable input must be validated and filtered for illegal characters as well as content that can be interpreted in the context of an XPath expression. Characters such as a single-quote(') or operators such as or (|), and (&) and such should be filtered if the application does not expect them in the context in which they appear. If such content cannot be filtered, it must at least be properly escaped to avoid them being interpreted as part of XPath expressions.
- Use of parameterized XPath queries - Parameterization causes the input to be restricted to certain domains, such as strings or integers, and any input outside such domains is considered invalid and the query fails.
- Use of custom error pages - Attackers can glean information about the nature of queries from descriptive error messages. Input validation must be coupled with customized error pages that inform about an error without disclosing information about the database or application.

## Source

- [MITRE CAPEC CAPEC-83](https://capec.mitre.org/data/definitions/83.html)
