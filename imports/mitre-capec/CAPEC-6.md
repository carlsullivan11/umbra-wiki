---
slug: attack-pattern/CAPEC-6
title: "CAPEC-6 — Argument Injection"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-6]
cwe_ids: [CWE-74, CWE-78, CWE-146, CWE-184, CWE-185, CWE-697]
related: [weakness/CWE-74, weakness/CWE-78, weakness/CWE-146, weakness/CWE-184, weakness/CWE-185, weakness/CWE-697]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-6
updated_at: 2026-08-31
summary: "An attacker changes the behavior or state of a targeted application through injecting data or command syntax through the targets use of non-validated and non-filtered arguments of exposed services or methods."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/6.html
---

# CAPEC-6: Argument Injection

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker changes the behavior or state of a targeted application through injecting data or command syntax through the targets use of non-validated and non-filtered arguments of exposed services or methods.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-74](/wiki/p/weakness/CWE-74), [CWE-78](/wiki/p/weakness/CWE-78), [CWE-146](/wiki/p/weakness/CWE-146), [CWE-184](/wiki/p/weakness/CWE-184), [CWE-185](/wiki/p/weakness/CWE-185), [CWE-697](/wiki/p/weakness/CWE-697)

## Prerequisites

- Target software fails to strip all user-supplied input of any content that could cause the shell to perform unexpected actions.
- Software must allow for unvalidated or unfiltered input to be executed on operating system shell, and, optionally, the system configuration must allow for output to be sent back to client.

## Skills required

- Medium: The attacker has to identify injection vector, identify the operating system-specific commands, and optionally collect the output.

## Consequences

- Confidentiality, Access Control, Authorization: Gain Privileges
- Integrity: Modify Data
- Confidentiality: Read Data

## Mitigations

- Design: Do not program input values directly on command shell, instead treat user input as guilty until proven innocent. Build a function that takes user input and converts it to applications specific types and values, stripping or filtering out all unauthorized commands and characters in the process.
- Design: Limit program privileges, so if metacharacters or other methods circumvent program input validation routines and shell access is attained then it is not running under a privileged account. chroot jails create a sandbox for the application to execute in, making it more difficult for an attacker to elevate privilege even in the case that a compromise has occurred.
- Implementation: Implement an audit log that is written to a separate host, in the event of a compromise the audit log may be able to provide evidence and details of the compromise.

## Source

- [MITRE CAPEC CAPEC-6](https://capec.mitre.org/data/definitions/6.html)
