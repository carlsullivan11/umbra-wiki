---
slug: attack-pattern/CAPEC-130
title: "CAPEC-130 — Excessive Allocation"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-130]
cwe_ids: [CWE-404, CWE-770, CWE-1325]
mitre_ids: [T1499.003]
related: [weakness/CWE-404, weakness/CWE-770, weakness/CWE-1325, technique/T1499.003]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-130
updated_at: 2026-08-31
summary: "An adversary causes the target to allocate excessive resources to servicing the attackers' request, thereby reducing the resources available for legitimate services and degrading or denying services. Usually, this attack focuses on memory allocation, but any finite resource on th…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/130.html
---

# CAPEC-130: Excessive Allocation

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Medium |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary causes the target to allocate excessive resources to servicing the attackers' request, thereby reducing the resources available for legitimate services and degrading or denying services. Usually, this attack focuses on memory allocation, but any finite resource on the target could be the attacked, including bandwidth, processing cycles, or other resources. This attack does not attempt to force this allocation through a large number of requests (that would be Resource Depletion through Flooding) but instead uses one or a small number of requests that are carefully formatted to force the target to allocate excessive resources to service this request(s). Often this attack takes advantage of a bug in the target to cause the target to allocate resources vastly beyond what would be needed for a normal request.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-404](/wiki/p/weakness/CWE-404), [CWE-770](/wiki/p/weakness/CWE-770), [CWE-1325](/wiki/p/weakness/CWE-1325)

**ATT&CK techniques:** [T1499.003](/wiki/p/technique/T1499.003)

## Prerequisites

- The target must accept service requests from the attacker and the adversary must be able to control the resource allocation associated with this request to be in excess of the normal allocation. The latter is usually accomplished through the presence of a bug on the target that allows the adversary to manipulate variables used in the allocation.

## Consequences

- Availability: Resource Consumption

## Mitigations

- Limit the amount of resources that are accessible to unprivileged users.
- Assume all input is malicious. Consider all potentially relevant properties when validating input.
- Consider uniformly throttling all requests in order to make it more difficult to consume resources more quickly than they can again be freed.
- Use resource-limiting settings, if possible.

## Source

- [MITRE CAPEC CAPEC-130](https://capec.mitre.org/data/definitions/130.html)
