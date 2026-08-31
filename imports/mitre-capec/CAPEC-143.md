---
slug: attack-pattern/CAPEC-143
title: "CAPEC-143 — Detect Unpublicized Web Pages"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-143]
cwe_ids: [CWE-425]
related: [weakness/CWE-425]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-143
updated_at: 2026-08-31
summary: "An adversary searches a targeted web site for web pages that have not been publicized. In doing this, the adversary may be able to gain access to information that the targeted site did not intend to make public."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/143.html
---

# CAPEC-143: Detect Unpublicized Web Pages

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Low |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary searches a targeted web site for web pages that have not been publicized. In doing this, the adversary may be able to gain access to information that the targeted site did not intend to make public.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-425](/wiki/p/weakness/CWE-425)

## Prerequisites

- The targeted web site must include pages within its published tree that are not connected to its tree of links. The sensitivity of the content of these pages determines the severity of this attack.

## Source

- [MITRE CAPEC CAPEC-143](https://capec.mitre.org/data/definitions/143.html)
