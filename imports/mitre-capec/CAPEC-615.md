---
slug: attack-pattern/CAPEC-615
title: "CAPEC-615 — Evil Twin Wi-Fi Attack"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-615]
cwe_ids: [CWE-300]
related: [weakness/CWE-300]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-615
updated_at: 2026-08-31
summary: "Adversaries install Wi-Fi equipment that acts as a legitimate Wi-Fi network access point. When a device connects to this access point, Wi-Fi data traffic is intercepted, captured, and analyzed. This also allows the adversary to use 'adversary-in-the-middle' (CAPEC-94) for all com…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/615.html
---

# CAPEC-615: Evil Twin Wi-Fi Attack

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Low |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

Adversaries install Wi-Fi equipment that acts as a legitimate Wi-Fi network access point. When a device connects to this access point, Wi-Fi data traffic is intercepted, captured, and analyzed. This also allows the adversary to use "adversary-in-the-middle" (CAPEC-94) for all communications.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-300](/wiki/p/weakness/CWE-300)

## Prerequisites

- None

## Consequences

- Confidentiality: Read Data

## Mitigations

- Commercial defensive technology that monitors for rogue Wi-Fi access points, adversary-in-the-middle attacks, and anomalous activity with the mobile device baseband radios.

## Source

- [MITRE CAPEC CAPEC-615](https://capec.mitre.org/data/definitions/615.html)
