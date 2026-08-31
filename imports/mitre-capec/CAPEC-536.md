---
slug: attack-pattern/CAPEC-536
title: "CAPEC-536 — Data Injected During Configuration"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-536]
cwe_ids: [CWE-284]
related: [weakness/CWE-284]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-536
updated_at: 2026-08-31
summary: "An attacker with access to data files and processes on a victim's system injects malicious data into critical operational data during configuration or recalibration, causing the victim's system to perform in a suboptimal manner that benefits the adversary."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/536.html
---

# CAPEC-536: Data Injected During Configuration

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | High |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker with access to data files and processes on a victim's system injects malicious data into critical operational data during configuration or recalibration, causing the victim's system to perform in a suboptimal manner that benefits the adversary.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-284](/wiki/p/weakness/CWE-284)

## Prerequisites

- The attacker must have previously compromised the victim's systems or have physical access to the victim's systems.
- Advanced knowledge of software and hardware capabilities of a manufacturer's product.

## Skills required

- High: Ability to generate and inject false data into operational data into a system with the intent of causing the victim to alter the configuration of the system.

## Mitigations

- Ensure that proper access control is implemented on all systems to prevent unauthorized access to system files and processes.

## Source

- [MITRE CAPEC CAPEC-536](https://capec.mitre.org/data/definitions/536.html)
