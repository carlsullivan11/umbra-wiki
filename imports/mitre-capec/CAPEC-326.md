---
slug: attack-pattern/CAPEC-326
title: "CAPEC-326 — TCP Initial Window Size Probe"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-326]
cwe_ids: [CWE-200]
related: [weakness/CWE-200]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-326
updated_at: 2026-08-31
summary: "This OS fingerprinting probe checks the initial TCP Window size. TCP stacks limit the range of sequence numbers allowable within a session to maintain the 'connected' state within TCP protocol logic. The initial window size specifies a range of acceptable sequence numbers that wi…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/326.html
---

# CAPEC-326: TCP Initial Window Size Probe

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Low |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

This OS fingerprinting probe checks the initial TCP Window size. TCP stacks limit the range of sequence numbers allowable within a session to maintain the "connected" state within TCP protocol logic. The initial window size specifies a range of acceptable sequence numbers that will qualify as a response to an ACK packet within a session. Various operating systems use different Initial window sizes. The initial window size can be sampled by establishing an ordinary TCP connection.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-200](/wiki/p/weakness/CWE-200)

## Prerequisites

- The ability to monitor and interact with network communications.Access to at least one host, and the privileges to interface with the network interface card.

## Consequences

- Confidentiality: Read Data
- Confidentiality, Access Control, Authorization: Bypass Protection Mechanism, Hide Activities

## Source

- [MITRE CAPEC CAPEC-326](https://capec.mitre.org/data/definitions/326.html)
