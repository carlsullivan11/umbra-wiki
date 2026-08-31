---
slug: attack-pattern/CAPEC-623
title: "CAPEC-623 — Compromising Emanations Attack"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-623]
cwe_ids: [CWE-201]
related: [weakness/CWE-201]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-623
updated_at: 2026-08-31
summary: "Compromising Emanations (CE) are defined as unintentional signals which an attacker may intercept and analyze to disclose the information processed by the targeted equipment. Commercial mobile devices and retransmission devices have displays, buttons, microchips, and radios that …"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/623.html
---

# CAPEC-623: Compromising Emanations Attack

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Low |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

Compromising Emanations (CE) are defined as unintentional signals which an attacker may intercept and analyze to disclose the information processed by the targeted equipment. Commercial mobile devices and retransmission devices have displays, buttons, microchips, and radios that emit mechanical emissions in the form of sound or vibrations. Capturing these emissions can help an adversary understand what the device is doing.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-201](/wiki/p/weakness/CWE-201)

## Prerequisites

- Proximal access to the device.

## Skills required

- High: Sophisticated attack.

## Consequences

- Confidentiality: Read Data

## Mitigations

- None are known.

## Source

- [MITRE CAPEC CAPEC-623](https://capec.mitre.org/data/definitions/623.html)
