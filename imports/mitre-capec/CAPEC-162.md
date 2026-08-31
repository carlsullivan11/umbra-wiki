---
slug: attack-pattern/CAPEC-162
title: "CAPEC-162 — Manipulating Hidden Fields"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-162]
cwe_ids: [CWE-602]
related: [weakness/CWE-602]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-162
updated_at: 2026-08-31
summary: "An adversary exploits a weakness in the server's trust of client-side processing by modifying data on the client-side, such as price information, and then submitting this data to the server, which processes the modified data. For example, eShoplifting is a data manipulation attac…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/162.html
---

# CAPEC-162: Manipulating Hidden Fields

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary exploits a weakness in the server's trust of client-side processing by modifying data on the client-side, such as price information, and then submitting this data to the server, which processes the modified data. For example, eShoplifting is a data manipulation attack against an on-line merchant during a purchasing transaction. The manipulation of price, discount or quantity fields in the transaction message allows the adversary to acquire items at a lower cost than the merchant intended. The adversary performs a normal purchasing transaction but edits hidden fields within the HTML form response that store price or other information to give themselves a better deal. The merchant then uses the modified pricing information in calculating the cost of the selected items.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-602](/wiki/p/weakness/CWE-602)

## Prerequisites

- The targeted site must contain hidden fields to be modified.
- The targeted site must not validate the hidden fields with backend processing.

## Source

- [MITRE CAPEC CAPEC-162](https://capec.mitre.org/data/definitions/162.html)
