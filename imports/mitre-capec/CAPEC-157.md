---
slug: attack-pattern/CAPEC-157
title: "CAPEC-157 — Sniffing Attacks"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-157]
cwe_ids: [CWE-311]
related: [weakness/CWE-311]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-157
updated_at: 2026-08-31
summary: "In this attack pattern, the adversary intercepts information transmitted between two third parties. The adversary must be able to observe, read, and/or hear the communication traffic, but not necessarily block the communication or change its content. Any transmission medium can t…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/157.html
---

# CAPEC-157: Sniffing Attacks

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

In this attack pattern, the adversary intercepts information transmitted between two third parties. The adversary must be able to observe, read, and/or hear the communication traffic, but not necessarily block the communication or change its content. Any transmission medium can theoretically be sniffed if the adversary can examine the contents between the sender and recipient. Sniffing Attacks are similar to Adversary-In-The-Middle attacks (CAPEC-94), but are entirely passive. AiTM attacks are predominantly active and often alter the content of the communications themselves.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-311](/wiki/p/weakness/CWE-311)

## Prerequisites

- The target data stream must be transmitted on a medium to which the adversary has access.

## Consequences

- Confidentiality: Read Data

## Mitigations

- Encrypt sensitive information when transmitted on insecure mediums to prevent interception.

## Source

- [MITRE CAPEC CAPEC-157](https://capec.mitre.org/data/definitions/157.html)
