---
slug: attack-pattern/CAPEC-122
title: "CAPEC-122 — Privilege Abuse"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-122]
cwe_ids: [CWE-269, CWE-732, CWE-1317]
mitre_ids: [T1548]
related: [weakness/CWE-269, weakness/CWE-732, weakness/CWE-1317, technique/T1548]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-122
updated_at: 2026-08-31
summary: "An adversary is able to exploit features of the target that should be reserved for privileged users or administrators but are exposed to use by lower or non-privileged accounts. Access to sensitive information and functionality must be controlled to ensure that only authorized us…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/122.html
---

# CAPEC-122: Privilege Abuse

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary is able to exploit features of the target that should be reserved for privileged users or administrators but are exposed to use by lower or non-privileged accounts. Access to sensitive information and functionality must be controlled to ensure that only authorized users are able to access these resources.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-269](/wiki/p/weakness/CWE-269), [CWE-732](/wiki/p/weakness/CWE-732), [CWE-1317](/wiki/p/weakness/CWE-1317)

**ATT&CK techniques:** [T1548](/wiki/p/technique/T1548)

## Prerequisites

- The target must have misconfigured their access control mechanisms such that sensitive information, which should only be accessible to more trusted users, remains accessible to less trusted users.
- The adversary must have access to the target, albeit with an account that is less privileged than would be appropriate for the targeted resources.

## Skills required

- Low: Adversary can leverage privileged features they already have access to without additional effort or skill. Adversary is only required to have access to an account with improper priveleges.

## Consequences

- Integrity: Modify Data
- Confidentiality: Read Data
- Authorization: Execute Unauthorized Commands
- Authorization: Gain Privileges
- Access Control, Authorization: Bypass Protection Mechanism

## Mitigations

- Configure account privileges such privileged/administrator functionality is not exposed to non-privileged/lower accounts.

## Source

- [MITRE CAPEC CAPEC-122](https://capec.mitre.org/data/definitions/122.html)
