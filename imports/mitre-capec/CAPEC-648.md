---
slug: attack-pattern/CAPEC-648
title: "CAPEC-648 — Collect Data from Screen Capture"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-648]
cwe_ids: [CWE-267]
mitre_ids: [T1113, T1513]
related: [weakness/CWE-267, technique/T1113]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-648
updated_at: 2026-08-31
summary: "An adversary gathers sensitive information by exploiting the system's screen capture functionality. Through screenshots, the adversary aims to see what happens on the screen over the course of an operation. The adversary can leverage information gathered in order to carry out fur…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/648.html
---

# CAPEC-648: Collect Data from Screen Capture

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary gathers sensitive information by exploiting the system's screen capture functionality. Through screenshots, the adversary aims to see what happens on the screen over the course of an operation. The adversary can leverage information gathered in order to carry out further attacks.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-267](/wiki/p/weakness/CWE-267)

**ATT&CK techniques:** [T1113](/wiki/p/technique/T1113), [T1513](/wiki/p/technique/T1513)

## Prerequisites

- The adversary must have obtained logical access to the system by some means (e.g., via obtained credentials or planting malware on the system).

## Skills required

- Low: Once the adversary has logical access (which can potentially require high knowledge and skill level), the adversary needs only to leverage the relevant command for screen capture.

## Consequences

- Confidentiality: Read Data

## Mitigations

- Identify potentially malicious software that may have functionality to acquire screen captures, and audit and/or block it by using allowlist tools.
- While screen capture is a legitimate and practical function, certain situations and context may require the disabling of this feature.

## Mappings that no longer resolve

CAPEC 3.9 (2023-01-24) maps this pattern to `T1513`, which the current ATT&CK corpus does not carry — MITRE has revoked or relocated them since CAPEC was last published. The mapping is recorded here rather than dropped, because a stale cross-reference is a fact about the taxonomies, not a gap in this page.

## Source

- [MITRE CAPEC CAPEC-648](https://capec.mitre.org/data/definitions/648.html)
