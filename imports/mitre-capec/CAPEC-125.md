---
slug: attack-pattern/CAPEC-125
title: "CAPEC-125 — Flooding"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-125]
cwe_ids: [CWE-404, CWE-770]
mitre_ids: [T1498.001, T1499]
related: [weakness/CWE-404, weakness/CWE-770, technique/T1498.001, technique/T1499]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-125
updated_at: 2026-08-31
summary: "An adversary consumes the resources of a target by rapidly engaging in a large number of interactions with the target. This type of attack generally exposes a weakness in rate limiting or flow. When successful this attack prevents legitimate users from accessing the service and c…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/125.html
---

# CAPEC-125: Flooding

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Medium |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary consumes the resources of a target by rapidly engaging in a large number of interactions with the target. This type of attack generally exposes a weakness in rate limiting or flow. When successful this attack prevents legitimate users from accessing the service and can cause the target to crash. This attack differs from resource depletion through leaks or allocations in that the latter attacks do not rely on the volume of requests made to the target but instead focus on manipulation of the target's operations. The key factor in a flooding attack is the number of requests the adversary can make in a given period of time. The greater this number, the more likely an attack is to succeed against a given target.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-404](/wiki/p/weakness/CWE-404), [CWE-770](/wiki/p/weakness/CWE-770)

**ATT&CK techniques:** [T1498.001](/wiki/p/technique/T1498.001), [T1499](/wiki/p/technique/T1499)

## Prerequisites

- Any target that services requests is vulnerable to this attack on some level of scale.

## Consequences

- Availability: Unreliable Execution, Resource Consumption

## Mitigations

- Ensure that protocols have specific limits of scale configured.
- Specify expectations for capabilities and dictate which behaviors are acceptable when resource allocation reaches limits.
- Uniformly throttle all requests in order to make it more difficult to consume resources more quickly than they can again be freed.

## Source

- [MITRE CAPEC CAPEC-125](https://capec.mitre.org/data/definitions/125.html)
