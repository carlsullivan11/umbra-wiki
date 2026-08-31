---
slug: attack-pattern/CAPEC-542
title: "CAPEC-542 — Targeted Malware"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-542]
mitre_ids: [T1027, T1587.001]
related: [technique/T1027, technique/T1587.001]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-542
updated_at: 2026-08-31
summary: "An adversary develops targeted malware that takes advantage of a known vulnerability in an organizational information technology environment. The malware crafted for these attacks is based specifically on information gathered about the technology environment. Successfully executi…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/542.html
---

# CAPEC-542: Targeted Malware

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | — |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary develops targeted malware that takes advantage of a known vulnerability in an organizational information technology environment. The malware crafted for these attacks is based specifically on information gathered about the technology environment. Successfully executing the malware enables an adversary to achieve a wide variety of negative technical impacts.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**ATT&CK techniques:** [T1027](/wiki/p/technique/T1027), [T1587.001](/wiki/p/technique/T1587.001)

## Source

- [MITRE CAPEC CAPEC-542](https://capec.mitre.org/data/definitions/542.html)
