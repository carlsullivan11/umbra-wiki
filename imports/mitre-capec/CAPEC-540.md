---
slug: attack-pattern/CAPEC-540
title: "CAPEC-540 — Overread Buffers"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-540]
cwe_ids: [CWE-125]
related: [weakness/CWE-125]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-540
updated_at: 2026-08-31
summary: "An adversary attacks a target by providing input that causes an application to read beyond the boundary of a defined buffer. This typically occurs when a value influencing where to start or stop reading is set to reflect positions outside of the valid memory location of the buffe…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/540.html
---

# CAPEC-540: Overread Buffers

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary attacks a target by providing input that causes an application to read beyond the boundary of a defined buffer. This typically occurs when a value influencing where to start or stop reading is set to reflect positions outside of the valid memory location of the buffer. This type of attack may result in exposure of sensitive information, a system crash, or arbitrary code execution.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-125](/wiki/p/weakness/CWE-125)

## Prerequisites

- For this type of attack to be successful, a few prerequisites must be met. First, the targeted software must be written in a language that enables fine grained buffer control. (e.g., c, c++) Second, the targeted software must actually perform buffer operations and inadequately perform bounds-checking on those buffer operations. Finally, the adversary must have the capability to influence the input that guides these buffer operations.

## Consequences

- Confidentiality: Read Data
- Availability: Unreliable Execution

## Source

- [MITRE CAPEC CAPEC-540](https://capec.mitre.org/data/definitions/540.html)
