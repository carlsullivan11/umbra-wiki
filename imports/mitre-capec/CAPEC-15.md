---
slug: attack-pattern/CAPEC-15
title: "CAPEC-15 — Command Delimiters"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-15]
cwe_ids: [CWE-77, CWE-78, CWE-93, CWE-138, CWE-140, CWE-146, CWE-154, CWE-157, CWE-184, CWE-185, CWE-697]
related: [weakness/CWE-77, weakness/CWE-78, weakness/CWE-93, weakness/CWE-138, weakness/CWE-140, weakness/CWE-146, weakness/CWE-154, weakness/CWE-157, weakness/CWE-184, weakness/CWE-185, weakness/CWE-697]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-15
updated_at: 2026-08-31
summary: "An attack of this type exploits a programs' vulnerabilities that allows an attacker's commands to be concatenated onto a legitimate command with the intent of targeting other resources such as the file system or database. The system that uses a filter or denylist input validation…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/15.html
---

# CAPEC-15: Command Delimiters

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attack of this type exploits a programs' vulnerabilities that allows an attacker's commands to be concatenated onto a legitimate command with the intent of targeting other resources such as the file system or database. The system that uses a filter or denylist input validation, as opposed to allowlist validation is vulnerable to an attacker who predicts delimiters (or combinations of delimiters) not present in the filter or denylist. As with other injection attacks, the attacker uses the command delimiter payload as an entry point to tunnel through the application and activate additional attacks through SQL queries, shell commands, network scanning, and so on.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-77](/wiki/p/weakness/CWE-77), [CWE-78](/wiki/p/weakness/CWE-78), [CWE-93](/wiki/p/weakness/CWE-93), [CWE-138](/wiki/p/weakness/CWE-138), [CWE-140](/wiki/p/weakness/CWE-140), [CWE-146](/wiki/p/weakness/CWE-146), [CWE-154](/wiki/p/weakness/CWE-154), [CWE-157](/wiki/p/weakness/CWE-157), [CWE-184](/wiki/p/weakness/CWE-184), [CWE-185](/wiki/p/weakness/CWE-185), [CWE-697](/wiki/p/weakness/CWE-697)

## Prerequisites

- Software's input validation or filtering must not detect and block presence of additional malicious command.

## Skills required

- Medium: The attacker has to identify injection vector, identify the specific commands, and optionally collect the output, i.e. from an interactive session.

## Consequences

- Confidentiality, Integrity, Availability: Execute Unauthorized Commands
- Confidentiality: Read Data

## Mitigations

- Design: Perform allowlist validation against a positive specification for command length, type, and parameters.
- Design: Limit program privileges, so if commands circumvent program input validation or filter routines then commands do not running under a privileged account
- Implementation: Perform input validation for all remote content.
- Implementation: Use type conversions such as JDBC prepared statements.

## Source

- [MITRE CAPEC CAPEC-15](https://capec.mitre.org/data/definitions/15.html)
