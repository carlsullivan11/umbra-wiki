---
slug: attack-pattern/CAPEC-7
title: "CAPEC-7 — Blind SQL Injection"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-7]
cwe_ids: [CWE-20, CWE-74, CWE-89, CWE-209, CWE-697, CWE-707]
related: [weakness/CWE-20, weakness/CWE-74, weakness/CWE-89, weakness/CWE-209, weakness/CWE-697, weakness/CWE-707]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-7
updated_at: 2026-08-31
summary: "Blind SQL Injection results from an insufficient mitigation for SQL Injection. Although suppressing database error messages are considered best practice, the suppression alone is not sufficient to prevent SQL Injection. Blind SQL Injection is a form of SQL Injection that overcome…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/7.html
---

# CAPEC-7: Blind SQL Injection

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

Blind SQL Injection results from an insufficient mitigation for SQL Injection. Although suppressing database error messages are considered best practice, the suppression alone is not sufficient to prevent SQL Injection. Blind SQL Injection is a form of SQL Injection that overcomes the lack of error messages. Without the error messages that facilitate SQL Injection, the adversary constructs input strings that probe the target through simple Boolean SQL expressions. The adversary can determine if the syntax and structure of the injection was successful based on whether the query was executed or not. Applied iteratively, the adversary determines how and where the target is vulnerable to SQL Injection.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-20](/wiki/p/weakness/CWE-20), [CWE-74](/wiki/p/weakness/CWE-74), [CWE-89](/wiki/p/weakness/CWE-89), [CWE-209](/wiki/p/weakness/CWE-209), [CWE-697](/wiki/p/weakness/CWE-697), [CWE-707](/wiki/p/weakness/CWE-707)

## Prerequisites

- SQL queries used by the application to store, retrieve or modify data.
- User-controllable input that is not properly validated by the application as part of SQL queries.

## Skills required

- Medium: Determining the database type and version, as well as the right number and type of parameters to the query being injected in the absence of error messages requires greater skill than reverse-engineering database error messages.

## Consequences

- Integrity: Modify Data
- Confidentiality: Read Data
- Confidentiality, Integrity, Availability: Execute Unauthorized Commands

## Mitigations

- Security by Obscurity is not a solution to preventing SQL Injection. Rather than suppress error messages and exceptions, the application must handle them gracefully, returning either a custom error page or redirecting the user to a default page, without revealing any information about the database or the application internals.
- Strong input validation - All user-controllable input must be validated and filtered for illegal characters as well as SQL content. Keywords such as UNION, SELECT or INSERT must be filtered in addition to characters such as a single-quote(') or SQL-comments (--) based on the context in which they appear.

## Source

- [MITRE CAPEC CAPEC-7](https://capec.mitre.org/data/definitions/7.html)
