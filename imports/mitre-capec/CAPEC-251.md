---
slug: attack-pattern/CAPEC-251
title: "CAPEC-251 — Local Code Inclusion"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-251]
cwe_ids: [CWE-829]
mitre_ids: [T1055]
related: [weakness/CWE-829, technique/T1055]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-251
updated_at: 2026-08-31
summary: "The attacker forces an application to load arbitrary code files from the local machine. The attacker could use this to try to load old versions of library files that have known vulnerabilities, to load files that the attacker placed on the local machine during a prior attack, or …"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/251.html
---

# CAPEC-251: Local Code Inclusion

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Medium |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

The attacker forces an application to load arbitrary code files from the local machine. The attacker could use this to try to load old versions of library files that have known vulnerabilities, to load files that the attacker placed on the local machine during a prior attack, or to otherwise change the functionality of the targeted application in unexpected ways.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-829](/wiki/p/weakness/CWE-829)

**ATT&CK techniques:** [T1055](/wiki/p/technique/T1055)

## Prerequisites

- The targeted application must have a bug that allows an adversary to control which code file is loaded at some juncture.
- Some variants of this attack may require that old versions of some code files be present and in predictable locations.

## Consequences

- Integrity: Execute Unauthorized Commands
- Confidentiality: Read Data

## Mitigations

- Implementation: Avoid passing user input to filesystem or framework API. If necessary to do so, implement a specific, allowlist approach.

## Source

- [MITRE CAPEC CAPEC-251](https://capec.mitre.org/data/definitions/251.html)
