---
slug: attack-pattern/CAPEC-25
title: "CAPEC-25 — Forced Deadlock"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-25]
cwe_ids: [CWE-412, CWE-567, CWE-662, CWE-667, CWE-833, CWE-1322]
mitre_ids: [T1499.004]
related: [weakness/CWE-412, weakness/CWE-567, weakness/CWE-662, weakness/CWE-667, weakness/CWE-833, weakness/CWE-1322, technique/T1499.004]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-25
updated_at: 2026-08-31
summary: "The adversary triggers and exploits a deadlock condition in the target software to cause a denial of service. A deadlock can occur when two or more competing actions are waiting for each other to finish, and thus neither ever does. Deadlock conditions can be difficult to detect."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/25.html
---

# CAPEC-25: Forced Deadlock

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | High |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

The adversary triggers and exploits a deadlock condition in the target software to cause a denial of service. A deadlock can occur when two or more competing actions are waiting for each other to finish, and thus neither ever does. Deadlock conditions can be difficult to detect.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-412](/wiki/p/weakness/CWE-412), [CWE-567](/wiki/p/weakness/CWE-567), [CWE-662](/wiki/p/weakness/CWE-662), [CWE-667](/wiki/p/weakness/CWE-667), [CWE-833](/wiki/p/weakness/CWE-833), [CWE-1322](/wiki/p/weakness/CWE-1322)

**ATT&CK techniques:** [T1499.004](/wiki/p/technique/T1499.004)

## Prerequisites

- The target host has a deadlock condition. There are four conditions for a deadlock to occur, known as the Coffman conditions. [REF-101]
- The target host exposes an API to the user.

## Skills required

- Medium: This type of attack may be sophisticated and require knowledge about the system's resources and APIs.

## Consequences

- Availability: Resource Consumption

## Mitigations

- Use known algorithm to avoid deadlock condition (for instance non-blocking synchronization algorithms).
- For competing actions, use well-known libraries which implement synchronization.

## Source

- [MITRE CAPEC CAPEC-25](https://capec.mitre.org/data/definitions/25.html)
