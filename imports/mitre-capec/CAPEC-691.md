---
slug: attack-pattern/CAPEC-691
title: "CAPEC-691 — Spoof Open-Source Software Metadata"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-691]
cwe_ids: [CWE-494]
mitre_ids: [T1195.001, T1195.002]
related: [weakness/CWE-494, technique/T1195.001, technique/T1195.002]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-691
updated_at: 2026-08-31
summary: "An adversary spoofs open-source software metadata in an attempt to masquerade malicious software as popular, maintained, and trusted."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/691.html
---

# CAPEC-691: Spoof Open-Source Software Metadata

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | High |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary spoofs open-source software metadata in an attempt to masquerade malicious software as popular, maintained, and trusted.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-494](/wiki/p/weakness/CWE-494)

**ATT&CK techniques:** [T1195.001](/wiki/p/technique/T1195.001), [T1195.002](/wiki/p/technique/T1195.002)

## Prerequisites

- Identification of a popular open-source component whose metadata is to be spoofed.

## Skills required

- Medium: Ability to spoof a variety of software metadata to convince victims the source is trusted.

## Consequences

- Integrity: Modify Data
- Accountability: Hide Activities
- Access Control, Authorization: Execute Unauthorized Commands, Alter Execution Logic, Gain Privileges

## Mitigations

- Before downloading open-source software, perform precursory metadata checks to determine the author(s), frequency of updates, when the software was last updated, and if the software is widely leveraged.
- Within package managers, look for conflicting or non-unique repository references to determine if multiple packages share the same repository reference.
- Reference vulnerability databases to determine if the software contains known vulnerabilities.
- Only download open-source software from reputable hosting sites or package managers.
- Only download open-source software that has been adequately signed by the developer(s). For repository commits/tags, look for the "Verified" status and for developers leveraging "Vigilant Mode" (GitHub) or similar modes.
- After downloading open-source software, ensure integrity values have not changed.
- Before executing or incorporating the software, leverage automated testing techniques (e.g., static and dynamic analysis) to determine if the software behaves maliciously.

## Source

- [MITRE CAPEC CAPEC-691](https://capec.mitre.org/data/definitions/691.html)
