---
slug: attack-pattern/CAPEC-186
title: "CAPEC-186 — Malicious Software Update"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-186]
cwe_ids: [CWE-494]
mitre_ids: [T1195.002]
related: [weakness/CWE-494, technique/T1195.002]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-186
updated_at: 2026-08-31
summary: "An adversary uses deceptive methods to cause a user or an automated process to download and install dangerous code believed to be a valid update that originates from an adversary controlled source."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/186.html
---

# CAPEC-186: Malicious Software Update

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary uses deceptive methods to cause a user or an automated process to download and install dangerous code believed to be a valid update that originates from an adversary controlled source.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-494](/wiki/p/weakness/CWE-494)

**ATT&CK techniques:** [T1195.002](/wiki/p/technique/T1195.002)

## Skills required

- High: This attack requires advanced cyber capabilities

## Consequences

- Access Control, Availability, Confidentiality: Execute Unauthorized Commands

## Mitigations

- Validate software updates before installing.

## Source

- [MITRE CAPEC CAPEC-186](https://capec.mitre.org/data/definitions/186.html)
