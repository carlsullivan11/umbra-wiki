---
slug: attack-pattern/CAPEC-313
title: "CAPEC-313 — Passive OS Fingerprinting"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-313]
cwe_ids: [CWE-200]
mitre_ids: [T1082]
related: [weakness/CWE-200, technique/T1082]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-313
updated_at: 2026-08-31
summary: "An adversary engages in activity to detect the version or type of OS software in a an environment by passively monitoring communication between devices, nodes, or applications. Passive techniques for operating system detection send no actual probes to a target, but monitor networ…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/313.html
---

# CAPEC-313: Passive OS Fingerprinting

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Low |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary engages in activity to detect the version or type of OS software in a an environment by passively monitoring communication between devices, nodes, or applications. Passive techniques for operating system detection send no actual probes to a target, but monitor network or client-server communication between nodes in order to identify operating systems based on observed behavior as compared to a database of known signatures or values. While passive OS fingerprinting is not usually as reliable as active methods, it is generally better able to evade detection.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-200](/wiki/p/weakness/CWE-200)

**ATT&CK techniques:** [T1082](/wiki/p/technique/T1082)

## Prerequisites

- The ability to monitor network communications.Access to at least one host, and the privileges to interface with the network interface card.

## Consequences

- Confidentiality: Read Data
- Confidentiality, Access Control, Authorization: Hide Activities

## Source

- [MITRE CAPEC CAPEC-313](https://capec.mitre.org/data/definitions/313.html)
