---
slug: attack-pattern/CAPEC-619
title: "CAPEC-619 — Signal Strength Tracking"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-619]
cwe_ids: [CWE-201]
related: [weakness/CWE-201]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-619
updated_at: 2026-08-31
summary: "In this attack scenario, the attacker passively monitors the signal strength of the target’s cellular RF signal or WiFi RF signal and uses the strength of the signal (with directional antennas and/or from multiple listening points at once) to identify the source location of the s…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/619.html
---

# CAPEC-619: Signal Strength Tracking

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Low |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

In this attack scenario, the attacker passively monitors the signal strength of the target’s cellular RF signal or WiFi RF signal and uses the strength of the signal (with directional antennas and/or from multiple listening points at once) to identify the source location of the signal. Obtaining the signal of the target can be accomplished through multiple techniques such as through Cellular Broadcast Message Request or through the use of IMSI Tracking or WiFi MAC Address Tracking.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-201](/wiki/p/weakness/CWE-201)

## Skills required

- Low: Commercial tools are available.

## Source

- [MITRE CAPEC CAPEC-619](https://capec.mitre.org/data/definitions/619.html)
