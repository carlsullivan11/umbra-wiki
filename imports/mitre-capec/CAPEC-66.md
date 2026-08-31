---
slug: attack-pattern/CAPEC-66
title: "CAPEC-66 — SQL Injection"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-66]
cwe_ids: [CWE-89, CWE-1286]
related: [weakness/CWE-89, weakness/CWE-1286]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-66
updated_at: 2026-08-31
summary: "This attack exploits target software that constructs SQL statements based on user input. An attacker crafts input strings so that when the target software constructs SQL statements based on the input, the resulting SQL statement performs actions other than those the application i…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/66.html
---

# CAPEC-66: SQL Injection

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

This attack exploits target software that constructs SQL statements based on user input. An attacker crafts input strings so that when the target software constructs SQL statements based on the input, the resulting SQL statement performs actions other than those the application intended. SQL Injection results from failure of the application to appropriately validate input.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-89](/wiki/p/weakness/CWE-89), [CWE-1286](/wiki/p/weakness/CWE-1286)

## Prerequisites

- SQL queries used by the application to store, retrieve or modify data.
- User-controllable input that is not properly validated by the application as part of SQL queries.

## Skills required

- Low: It is fairly simple for someone with basic SQL knowledge to perform SQL injection, in general. In certain instances, however, specific knowledge of the database employed may be required.

## Consequences

- Integrity: Modify Data
- Confidentiality: Read Data
- Confidentiality, Integrity, Availability: Execute Unauthorized Commands
- Confidentiality, Access Control, Authorization: Gain Privileges

## Mitigations

- Strong input validation - All user-controllable input must be validated and filtered for illegal characters as well as SQL content. Keywords such as UNION, SELECT or INSERT must be filtered in addition to characters such as a single-quote(') or SQL-comments (--) based on the context in which they appear.
- Use of parameterized queries or stored procedures - Parameterization causes the input to be restricted to certain domains, such as strings or integers, and any input outside such domains is considered invalid and the query fails. Note that SQL Injection is possible even in the presence of stored procedures if the eventual query is constructed dynamically.
- Use of custom error pages - Attackers can glean information about the nature of queries from descriptive error messages. Input validation must be coupled with customized error pages that inform about an error without disclosing information about the database or application.

## Source

- [MITRE CAPEC CAPEC-66](https://capec.mitre.org/data/definitions/66.html)
