---
slug: attack-pattern/CAPEC-136
title: "CAPEC-136 — LDAP Injection"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-136]
cwe_ids: [CWE-20, CWE-77, CWE-90]
related: [weakness/CWE-20, weakness/CWE-77, weakness/CWE-90]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-136
updated_at: 2026-08-31
summary: "An attacker manipulates or crafts an LDAP query for the purpose of undermining the security of the target. Some applications use user input to create LDAP queries that are processed by an LDAP server. For example, a user might provide their username during authentication and the …"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/136.html
---

# CAPEC-136: LDAP Injection

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker manipulates or crafts an LDAP query for the purpose of undermining the security of the target. Some applications use user input to create LDAP queries that are processed by an LDAP server. For example, a user might provide their username during authentication and the username might be inserted in an LDAP query during the authentication process. An attacker could use this input to inject additional commands into an LDAP query that could disclose sensitive information. For example, entering a * in the aforementioned query might return information about all users on the system. This attack is very similar to an SQL injection attack in that it manipulates a query to gather additional information or coerce a particular return value.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-20](/wiki/p/weakness/CWE-20), [CWE-77](/wiki/p/weakness/CWE-77), [CWE-90](/wiki/p/weakness/CWE-90)

## Prerequisites

- The target application must accept a string as user input, fail to sanitize characters that have a special meaning in LDAP queries in the user input, and insert the user-supplied string in an LDAP query which is then processed.

## Skills required

- Medium: The attacker needs to have knowledge of LDAP, especially its query syntax.

## Consequences

- Availability: Unreliable Execution
- Integrity: Modify Data
- Confidentiality: Read Data
- Authorization: Execute Unauthorized Commands
- Accountability, Authentication, Authorization, Non-Repudiation: Gain Privileges
- Access Control, Authorization: Bypass Protection Mechanism

## Mitigations

- Strong input validation - All user-controllable input must be validated and filtered for illegal characters as well as LDAP content.
- Use of custom error pages - Attackers can glean information about the nature of queries from descriptive error messages. Input validation must be coupled with customized error pages that inform about an error without disclosing information about the LDAP or application.

## Source

- [MITRE CAPEC CAPEC-136](https://capec.mitre.org/data/definitions/136.html)
