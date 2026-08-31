---
slug: attack-pattern/CAPEC-529
title: "CAPEC-529 — Malware-Directed Internal Reconnaissance"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-529]
related: []
provenance: imported
import_source: mitre-capec
import_id: CAPEC-529
updated_at: 2026-08-31
summary: "Adversary uses malware or a similarly controlled application installed inside an organizational perimeter to gather information about the composition, configuration, and security mechanisms of a targeted application, system or network."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/529.html
---

# CAPEC-529: Malware-Directed Internal Reconnaissance

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Medium |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

Adversary uses malware or a similarly controlled application installed inside an organizational perimeter to gather information about the composition, configuration, and security mechanisms of a targeted application, system or network.

## Prerequisites

- The adversary must have internal, logical access to the target network and system.

## Skills required

- Medium: The adversary must be able to obtain or develop, as well as place malicious software inside the target network/system.

## Consequences

- Confidentiality: Read Data

## Mitigations

- Keep patches up to date by installing weekly or daily if possible.
- Identify programs that may be used to acquire peripheral information and block them by using a software restriction policy or tools that restrict program execution by using a process allowlist.

## Source

- [MITRE CAPEC CAPEC-529](https://capec.mitre.org/data/definitions/529.html)
