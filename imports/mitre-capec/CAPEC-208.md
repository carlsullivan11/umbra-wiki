---
slug: attack-pattern/CAPEC-208
title: "CAPEC-208 — Removing/short-circuiting 'Purse' logic: removing/mutating 'cash' decrements"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-208]
cwe_ids: [CWE-602]
related: [weakness/CWE-602]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-208
updated_at: 2026-08-31
summary: "An attacker removes or modifies the logic on a client associated with monetary calculations resulting in incorrect information being sent to the server. A server may rely on a client to correctly compute monetary information. For example, a server might supply a price for an item…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/208.html
---

# CAPEC-208: Removing/short-circuiting 'Purse' logic: removing/mutating 'cash' decrements

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker removes or modifies the logic on a client associated with monetary calculations resulting in incorrect information being sent to the server. A server may rely on a client to correctly compute monetary information. For example, a server might supply a price for an item and then rely on the client to correctly compute the total cost of a purchase given the number of items the user is buying. If the attacker can remove or modify the logic that controls these calculations, they can return incorrect values to the server. The attacker can use this to make purchases for a fraction of the legitimate cost or otherwise avoid correct billing for activities.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-602](/wiki/p/weakness/CWE-602)

## Prerequisites

- The targeted server must rely on the client to correctly perform monetary calculations and must fail to detect errors in these calculations.

## Source

- [MITRE CAPEC CAPEC-208](https://capec.mitre.org/data/definitions/208.html)
