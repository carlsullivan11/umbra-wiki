---
slug: attack-pattern/CAPEC-681
title: "CAPEC-681 — Exploitation of Improperly Controlled Hardware Security Identifiers"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-681]
cwe_ids: [CWE-1259, CWE-1267, CWE-1270, CWE-1294, CWE-1302]
related: [weakness/CWE-1259, weakness/CWE-1267, weakness/CWE-1270, weakness/CWE-1294, weakness/CWE-1302]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-681
updated_at: 2026-08-31
summary: "An adversary takes advantage of missing or incorrectly configured security identifiers (e.g., tokens), which are used for access control within a System-on-Chip (SoC), to read/write data or execute a given action."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/681.html
---

# CAPEC-681: Exploitation of Improperly Controlled Hardware Security Identifiers

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Very High |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary takes advantage of missing or incorrectly configured security identifiers (e.g., tokens), which are used for access control within a System-on-Chip (SoC), to read/write data or execute a given action.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-1259](/wiki/p/weakness/CWE-1259), [CWE-1267](/wiki/p/weakness/CWE-1267), [CWE-1270](/wiki/p/weakness/CWE-1270), [CWE-1294](/wiki/p/weakness/CWE-1294), [CWE-1302](/wiki/p/weakness/CWE-1302)

## Prerequisites

- Awareness of the hardware being leveraged.
- Access to the hardware being leveraged.

## Skills required

- Medium: Ability to execute actions within the SoC.
- High: Intricate knowledge of the identifiers being utilized.

## Consequences

- Integrity: Modify Data
- Confidentiality: Read Data
- Confidentiality, Access Control, Authorization: Gain Privileges

## Mitigations

- Review generation of security identifiers for design inconsistencies and common weaknesses.
- Review security identifier decoders for design inconsistencies and common weaknesses.
- Test security identifier definition, access, and programming flow in both pre-silicon and post-silicon environments.

## Source

- [MITRE CAPEC CAPEC-681](https://capec.mitre.org/data/definitions/681.html)
