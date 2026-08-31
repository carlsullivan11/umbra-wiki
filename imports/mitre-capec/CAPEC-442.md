---
slug: attack-pattern/CAPEC-442
title: "CAPEC-442 — Infected Software"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-442]
cwe_ids: [CWE-506]
mitre_ids: [T1195.001, T1195.002]
related: [weakness/CWE-506, technique/T1195.001, technique/T1195.002]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-442
updated_at: 2026-08-31
summary: "An adversary adds malicious logic, often in the form of a computer virus, to otherwise benign software. This logic is often hidden from the user of the software and works behind the scenes to achieve negative impacts. Many times, the malicious logic is inserted into empty space b…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/442.html
---

# CAPEC-442: Infected Software

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | High |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary adds malicious logic, often in the form of a computer virus, to otherwise benign software. This logic is often hidden from the user of the software and works behind the scenes to achieve negative impacts. Many times, the malicious logic is inserted into empty space between legitimate code, and is then called when the software is executed. This pattern of attack focuses on software already fielded and used in operation as opposed to software that is still under development and part of the supply chain.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-506](/wiki/p/weakness/CWE-506)

**ATT&CK techniques:** [T1195.001](/wiki/p/technique/T1195.001), [T1195.002](/wiki/p/technique/T1195.002)

## Prerequisites

- Access to the software currently deployed at a victim location. This access is often obtained by leveraging another attack pattern to gain permissions that the adversary wouldn't normally have.

## Consequences

- Authorization: Execute Unauthorized Commands

## Mitigations

- Leverage anti-virus products to detect and quarantine software with known virus.

## Source

- [MITRE CAPEC CAPEC-442](https://capec.mitre.org/data/definitions/442.html)
