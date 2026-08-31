---
slug: attack-pattern/CAPEC-29
title: "CAPEC-29 — Leveraging Time-of-Check and Time-of-Use (TOCTOU) Race Conditions"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-29]
cwe_ids: [CWE-362, CWE-366, CWE-367, CWE-368, CWE-370, CWE-662, CWE-663, CWE-665, CWE-691]
related: [weakness/CWE-362, weakness/CWE-366, weakness/CWE-367, weakness/CWE-368, weakness/CWE-370, weakness/CWE-662, weakness/CWE-663, weakness/CWE-665, weakness/CWE-691]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-29
updated_at: 2026-08-31
summary: "This attack targets a race condition occurring between the time of check (state) for a resource and the time of use of a resource. A typical example is file access. The adversary can leverage a file access race condition by 'running the race', meaning that they would modify the r…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/29.html
---

# CAPEC-29: Leveraging Time-of-Check and Time-of-Use (TOCTOU) Race Conditions

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

This attack targets a race condition occurring between the time of check (state) for a resource and the time of use of a resource. A typical example is file access. The adversary can leverage a file access race condition by "running the race", meaning that they would modify the resource between the first time the target program accesses the file and the time the target program uses the file. During that period of time, the adversary could replace or modify the file, causing the application to behave unexpectedly.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-362](/wiki/p/weakness/CWE-362), [CWE-366](/wiki/p/weakness/CWE-366), [CWE-367](/wiki/p/weakness/CWE-367), [CWE-368](/wiki/p/weakness/CWE-368), [CWE-370](/wiki/p/weakness/CWE-370), [CWE-662](/wiki/p/weakness/CWE-662), [CWE-663](/wiki/p/weakness/CWE-663), [CWE-665](/wiki/p/weakness/CWE-665), [CWE-691](/wiki/p/weakness/CWE-691)

## Prerequisites

- A resource is access/modified concurrently by multiple processes.
- The adversary is able to modify resource.
- A race condition exists while accessing a resource.

## Skills required

- Medium: This attack can get sophisticated since the attack has to occur within a short interval of time.

## Consequences

- Integrity: Modify Data
- Confidentiality, Access Control, Authorization: Gain Privileges
- Confidentiality, Integrity, Availability: Alter Execution Logic
- Confidentiality: Read Data
- Availability: Resource Consumption

## Mitigations

- Use safe libraries to access resources such as files.
- Be aware that improper use of access function calls such as chown(), tempfile(), chmod(), etc. can cause a race condition.
- Use synchronization to control the flow of execution.
- Use static analysis tools to find race conditions.
- Pay attention to concurrency problems related to the access of resources.

## Source

- [MITRE CAPEC CAPEC-29](https://capec.mitre.org/data/definitions/29.html)
