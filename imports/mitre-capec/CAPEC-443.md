---
slug: attack-pattern/CAPEC-443
title: "CAPEC-443 — Malicious Logic Inserted Into Product by Authorized Developer"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-443]
mitre_ids: [T1195.002, T1195.003]
related: [technique/T1195.002, technique/T1195.003]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-443
updated_at: 2026-08-31
summary: "An adversary uses their privileged position within an authorized development organization to inject malicious logic into a codebase or product."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/443.html
---

# CAPEC-443: Malicious Logic Inserted Into Product by Authorized Developer

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | High |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary uses their privileged position within an authorized development organization to inject malicious logic into a codebase or product.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**ATT&CK techniques:** [T1195.002](/wiki/p/technique/T1195.002), [T1195.003](/wiki/p/technique/T1195.003)

## Prerequisites

- Access to the product during the initial or continuous development.

## Consequences

- Authorization: Execute Unauthorized Commands

## Mitigations

- Assess software and hardware during development and prior to deployment to ensure that it functions as intended and without any malicious functionality. This includes both initial development, as well as updates propagated to the product after deployment.

## Source

- [MITRE CAPEC CAPEC-443](https://capec.mitre.org/data/definitions/443.html)
