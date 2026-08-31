---
slug: attack-pattern/CAPEC-227
title: "CAPEC-227 — Sustained Client Engagement"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-227]
cwe_ids: [CWE-400]
mitre_ids: [T1499]
related: [weakness/CWE-400, technique/T1499]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-227
updated_at: 2026-08-31
summary: "An adversary attempts to deny legitimate users access to a resource by continually engaging a specific resource in an attempt to keep the resource tied up as long as possible. The adversary's primary goal is not to crash or flood the target, which would alert defenders; rather it…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/227.html
---

# CAPEC-227: Sustained Client Engagement

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | — |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary attempts to deny legitimate users access to a resource by continually engaging a specific resource in an attempt to keep the resource tied up as long as possible. The adversary's primary goal is not to crash or flood the target, which would alert defenders; rather it is to repeatedly perform actions or abuse algorithmic flaws such that a given resource is tied up and not available to a legitimate user. By carefully crafting a requests that keep the resource engaged through what is seemingly benign requests, legitimate users are limited or completely denied access to the resource.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-400](/wiki/p/weakness/CWE-400)

**ATT&CK techniques:** [T1499](/wiki/p/technique/T1499)

## Prerequisites

- This pattern of attack requires a temporal aspect to the servicing of a given request. Success can be achieved if the adversary can make requests that collectively take more time to complete than legitimate user requests within the same time frame.

## Mitigations

- Potential mitigations include requiring a unique login for each resource request, constraining local unprivileged access by disallowing simultaneous engagements of the resource, or limiting access to the resource to one access per IP address. In such scenarios, the adversary would have to increase engagements either by launching multiple sessions manually or programmatically to counter such defenses.

## Source

- [MITRE CAPEC CAPEC-227](https://capec.mitre.org/data/definitions/227.html)
