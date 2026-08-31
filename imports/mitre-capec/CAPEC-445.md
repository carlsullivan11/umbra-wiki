---
slug: attack-pattern/CAPEC-445
title: "CAPEC-445 — Malicious Logic Insertion into Product Software via Configuration Management Manipulation"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-445]
mitre_ids: [T1195.001]
related: [technique/T1195.001]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-445
updated_at: 2026-08-31
summary: "An adversary exploits a configuration management system so that malicious logic is inserted into a software products build, update or deployed environment. If an adversary can control the elements included in a product's configuration management for build they can potentially rep…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/445.html
---

# CAPEC-445: Malicious Logic Insertion into Product Software via Configuration Management Manipulation

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | High |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary exploits a configuration management system so that malicious logic is inserted into a software products build, update or deployed environment. If an adversary can control the elements included in a product's configuration management for build they can potentially replace, modify or insert code files containing malicious logic. If an adversary can control elements of a product's ongoing operational configuration management baseline they can potentially force clients receiving updates from the system to install insecure software when receiving updates from the server.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**ATT&CK techniques:** [T1195.001](/wiki/p/technique/T1195.001)

## Prerequisites

- Access to the configuration management system during deployment or currently deployed at a victim location. This access is often obtained via insider access or by leveraging another attack pattern to gain permissions that the adversary wouldn't normally have.

## Consequences

- Authorization: Execute Unauthorized Commands

## Mitigations

- Assess software during development and prior to deployment to ensure that it functions as intended and without any malicious functionality.
- Leverage anti-virus products to detect and quarantine software with known virus.

## Source

- [MITRE CAPEC CAPEC-445](https://capec.mitre.org/data/definitions/445.html)
