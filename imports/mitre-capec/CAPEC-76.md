---
slug: attack-pattern/CAPEC-76
title: "CAPEC-76 — Manipulating Web Input to File System Calls"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-76]
cwe_ids: [CWE-15, CWE-22, CWE-23, CWE-59, CWE-73, CWE-74, CWE-77, CWE-272, CWE-285, CWE-346, CWE-348]
related: [weakness/CWE-15, weakness/CWE-22, weakness/CWE-23, weakness/CWE-59, weakness/CWE-73, weakness/CWE-74, weakness/CWE-77, weakness/CWE-272, weakness/CWE-285, weakness/CWE-346, weakness/CWE-348]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-76
updated_at: 2026-08-31
summary: "An attacker manipulates inputs to the target software which the target software passes to file system calls in the OS. The goal is to gain access to, and perhaps modify, areas of the file system that the target software did not intend to be accessible."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/76.html
---

# CAPEC-76: Manipulating Web Input to File System Calls

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Very High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker manipulates inputs to the target software which the target software passes to file system calls in the OS. The goal is to gain access to, and perhaps modify, areas of the file system that the target software did not intend to be accessible.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-15](/wiki/p/weakness/CWE-15), [CWE-22](/wiki/p/weakness/CWE-22), [CWE-23](/wiki/p/weakness/CWE-23), [CWE-59](/wiki/p/weakness/CWE-59), [CWE-73](/wiki/p/weakness/CWE-73), [CWE-74](/wiki/p/weakness/CWE-74), [CWE-77](/wiki/p/weakness/CWE-77), [CWE-272](/wiki/p/weakness/CWE-272), [CWE-285](/wiki/p/weakness/CWE-285), [CWE-346](/wiki/p/weakness/CWE-346), [CWE-348](/wiki/p/weakness/CWE-348)

## Prerequisites

- Program must allow for user controlled variables to be applied directly to the filesystem

## Skills required

- Low: To identify file system entry point and execute against an over-privileged system interface

## Consequences

- Confidentiality, Access Control, Authorization: Gain Privileges
- Integrity: Modify Data

## Mitigations

- Design: Enforce principle of least privilege.
- Design: Ensure all input is validated, and does not contain file system commands
- Design: Run server interfaces with a non-root account and/or utilize chroot jails or other configuration techniques to constrain privileges even if attacker gains some limited access to commands.
- Design: For interactive user applications, consider if direct file system interface is necessary, instead consider having the application proxy communication.
- Implementation: Perform testing such as pen-testing and vulnerability scanning to identify directories, programs, and interfaces that grant direct access to executables.

## Source

- [MITRE CAPEC CAPEC-76](https://capec.mitre.org/data/definitions/76.html)
