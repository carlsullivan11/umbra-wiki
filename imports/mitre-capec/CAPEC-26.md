---
slug: attack-pattern/CAPEC-26
title: "CAPEC-26 — Leveraging Race Conditions"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-26]
cwe_ids: [CWE-362, CWE-363, CWE-366, CWE-368, CWE-370, CWE-662, CWE-665, CWE-667, CWE-689, CWE-1223, CWE-1254, CWE-1298]
related: [weakness/CWE-362, weakness/CWE-363, weakness/CWE-366, weakness/CWE-368, weakness/CWE-370, weakness/CWE-662, weakness/CWE-665, weakness/CWE-667, weakness/CWE-689, weakness/CWE-1223, weakness/CWE-1254, weakness/CWE-1298]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-26
updated_at: 2026-08-31
summary: "The adversary targets a race condition occurring when multiple processes access and manipulate the same resource concurrently, and the outcome of the execution depends on the particular order in which the access takes place. The adversary can leverage a race condition by 'running…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/26.html
---

# CAPEC-26: Leveraging Race Conditions

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

The adversary targets a race condition occurring when multiple processes access and manipulate the same resource concurrently, and the outcome of the execution depends on the particular order in which the access takes place. The adversary can leverage a race condition by "running the race", modifying the resource and modifying the normal execution flow. For instance, a race condition can occur while accessing a file: the adversary can trick the system by replacing the original file with their version and cause the system to read the malicious file.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-362](/wiki/p/weakness/CWE-362), [CWE-363](/wiki/p/weakness/CWE-363), [CWE-366](/wiki/p/weakness/CWE-366), [CWE-368](/wiki/p/weakness/CWE-368), [CWE-370](/wiki/p/weakness/CWE-370), [CWE-662](/wiki/p/weakness/CWE-662), [CWE-665](/wiki/p/weakness/CWE-665), [CWE-667](/wiki/p/weakness/CWE-667), [CWE-689](/wiki/p/weakness/CWE-689), [CWE-1223](/wiki/p/weakness/CWE-1223), [CWE-1254](/wiki/p/weakness/CWE-1254), [CWE-1298](/wiki/p/weakness/CWE-1298)

## Prerequisites

- A resource is accessed/modified concurrently by multiple processes such that a race condition exists.
- The adversary has the ability to modify the resource.

## Skills required

- Medium: Being able to "run the race" requires basic knowledge of concurrent processing including synchonization techniques.

## Consequences

- Confidentiality, Access Control, Authorization: Gain Privileges
- Integrity: Modify Data

## Mitigations

- Use safe libraries to access resources such as files.
- Be aware that improper use of access function calls such as chown(), tempfile(), chmod(), etc. can cause a race condition.
- Use synchronization to control the flow of execution.
- Use static analysis tools to find race conditions.
- Pay attention to concurrency problems related to the access of resources.

## Source

- [MITRE CAPEC CAPEC-26](https://capec.mitre.org/data/definitions/26.html)
