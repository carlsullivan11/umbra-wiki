---
slug: attack-pattern/CAPEC-151
title: "CAPEC-151 — Identity Spoofing"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-151]
cwe_ids: [CWE-287]
related: [weakness/CWE-287]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-151
updated_at: 2026-08-31
summary: "Identity Spoofing refers to the action of assuming (i.e., taking on) the identity of some other entity (human or non-human) and then using that identity to accomplish a goal. An adversary may craft messages that appear to come from a different principle or use stolen / spoofed au…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/151.html
---

# CAPEC-151: Identity Spoofing

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Medium |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

Identity Spoofing refers to the action of assuming (i.e., taking on) the identity of some other entity (human or non-human) and then using that identity to accomplish a goal. An adversary may craft messages that appear to come from a different principle or use stolen / spoofed authentication credentials.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-287](/wiki/p/weakness/CWE-287)

## Prerequisites

- The identity associated with the message or resource must be removable or modifiable in an undetectable way.

## Consequences

- Confidentiality, Integrity, Authentication, Access Control: Gain Privileges

## Mitigations

- Employ robust authentication processes (e.g., multi-factor authentication).

## Source

- [MITRE CAPEC CAPEC-151](https://capec.mitre.org/data/definitions/151.html)
