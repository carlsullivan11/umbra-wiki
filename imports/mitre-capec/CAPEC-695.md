---
slug: attack-pattern/CAPEC-695
title: "CAPEC-695 — Repo Jacking"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-695]
cwe_ids: [CWE-494, CWE-829]
mitre_ids: [T1195.001]
related: [weakness/CWE-494, weakness/CWE-829, technique/T1195.001]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-695
updated_at: 2026-08-31
summary: "An adversary takes advantage of the redirect property of directly linked Version Control System (VCS) repositories to trick users into incorporating malicious code into their applications."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/695.html
---

# CAPEC-695: Repo Jacking

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | High |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary takes advantage of the redirect property of directly linked Version Control System (VCS) repositories to trick users into incorporating malicious code into their applications.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-494](/wiki/p/weakness/CWE-494), [CWE-829](/wiki/p/weakness/CWE-829)

**ATT&CK techniques:** [T1195.001](/wiki/p/technique/T1195.001)

## Prerequisites

- Identification of a popular repository that may be directly referenced in numerous software applications
- A repository owner/maintainer who has recently changed their username or deleted their account

## Skills required

- Low: Ability to create an account on a VCS hosting site and recreate an existing directory structure.
- Low: Ability to create malware that can exploit various software applications.

## Consequences

- Integrity: Read Data, Modify Data
- Access Control, Authorization: Execute Unauthorized Commands, Alter Execution Logic, Gain Privileges

## Mitigations

- Leverage dedicated package managers instead of directly linking to VCS repositories.
- Utilize version pinning and lock files to prevent use of maliciously modified repositories.
- Implement "vendoring" (i.e., including third-party dependencies locally) and leverage automated testing techniques (e.g., static analysis) to determine if the software behaves maliciously.
- Leverage automated tools, such as Checkmarx's "ChainJacking" tool, to determine susceptibility to Repo Jacking attacks.

## Source

- [MITRE CAPEC CAPEC-695](https://capec.mitre.org/data/definitions/695.html)
