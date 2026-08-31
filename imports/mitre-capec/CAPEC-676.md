---
slug: attack-pattern/CAPEC-676
title: "CAPEC-676 — NoSQL Injection"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-676]
cwe_ids: [CWE-943, CWE-1286]
related: [weakness/CWE-943, weakness/CWE-1286]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-676
updated_at: 2026-08-31
summary: "An adversary targets software that constructs NoSQL statements based on user input or with parameters vulnerable to operator replacement in order to achieve a variety of technical impacts such as escalating privileges, bypassing authentication, and/or executing code."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/676.html
---

# CAPEC-676: NoSQL Injection

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary targets software that constructs NoSQL statements based on user input or with parameters vulnerable to operator replacement in order to achieve a variety of technical impacts such as escalating privileges, bypassing authentication, and/or executing code.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-943](/wiki/p/weakness/CWE-943), [CWE-1286](/wiki/p/weakness/CWE-1286)

## Prerequisites

- Awareness of the technology stack being leveraged by the target application.
- NoSQL queries used by the application to store, retrieve, or modify data.
- User-controllable input that is not properly validated by the application as part of NoSQL queries.
- Target potentially susceptible to operator replacement attacks.

## Skills required

- Low: For keyword and JavaScript injection attacks, it is fairly simple for someone with basic NoSQL knowledge to perform NoSQL injection, once the target's technology stack has been determined.
- Medium: For operator replacement attacks, the adversary must also have knowledge of HTTP Parameter Pollution attacks and how to conduct them.

## Consequences

- Integrity: Modify Data
- Confidentiality: Read Data
- Confidentiality, Integrity, Availability: Execute Unauthorized Commands
- Confidentiality, Access Control, Authorization: Gain Privileges

## Mitigations

- Strong input validation - All user-controllable input must be validated and filtered for illegal characters as well as relevant NoSQL and JavaScript content. NoSQL-specific keywords, such as $ne, $eq or $gt for MongoDB, must be filtered in addition to characters such as a single-quote(') or semicolons (;) based on the context in which they appear. Validation should also extend to expected types.
- If possible, leverage safe APIs (e.g., PyMongo and Flask-PyMongo for Python and MongoDB) for queries as opposed to building queries from strings.
- Ensure the most recent version of a NoSQL database and it's corresponding API are used by the application.
- Use of custom error pages - Adversaries can glean information about the nature of queries from descriptive error messages. Input validation must be coupled with customized error pages that inform about an error without disclosing information about the database or application.
- Exercise the principle of Least Privilege with regards to application accounts to minimize damage if a NoSQL injection attack is successful.
- If using MongoDB, disable server-side JavaScript execution and leverage a sanitization module such as "mongo-sanitize".
- If using PHP with MongoDB, ensure all special query operators (starting with $) use single quotes to prevent operator replacement attacks.
- Additional mitigations will depend on the NoSQL database, API, and programming language leveraged by the application.

## Source

- [MITRE CAPEC CAPEC-676](https://capec.mitre.org/data/definitions/676.html)
