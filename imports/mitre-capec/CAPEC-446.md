---
slug: attack-pattern/CAPEC-446
title: "CAPEC-446 — Malicious Logic Insertion into Product via Inclusion of Third-Party Component"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-446]
mitre_ids: [T1195]
related: [technique/T1195]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-446
updated_at: 2026-08-31
summary: "An adversary conducts supply chain attacks by the inclusion of insecure third-party components into a technology, product, or code-base, possibly packaging a malicious driver or component along with the product before shipping it to the consumer or acquirer."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/446.html
---

# CAPEC-446: Malicious Logic Insertion into Product via Inclusion of Third-Party Component

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | High |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary conducts supply chain attacks by the inclusion of insecure third-party components into a technology, product, or code-base, possibly packaging a malicious driver or component along with the product before shipping it to the consumer or acquirer.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**ATT&CK techniques:** [T1195](/wiki/p/technique/T1195)

## Prerequisites

- Access to the product during the initial or continuous development. This access is often obtained via insider access to include the third-party component after deployment.

## Consequences

- Authorization: Execute Unauthorized Commands

## Mitigations

- Assess software and hardware during development and prior to deployment to ensure that it functions as intended and without any malicious functionality. This includes both initial development, as well as updates propagated to the product after deployment.
- Don't assume popular third-party components are free from malware or vulnerabilities. For software, assess for malicious functionality via update/commit reviews or automated static/dynamic analysis prior to including the component within the application and deploying in a production environment.

## Source

- [MITRE CAPEC CAPEC-446](https://capec.mitre.org/data/definitions/446.html)
