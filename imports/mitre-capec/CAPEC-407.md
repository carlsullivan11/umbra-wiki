---
slug: attack-pattern/CAPEC-407
title: "CAPEC-407 — Pretexting"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-407]
mitre_ids: [T1589]
related: [technique/T1589]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-407
updated_at: 2026-08-31
summary: "An adversary engages in pretexting behavior to solicit information from target persons, or manipulate the target into performing some action that serves the adversary's interests. During a pretexting attack, the adversary creates an invented scenario, assuming an identity or role…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/407.html
---

# CAPEC-407: Pretexting

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Low |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary engages in pretexting behavior to solicit information from target persons, or manipulate the target into performing some action that serves the adversary's interests. During a pretexting attack, the adversary creates an invented scenario, assuming an identity or role to persuade a targeted victim to release information or perform some action. It is more than just creating a lie; in some cases it can be creating a whole new identity and then using that identity to manipulate the receipt of information.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**ATT&CK techniques:** [T1589](/wiki/p/technique/T1589)

## Prerequisites

- The adversary must have the means and knowledge of how to communicate with the target in some manner.The adversary must have knowledge of the pretext that would influence the actions of the specific target.

## Skills required

- Low: The adversary requires strong inter-personal and communication skills.

## Consequences

- Confidentiality: Other

## Mitigations

- An organization should provide regular, robust cybersecurity training to its employees to prevent successful social engineering attacks.

## Source

- [MITRE CAPEC CAPEC-407](https://capec.mitre.org/data/definitions/407.html)
