---
slug: attack-pattern/CAPEC-538
title: "CAPEC-538 — Open-Source Library Manipulation"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-538]
cwe_ids: [CWE-494, CWE-829]
mitre_ids: [T1195.001]
related: [weakness/CWE-494, weakness/CWE-829, technique/T1195.001]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-538
updated_at: 2026-08-31
summary: "Adversaries implant malicious code in open source software (OSS) libraries to have it widely distributed, as OSS is commonly downloaded by developers and other users to incorporate into software development projects. The adversary can have a particular system in mind to target, o…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/538.html
---

# CAPEC-538: Open-Source Library Manipulation

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | High |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

Adversaries implant malicious code in open source software (OSS) libraries to have it widely distributed, as OSS is commonly downloaded by developers and other users to incorporate into software development projects. The adversary can have a particular system in mind to target, or the implantation can be the first stage of follow-on attacks on many systems.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-494](/wiki/p/weakness/CWE-494), [CWE-829](/wiki/p/weakness/CWE-829)

**ATT&CK techniques:** [T1195.001](/wiki/p/technique/T1195.001)

## Prerequisites

- Access to the open source code base being used by the manufacturer in a system being developed or currently deployed at a victim location.

## Skills required

- High: Advanced knowledge about the inclusion and specific usage of an open source code project within system being targeted for infiltration.

## Source

- [MITRE CAPEC CAPEC-538](https://capec.mitre.org/data/definitions/538.html)
