---
slug: attack-pattern/CAPEC-594
title: "CAPEC-594 — Traffic Injection"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-594]
cwe_ids: [CWE-940]
related: [weakness/CWE-940]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-594
updated_at: 2026-08-31
summary: "An adversary injects traffic into the target's network connection. The adversary is therefore able to degrade or disrupt the connection, and potentially modify the content. This is not a flooding attack, as the adversary is not focusing on exhausting resources. Instead, the adver…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/594.html
---

# CAPEC-594: Traffic Injection

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | — |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary injects traffic into the target's network connection. The adversary is therefore able to degrade or disrupt the connection, and potentially modify the content. This is not a flooding attack, as the adversary is not focusing on exhausting resources. Instead, the adversary is crafting a specific input to affect the system in a particular way.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-940](/wiki/p/weakness/CWE-940)

## Prerequisites

- The target application must leverage an open communications channel.
- The channel on which the target communicates must be vulnerable to interception (e.g., adversary in the middle attack - CAPEC-94).

## Consequences

- Availability: Unreliable Execution
- Integrity: Other

## Source

- [MITRE CAPEC CAPEC-594](https://capec.mitre.org/data/definitions/594.html)
