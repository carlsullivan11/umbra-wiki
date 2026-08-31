---
slug: attack-pattern/CAPEC-679
title: "CAPEC-679 — Exploitation of Improperly Configured or Implemented Memory Protections"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-679]
cwe_ids: [CWE-1222, CWE-1252, CWE-1257, CWE-1260, CWE-1274, CWE-1282, CWE-1312, CWE-1316, CWE-1326]
related: [weakness/CWE-1222, weakness/CWE-1252, weakness/CWE-1257, weakness/CWE-1260, weakness/CWE-1274, weakness/CWE-1282, weakness/CWE-1312, weakness/CWE-1316, weakness/CWE-1326]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-679
updated_at: 2026-08-31
summary: "An adversary takes advantage of missing or incorrectly configured access control within memory to read/write data or inject malicious code into said memory."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/679.html
---

# CAPEC-679: Exploitation of Improperly Configured or Implemented Memory Protections

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Very High |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary takes advantage of missing or incorrectly configured access control within memory to read/write data or inject malicious code into said memory.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-1222](/wiki/p/weakness/CWE-1222), [CWE-1252](/wiki/p/weakness/CWE-1252), [CWE-1257](/wiki/p/weakness/CWE-1257), [CWE-1260](/wiki/p/weakness/CWE-1260), [CWE-1274](/wiki/p/weakness/CWE-1274), [CWE-1282](/wiki/p/weakness/CWE-1282), [CWE-1312](/wiki/p/weakness/CWE-1312), [CWE-1316](/wiki/p/weakness/CWE-1316), [CWE-1326](/wiki/p/weakness/CWE-1326)

## Prerequisites

- Access to the hardware being leveraged.

## Skills required

- Medium: Ability to craft malicious code to inject into the memory region.
- High: Intricate knowledge of memory structures.

## Consequences

- Integrity: Modify Data
- Confidentiality: Read Data
- Confidentiality, Integrity, Availability: Execute Unauthorized Commands
- Confidentiality, Access Control, Authorization: Gain Privileges

## Mitigations

- Ensure that protected and unprotected memory ranges are isolated and do not overlap.
- If memory regions must overlap, leverage memory priority schemes if memory regions can overlap.
- Ensure that original and mirrored memory regions apply the same protections.
- Ensure immutable code or data is programmed into ROM or write-once memory.

## Source

- [MITRE CAPEC CAPEC-679](https://capec.mitre.org/data/definitions/679.html)
