---
slug: attack-pattern/CAPEC-668
title: "CAPEC-668 — Key Negotiation of Bluetooth Attack (KNOB)"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-668]
cwe_ids: [CWE-285, CWE-425, CWE-693]
mitre_ids: [T1565.002]
related: [weakness/CWE-285, weakness/CWE-425, weakness/CWE-693, technique/T1565.002]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-668
updated_at: 2026-08-31
summary: "An adversary can exploit a flaw in Bluetooth key negotiation allowing them to decrypt information sent between two devices communicating via Bluetooth. The adversary uses an Adversary in the Middle setup to modify packets sent between the two devices during the authentication pro…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/668.html
---

# CAPEC-668: Key Negotiation of Bluetooth Attack (KNOB)

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary can exploit a flaw in Bluetooth key negotiation allowing them to decrypt information sent between two devices communicating via Bluetooth. The adversary uses an Adversary in the Middle setup to modify packets sent between the two devices during the authentication process, specifically the entropy bits. Knowledge of the number of entropy bits will allow the attacker to easily decrypt information passing over the line of communication.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-285](/wiki/p/weakness/CWE-285), [CWE-425](/wiki/p/weakness/CWE-425), [CWE-693](/wiki/p/weakness/CWE-693)

**ATT&CK techniques:** [T1565.002](/wiki/p/technique/T1565.002)

## Prerequisites

- Person in the Middle network setup.

## Skills required

- Medium: Ability to modify packets.

## Consequences

- Confidentiality: Read Data
- Confidentiality, Access Control, Authorization: Bypass Protection Mechanism
- Integrity: Modify Data

## Mitigations

- Newer Bluetooth firmwares ensure that the KNOB is not negotaited in plaintext. Update your device.

## Source

- [MITRE CAPEC CAPEC-668](https://capec.mitre.org/data/definitions/668.html)
