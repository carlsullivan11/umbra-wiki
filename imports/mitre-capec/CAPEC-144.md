---
slug: attack-pattern/CAPEC-144
title: "CAPEC-144 — Detect Unpublicized Web Services"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-144]
cwe_ids: [CWE-425]
related: [weakness/CWE-425]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-144
updated_at: 2026-08-31
summary: "An adversary searches a targeted web site for web services that have not been publicized. This attack can be especially dangerous since unpublished but available services may not have adequate security controls placed upon them given that an administrator may believe they are unr…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/144.html
---

# CAPEC-144: Detect Unpublicized Web Services

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Low |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary searches a targeted web site for web services that have not been publicized. This attack can be especially dangerous since unpublished but available services may not have adequate security controls placed upon them given that an administrator may believe they are unreachable.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-425](/wiki/p/weakness/CWE-425)

## Prerequisites

- The targeted web site must include unpublished services within its web tree. The nature of these services determines the severity of this attack.

## Source

- [MITRE CAPEC CAPEC-144](https://capec.mitre.org/data/definitions/144.html)
