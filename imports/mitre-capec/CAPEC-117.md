---
slug: attack-pattern/CAPEC-117
title: "CAPEC-117 — Interception"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-117]
cwe_ids: [CWE-319]
related: [weakness/CWE-319]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-117
updated_at: 2026-08-31
summary: "An adversary monitors data streams to or from the target for information gathering purposes. This attack may be undertaken to solely gather sensitive information or to support a further attack against the target. This attack pattern can involve sniffing network traffic as well as…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/117.html
---

# CAPEC-117: Interception

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Medium |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary monitors data streams to or from the target for information gathering purposes. This attack may be undertaken to solely gather sensitive information or to support a further attack against the target. This attack pattern can involve sniffing network traffic as well as other types of data streams (e.g. radio). The adversary can attempt to initiate the establishment of a data stream or passively observe the communications as they unfold. In all variants of this attack, the adversary is not the intended recipient of the data stream. In contrast to other means of gathering information (e.g., targeting data leaks), the adversary must actively position themself so as to observe explicit data channels (e.g. network traffic) and read the content. However, this attack differs from a Adversary-In-the-Middle (CAPEC-94) attack, as the adversary does not alter the content of the communications nor forward data to the intended recipient.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-319](/wiki/p/weakness/CWE-319)

## Prerequisites

- The target must transmit data over a medium that is accessible to the adversary.

## Consequences

- Confidentiality: Read Data

## Mitigations

- Leverage encryption to encode the transmission of data thus making it accessible only to authorized parties.

## Source

- [MITRE CAPEC CAPEC-117](https://capec.mitre.org/data/definitions/117.html)
