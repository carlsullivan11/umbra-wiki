---
slug: attack-pattern/CAPEC-131
title: "CAPEC-131 — Resource Leak Exposure"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-131]
cwe_ids: [CWE-404]
mitre_ids: [T1499]
related: [weakness/CWE-404, technique/T1499]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-131
updated_at: 2026-08-31
summary: "An adversary utilizes a resource leak on the target to deplete the quantity of the resource available to service legitimate requests."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/131.html
---

# CAPEC-131: Resource Leak Exposure

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Medium |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary utilizes a resource leak on the target to deplete the quantity of the resource available to service legitimate requests.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-404](/wiki/p/weakness/CWE-404)

**ATT&CK techniques:** [T1499](/wiki/p/technique/T1499)

## Prerequisites

- The target must have a resource leak that the adversary can repeatedly trigger.

## Consequences

- Availability: Unreliable Execution, Resource Consumption

## Mitigations

- If possible, leverage coding language(s) that do not allow this weakness to occur (e.g., Java, Ruby, and Python all perform automatic garbage collection that releases memory for objects that have been deallocated).
- Memory should always be allocated/freed using matching functions (e.g., malloc/free, new/delete, etc.)
- Implement best practices with respect to memory management, including the freeing of all allocated resources at all exit points and ensuring consistency with how and where memory is freed in a function.

## Source

- [MITRE CAPEC CAPEC-131](https://capec.mitre.org/data/definitions/131.html)
