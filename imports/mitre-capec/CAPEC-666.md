---
slug: attack-pattern/CAPEC-666
title: "CAPEC-666 — BlueSmacking"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-666]
cwe_ids: [CWE-404]
mitre_ids: [T1498.001, T1499.001]
related: [weakness/CWE-404, technique/T1498.001, technique/T1499.001]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-666
updated_at: 2026-08-31
summary: "An adversary uses Bluetooth flooding to transfer large packets to Bluetooth enabled devices over the L2CAP protocol with the goal of creating a DoS. This attack must be carried out within close proximity to a Bluetooth enabled device."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/666.html
---

# CAPEC-666: BlueSmacking

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary uses Bluetooth flooding to transfer large packets to Bluetooth enabled devices over the L2CAP protocol with the goal of creating a DoS. This attack must be carried out within close proximity to a Bluetooth enabled device.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-404](/wiki/p/weakness/CWE-404)

**ATT&CK techniques:** [T1498.001](/wiki/p/technique/T1498.001), [T1499.001](/wiki/p/technique/T1499.001)

## Prerequisites

- The system/application has Bluetooth enabled.

## Skills required

- Low: An adversary only needs a Linux machine along with a Bluetooth adapter, which is extremely common.

## Consequences

- Availability: Unreliable Execution, Resource Consumption

## Mitigations

- Disable Bluetooth when not being used.
- When using Bluetooth, set it to hidden or non-discoverable mode.

## Source

- [MITRE CAPEC CAPEC-666](https://capec.mitre.org/data/definitions/666.html)
