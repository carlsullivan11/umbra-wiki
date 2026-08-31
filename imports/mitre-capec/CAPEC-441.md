---
slug: attack-pattern/CAPEC-441
title: "CAPEC-441 — Malicious Logic Insertion"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-441]
cwe_ids: [CWE-284]
related: [weakness/CWE-284]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-441
updated_at: 2026-08-31
summary: "An adversary installs or adds malicious logic (also known as malware) into a seemingly benign component of a fielded system. This logic is often hidden from the user of the system and works behind the scenes to achieve negative impacts. With the proliferation of mass digital stor…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/441.html
---

# CAPEC-441: Malicious Logic Insertion

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | High |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary installs or adds malicious logic (also known as malware) into a seemingly benign component of a fielded system. This logic is often hidden from the user of the system and works behind the scenes to achieve negative impacts. With the proliferation of mass digital storage and inexpensive multimedia devices, Bluetooth and 802.11 support, new attack vectors for spreading malware are emerging for things we once thought of as innocuous greeting cards, picture frames, or digital projectors. This pattern of attack focuses on systems already fielded and used in operation as opposed to systems and their components that are still under development and part of the supply chain.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-284](/wiki/p/weakness/CWE-284)

## Prerequisites

- Access to the component currently deployed at a victim location.

## Consequences

- Authorization: Execute Unauthorized Commands

## Source

- [MITRE CAPEC CAPEC-441](https://capec.mitre.org/data/definitions/441.html)
