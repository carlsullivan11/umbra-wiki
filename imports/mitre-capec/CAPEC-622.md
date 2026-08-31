---
slug: attack-pattern/CAPEC-622
title: "CAPEC-622 — Electromagnetic Side-Channel Attack"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-622]
cwe_ids: [CWE-201]
related: [weakness/CWE-201]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-622
updated_at: 2026-08-31
summary: "In this attack scenario, the attacker passively monitors electromagnetic emanations that are produced by the targeted electronic device as an unintentional side-effect of its processing. From these emanations, the attacker derives information about the data that is being processe…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/622.html
---

# CAPEC-622: Electromagnetic Side-Channel Attack

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Low |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

In this attack scenario, the attacker passively monitors electromagnetic emanations that are produced by the targeted electronic device as an unintentional side-effect of its processing. From these emanations, the attacker derives information about the data that is being processed (e.g. the attacker can recover cryptographic keys by monitoring emanations associated with cryptographic processing). This style of attack requires proximal access to the device, however attacks have been demonstrated at public conferences that work at distances of up to 10-15 feet. There have not been any significant studies to determine the maximum practical distance for such attacks. Since the attack is passive, it is nearly impossible to detect and the targeted device will continue to operate as normal after a successful attack.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-201](/wiki/p/weakness/CWE-201)

## Prerequisites

- Proximal access to the device.

## Skills required

- Medium: Sophisticated attack, but detailed techniques published in the open literature.

## Consequences

- Confidentiality: Read Data

## Mitigations

- Utilize side-channel resistant implementations of all crypto algorithms.
- Strong physical security of all devices that contain secret key information. (even when devices are not in use)

## Source

- [MITRE CAPEC CAPEC-622](https://capec.mitre.org/data/definitions/622.html)
