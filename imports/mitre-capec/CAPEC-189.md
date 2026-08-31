---
slug: attack-pattern/CAPEC-189
title: "CAPEC-189 — Black Box Reverse Engineering"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-189]
cwe_ids: [CWE-203, CWE-1255, CWE-1300]
related: [weakness/CWE-203, weakness/CWE-1255, weakness/CWE-1300]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-189
updated_at: 2026-08-31
summary: "An adversary discovers the structure, function, and composition of a type of computer software through black box analysis techniques. 'Black Box' methods involve interacting with the software indirectly, in the absence of direct access to the executable object. Such analysis typi…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/189.html
---

# CAPEC-189: Black Box Reverse Engineering

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Low |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary discovers the structure, function, and composition of a type of computer software through black box analysis techniques. 'Black Box' methods involve interacting with the software indirectly, in the absence of direct access to the executable object. Such analysis typically involves interacting with the software at the boundaries of where the software interfaces with a larger execution environment, such as input-output vectors, libraries, or APIs. Black Box Reverse Engineering also refers to gathering physical side effects of a hardware device, such as electromagnetic radiation or sounds.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-203](/wiki/p/weakness/CWE-203), [CWE-1255](/wiki/p/weakness/CWE-1255), [CWE-1300](/wiki/p/weakness/CWE-1300)

## Source

- [MITRE CAPEC CAPEC-189](https://capec.mitre.org/data/definitions/189.html)
