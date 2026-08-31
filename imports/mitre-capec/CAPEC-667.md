---
slug: attack-pattern/CAPEC-667
title: "CAPEC-667 — Bluetooth Impersonation AttackS (BIAS)"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-667]
cwe_ids: [CWE-290]
related: [weakness/CWE-290]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-667
updated_at: 2026-08-31
summary: "An adversary disguises the MAC address of their Bluetooth enabled device to one for which there exists an active and trusted connection and authenticates successfully. The adversary can then perform malicious actions on the target Bluetooth device depending on the target’s capabi…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/667.html
---

# CAPEC-667: Bluetooth Impersonation AttackS (BIAS)

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary disguises the MAC address of their Bluetooth enabled device to one for which there exists an active and trusted connection and authenticates successfully. The adversary can then perform malicious actions on the target Bluetooth device depending on the target’s capabilities.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-290](/wiki/p/weakness/CWE-290)

## Prerequisites

- Knowledge of a target device's list of trusted connections.

## Skills required

- Low: Adversaries must be capable of using command line Linux tools.
- Low: Adversaries must be in close proximity to Bluetooth devices.

## Consequences

- Integrity: —
- Confidentiality: —

## Mitigations

- Disable Bluetooth in public places.
- Verify incoming Bluetooth connections; do not automatically trust.
- Change default PIN passwords and always use one when connecting.

## Source

- [MITRE CAPEC CAPEC-667](https://capec.mitre.org/data/definitions/667.html)
