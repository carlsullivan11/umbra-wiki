---
slug: attack-pattern/CAPEC-616
title: "CAPEC-616 — Establish Rogue Location"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-616]
cwe_ids: [CWE-200]
mitre_ids: [T1036.005]
related: [weakness/CWE-200, technique/T1036.005]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-616
updated_at: 2026-08-31
summary: "An adversary provides a malicious version of a resource at a location that is similar to the expected location of a legitimate resource. After establishing the rogue location, the adversary waits for a victim to visit the location and access the malicious resource."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/616.html
---

# CAPEC-616: Establish Rogue Location

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Medium |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary provides a malicious version of a resource at a location that is similar to the expected location of a legitimate resource. After establishing the rogue location, the adversary waits for a victim to visit the location and access the malicious resource.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-200](/wiki/p/weakness/CWE-200)

**ATT&CK techniques:** [T1036.005](/wiki/p/technique/T1036.005)

## Prerequisites

- A resource is expected to available to the user.

## Skills required

- Low: Adversaries can often purchase low-cost technology to implement rogue access points.

## Consequences

- Confidentiality, Integrity: Other

## Source

- [MITRE CAPEC CAPEC-616](https://capec.mitre.org/data/definitions/616.html)
