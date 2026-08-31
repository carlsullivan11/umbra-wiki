---
slug: attack-pattern/CAPEC-110
title: "CAPEC-110 — SQL Injection through SOAP Parameter Tampering"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-110]
cwe_ids: [CWE-20, CWE-89]
related: [weakness/CWE-20, weakness/CWE-89]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-110
updated_at: 2026-08-31
summary: "An attacker modifies the parameters of the SOAP message that is sent from the service consumer to the service provider to initiate a SQL injection attack. On the service provider side, the SOAP message is parsed and parameters are not properly validated before being used to acces…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/110.html
---

# CAPEC-110: SQL Injection through SOAP Parameter Tampering

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Very High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker modifies the parameters of the SOAP message that is sent from the service consumer to the service provider to initiate a SQL injection attack. On the service provider side, the SOAP message is parsed and parameters are not properly validated before being used to access a database in a way that does not use parameter binding, thus enabling the attacker to control the structure of the executed SQL query. This pattern describes a SQL injection attack with the delivery mechanism being a SOAP message.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-20](/wiki/p/weakness/CWE-20), [CWE-89](/wiki/p/weakness/CWE-89)

## Prerequisites

- SOAP messages are used as a communication mechanism in the system
- SOAP parameters are not properly validated at the service provider
- The service provider does not properly utilize parameter binding when building SQL queries

## Skills required

- Medium: If the attacker is able to gain good understanding of the system's database schema
- High: If the attacker has to perform Blind SQL Injection

## Consequences

- Integrity: Modify Data
- Availability: Unreliable Execution
- Confidentiality: Read Data
- Confidentiality, Access Control, Authorization: Gain Privileges
- Confidentiality, Integrity, Availability: Execute Unauthorized Commands

## Mitigations

- Properly validate and sanitize/reject user input at the service provider.
- Ensure that prepared statements or other mechanism that enables parameter binding is used when accessing the database in a way that would prevent the attackers' supplied data from controlling the structure of the executed query.
- At the database level, ensure that the database user used by the application in a particular context has the minimum needed privileges to the database that are needed to perform the operation. When possible, run queries against pre-generated views rather than the tables directly.

## Source

- [MITRE CAPEC CAPEC-110](https://capec.mitre.org/data/definitions/110.html)
