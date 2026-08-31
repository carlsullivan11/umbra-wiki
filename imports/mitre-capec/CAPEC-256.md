---
slug: attack-pattern/CAPEC-256
title: "CAPEC-256 — SOAP Array Overflow"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-256]
cwe_ids: [CWE-805]
related: [weakness/CWE-805]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-256
updated_at: 2026-08-31
summary: "An attacker sends a SOAP request with an array whose actual length exceeds the length indicated in the request. If the server processing the transmission naively trusts the specified size, then an attacker can intentionally understate the size of the array, possibly resulting in …"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/256.html
---

# CAPEC-256: SOAP Array Overflow

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker sends a SOAP request with an array whose actual length exceeds the length indicated in the request. If the server processing the transmission naively trusts the specified size, then an attacker can intentionally understate the size of the array, possibly resulting in a buffer overflow if the server attempts to read the entire data set into the memory it allocated for a smaller array.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-805](/wiki/p/weakness/CWE-805)

## Prerequisites

- The targeted SOAP server must trust that the array size as stated in messages it receives is correct, but read through the entire content of the message regardless of the stated size of the array.

## Mitigations

- If the server either verifies the correctness of the stated array size or if the server stops processing an array once the stated number of elements have been read, regardless of the actual array size, then this attack will fail. The former detects the malformed SOAP message while the latter ensures that the server does not attempt to load more data than was allocated for.

## Source

- [MITRE CAPEC CAPEC-256](https://capec.mitre.org/data/definitions/256.html)
