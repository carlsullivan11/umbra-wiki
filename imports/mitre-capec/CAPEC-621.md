---
slug: attack-pattern/CAPEC-621
title: "CAPEC-621 — Analysis of Packet Timing and Sizes"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-621]
cwe_ids: [CWE-201]
related: [weakness/CWE-201]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-621
updated_at: 2026-08-31
summary: "An attacker may intercept and log encrypted transmissions for the purpose of analyzing metadata such as packet timing and sizes. Although the actual data may be encrypted, this metadata may reveal valuable information to an attacker. Note that this attack is applicable to VOIP da…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/621.html
---

# CAPEC-621: Analysis of Packet Timing and Sizes

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Low |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker may intercept and log encrypted transmissions for the purpose of analyzing metadata such as packet timing and sizes. Although the actual data may be encrypted, this metadata may reveal valuable information to an attacker. Note that this attack is applicable to VOIP data as well as application data, especially for interactive apps that require precise timing and low-latency (e.g. thin-clients).

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-201](/wiki/p/weakness/CWE-201)

## Prerequisites

- Use of untrusted communication paths enables an attacker to intercept and log communications, including metadata such as packet timing and sizes.

## Skills required

- High: These attacks generally require sophisticated machine learning techniques and require traffic capture as a prerequisite.

## Consequences

- Confidentiality: Read Data

## Mitigations

- Distort packet sizes and timing at VPN layer by adding padding to normalize packet sizes and timing delays to reduce information leakage via timing.

## Source

- [MITRE CAPEC CAPEC-621](https://capec.mitre.org/data/definitions/621.html)
