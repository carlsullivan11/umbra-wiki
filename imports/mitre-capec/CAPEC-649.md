---
slug: attack-pattern/CAPEC-649
title: "CAPEC-649 — Adding a Space to a File Extension"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-649]
cwe_ids: [CWE-46]
mitre_ids: [T1036.006]
related: [weakness/CWE-46, technique/T1036.006]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-649
updated_at: 2026-08-31
summary: "An adversary adds a space character to the end of a file extension and takes advantage of an application that does not properly neutralize trailing special elements in file names. This extra space, which can be difficult for a user to notice, affects which default application is …"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/649.html
---

# CAPEC-649: Adding a Space to a File Extension

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary adds a space character to the end of a file extension and takes advantage of an application that does not properly neutralize trailing special elements in file names. This extra space, which can be difficult for a user to notice, affects which default application is used to operate on the file and can be leveraged by the adversary to control execution.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-46](/wiki/p/weakness/CWE-46)

**ATT&CK techniques:** [T1036.006](/wiki/p/technique/T1036.006)

## Prerequisites

- The use of the file must be controlled by the file extension.

## Consequences

- Confidentiality, Integrity, Availability: Execute Unauthorized Commands

## Mitigations

- File extensions should be checked to see if non-visible characters are being included.

## Source

- [MITRE CAPEC CAPEC-649](https://capec.mitre.org/data/definitions/649.html)
