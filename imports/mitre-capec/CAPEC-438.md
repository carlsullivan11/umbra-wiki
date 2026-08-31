---
slug: attack-pattern/CAPEC-438
title: "CAPEC-438 — Modification During Manufacture"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-438]
mitre_ids: [T1195]
related: [technique/T1195]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-438
updated_at: 2026-08-31
summary: "An attacker modifies a technology, product, or component during a stage in its manufacture for the purpose of carrying out an attack against some entity involved in the supply chain lifecycle. There are an almost limitless number of ways an attacker can modify a technology when t…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/438.html
---

# CAPEC-438: Modification During Manufacture

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | — |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker modifies a technology, product, or component during a stage in its manufacture for the purpose of carrying out an attack against some entity involved in the supply chain lifecycle. There are an almost limitless number of ways an attacker can modify a technology when they are involved in its manufacture, as the attacker has potential inroads to the software composition, hardware design and assembly, firmware, or basic design mechanics. Additionally, manufacturing of key components is often outsourced with the final product assembled by the primary manufacturer. The greatest risk, however, is deliberate manipulation of design specifications to produce malicious hardware or devices. There are billions of transistors in a single integrated circuit and studies have shown that fewer than 10 transistors are required to create malicious functionality.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**ATT&CK techniques:** [T1195](/wiki/p/technique/T1195)

## Source

- [MITRE CAPEC CAPEC-438](https://capec.mitre.org/data/definitions/438.html)
