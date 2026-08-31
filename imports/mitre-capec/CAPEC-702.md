---
slug: attack-pattern/CAPEC-702
title: "CAPEC-702 — Exploiting Incorrect Chaining or Granularity of Hardware Debug Components"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-702]
cwe_ids: [CWE-1296]
related: [weakness/CWE-1296]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-702
updated_at: 2026-08-31
summary: "An adversary exploits incorrect chaining or granularity of hardware debug components in order to gain unauthorized access to debug functionality on a chip. This happens when authorization is not checked on a per function basis and is assumed for a chain or group of debug function…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/702.html
---

# CAPEC-702: Exploiting Incorrect Chaining or Granularity of Hardware Debug Components

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary exploits incorrect chaining or granularity of hardware debug components in order to gain unauthorized access to debug functionality on a chip. This happens when authorization is not checked on a per function basis and is assumed for a chain or group of debug functionality.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-1296](/wiki/p/weakness/CWE-1296)

## Prerequisites

- Hardware device has an exposed debug interface

## Skills required

- Medium: Ability to identify physical debug interfaces on a device
- Medium: Ability to operate devices to scan and connect to an exposed debug interface

## Consequences

- Confidentiality: Read Data
- Integrity: Modify Data
- Access Control, Authorization: Gain Privileges

## Mitigations

- Implement: Ensure that debug components are properly chained, and their granularity is maintained at different authorization levels
- Perform Post-silicon validation tests at various authorization levels to ensure that debug components are only accessible to authorized users

## Source

- [MITRE CAPEC CAPEC-702](https://capec.mitre.org/data/definitions/702.html)
