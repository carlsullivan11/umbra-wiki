---
slug: attack-pattern/CAPEC-108
title: "CAPEC-108 — Command Line Execution through SQL Injection"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-108]
cwe_ids: [CWE-20, CWE-74, CWE-78, CWE-89, CWE-114]
related: [weakness/CWE-20, weakness/CWE-74, weakness/CWE-78, weakness/CWE-89, weakness/CWE-114]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-108
updated_at: 2026-08-31
summary: "An attacker uses standard SQL injection methods to inject data into the command line for execution. This could be done directly through misuse of directives such as MSSQL_xp_cmdshell or indirectly through injection of data into the database that would be interpreted as shell comm…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/108.html
---

# CAPEC-108: Command Line Execution through SQL Injection

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Very High |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker uses standard SQL injection methods to inject data into the command line for execution. This could be done directly through misuse of directives such as MSSQL_xp_cmdshell or indirectly through injection of data into the database that would be interpreted as shell commands. Sometime later, an unscrupulous backend application (or could be part of the functionality of the same application) fetches the injected data stored in the database and uses this data as command line arguments without performing proper validation. The malicious data escapes that data plane by spawning new commands to be executed on the host.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-20](/wiki/p/weakness/CWE-20), [CWE-74](/wiki/p/weakness/CWE-74), [CWE-78](/wiki/p/weakness/CWE-78), [CWE-89](/wiki/p/weakness/CWE-89), [CWE-114](/wiki/p/weakness/CWE-114)

## Prerequisites

- The application does not properly validate data before storing in the database
- Backend application implicitly trusts the data stored in the database
- Malicious data is used on the backend as a command line argument

## Skills required

- High: The attacker most likely has to be familiar with the internal functionality of the system to launch this attack. Without that knowledge, there are not many feedback mechanisms to give an attacker the indication of how to perform command injection or whether the attack is succeeding.

## Consequences

- Integrity: Modify Data
- Confidentiality: Read Data
- Availability: Unreliable Execution
- Confidentiality, Access Control, Authorization: Gain Privileges
- Confidentiality, Integrity, Availability: Execute Unauthorized Commands

## Mitigations

- Disable MSSQL xp_cmdshell directive on the database
- Properly validate the data (syntactically and semantically) before writing it to the database.
- Do not implicitly trust the data stored in the database. Re-validate it prior to usage to make sure that it is safe to use in a given context (e.g. as a command line argument).

## Source

- [MITRE CAPEC CAPEC-108](https://capec.mitre.org/data/definitions/108.html)
