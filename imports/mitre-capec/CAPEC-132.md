---
slug: attack-pattern/CAPEC-132
title: "CAPEC-132 — Symlink Attack"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-132]
cwe_ids: [CWE-59]
mitre_ids: [T1547.009]
related: [weakness/CWE-59, technique/T1547.009]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-132
updated_at: 2026-08-31
summary: "An adversary positions a symbolic link in such a manner that the targeted user or application accesses the link's endpoint, assuming that it is accessing a file with the link's name."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/132.html
---

# CAPEC-132: Symlink Attack

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary positions a symbolic link in such a manner that the targeted user or application accesses the link's endpoint, assuming that it is accessing a file with the link's name.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-59](/wiki/p/weakness/CWE-59)

**ATT&CK techniques:** [T1547.009](/wiki/p/technique/T1547.009)

## Prerequisites

- The targeted application must perform the desired activities on a file without checking whether the file is a symbolic link or not. The adversary must be able to predict the name of the file the target application is modifying and be able to create a new symbolic link where that file would appear.

## Skills required

- Low: To create symlinks
- High: To identify the files and create the symlinks during the file operation time window

## Consequences

- Confidentiality: Other
- Integrity: Modify Data
- Confidentiality: Read Data
- Integrity: Modify Data
- Authorization: Execute Unauthorized Commands
- Accountability, Authentication, Authorization, Non-Repudiation: Gain Privileges

## Mitigations

- Design: Check for the existence of files to be created, if in existence verify they are neither symlinks nor hard links before opening them.
- Implementation: Use randomly generated file names for temporary files. Give the files restrictive permissions.

## Source

- [MITRE CAPEC CAPEC-132](https://capec.mitre.org/data/definitions/132.html)
