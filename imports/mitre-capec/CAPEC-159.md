---
slug: attack-pattern/CAPEC-159
title: "CAPEC-159 — Redirect Access to Libraries"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-159]
cwe_ids: [CWE-706]
mitre_ids: [T1574.008]
related: [weakness/CWE-706, technique/T1574.008]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-159
updated_at: 2026-08-31
summary: "An adversary exploits a weakness in the way an application searches for external libraries to manipulate the execution flow to point to an adversary supplied library or code base. This pattern of attack allows the adversary to compromise the application or server via the executio…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/159.html
---

# CAPEC-159: Redirect Access to Libraries

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Very High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary exploits a weakness in the way an application searches for external libraries to manipulate the execution flow to point to an adversary supplied library or code base. This pattern of attack allows the adversary to compromise the application or server via the execution of unauthorized code. An application typically makes calls to functions that are a part of libraries external to the application. These libraries may be part of the operating system or they may be third party libraries. If an adversary can redirect an application's attempts to access these libraries to other libraries that the adversary supplies, the adversary will be able to force the targeted application to execute arbitrary code. This is especially dangerous if the targeted application has enhanced privileges. Access can be redirected through a number of techniques, including the use of symbolic links, search path modification, and relative path manipulation.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-706](/wiki/p/weakness/CWE-706)

**ATT&CK techniques:** [T1574.008](/wiki/p/technique/T1574.008)

## Prerequisites

- The target must utilize external libraries and must fail to verify the integrity of these libraries before using them.

## Skills required

- Low: To modify the entries in the configuration file pointing to malicious libraries
- Medium: To force symlink and timing issues for redirecting access to libraries
- High: To reverse engineering the libraries and inject malicious code into the libraries

## Consequences

- Authorization: Execute Unauthorized Commands
- Access Control, Authorization: Bypass Protection Mechanism

## Mitigations

- Implementation: Restrict the permission to modify the entries in the configuration file.
- Implementation: Check the integrity of the dynamically linked libraries before use them.
- Implementation: Use obfuscation and other techniques to prevent reverse engineering the libraries.

## Source

- [MITRE CAPEC CAPEC-159](https://capec.mitre.org/data/definitions/159.html)
