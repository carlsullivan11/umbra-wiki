---
slug: attack-pattern/CAPEC-320
title: "CAPEC-320 — TCP Timestamp Probe"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-320]
cwe_ids: [CWE-200]
related: [weakness/CWE-200]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-320
updated_at: 2026-08-31
summary: "This OS fingerprinting probe examines the remote server's implementation of TCP timestamps. Not all operating systems implement timestamps within the TCP header, but when timestamps are used then this provides the attacker with a means to guess the operating system of the target.…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/320.html
---

# CAPEC-320: TCP Timestamp Probe

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Low |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

This OS fingerprinting probe examines the remote server's implementation of TCP timestamps. Not all operating systems implement timestamps within the TCP header, but when timestamps are used then this provides the attacker with a means to guess the operating system of the target. The attacker begins by probing any active TCP service in order to get response which contains a TCP timestamp. Different Operating systems update the timestamp value using different intervals. This type of analysis is most accurate when multiple timestamp responses are received and then analyzed. TCP timestamps can be found in the TCP Options field of the TCP header.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-200](/wiki/p/weakness/CWE-200)

## Prerequisites

- The ability to monitor and interact with network communications.Access to at least one host, and the privileges to interface with the network interface card.The target OS must support the TCP timestamp option in order to obtain a fingerprint.

## Consequences

- Confidentiality: Read Data
- Confidentiality, Access Control, Authorization: Bypass Protection Mechanism

## Source

- [MITRE CAPEC CAPEC-320](https://capec.mitre.org/data/definitions/320.html)
