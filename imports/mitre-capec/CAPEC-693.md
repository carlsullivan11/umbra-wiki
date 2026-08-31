---
slug: attack-pattern/CAPEC-693
title: "CAPEC-693 — StarJacking"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-693]
cwe_ids: [CWE-494]
related: [weakness/CWE-494]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-693
updated_at: 2026-08-31
summary: "An adversary spoofs software popularity metadata to deceive users into believing that a maliciously provided package is widely used and originates from a trusted source."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/693.html
---

# CAPEC-693: StarJacking

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | High |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary spoofs software popularity metadata to deceive users into believing that a maliciously provided package is widely used and originates from a trusted source.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-494](/wiki/p/weakness/CWE-494)

## Prerequisites

- Identification of a popular open-source package whose popularity metadata is to be used for the malicious package.

## Skills required

- Low: Ability to provide a package to a package manager and associate a popular package's source code repository URL.

## Consequences

- Integrity: Modify Data
- Accountability: Hide Activities
- Access Control, Authorization: Execute Unauthorized Commands, Alter Execution Logic, Gain Privileges

## Mitigations

- Before downloading open-source packages, perform precursory metadata checks to determine the author(s), frequency of updates, when the software was last updated, and if the software is widely leveraged.
- Look for conflicting or non-unique repository references to determine if multiple packages share the same repository reference.
- Reference vulnerability databases to determine if the software contains known vulnerabilities.
- Only download open-source packages from reputable package managers.
- After downloading open-source packages, ensure integrity values have not changed.
- Before executing or incorporating the package, leverage automated testing techniques (e.g., static and dynamic analysis) to determine if the software behaves maliciously.

## Source

- [MITRE CAPEC CAPEC-693](https://capec.mitre.org/data/definitions/693.html)
