---
slug: attack-pattern/CAPEC-312
title: "CAPEC-312 — Active OS Fingerprinting"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-312]
cwe_ids: [CWE-200]
mitre_ids: [T1082]
related: [weakness/CWE-200, technique/T1082]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-312
updated_at: 2026-08-31
summary: "An adversary engages in activity to detect the operating system or firmware version of a remote target by interrogating a device, server, or platform with a probe designed to solicit behavior that will reveal information about the operating systems or firmware in the environment.…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/312.html
---

# CAPEC-312: Active OS Fingerprinting

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Low |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary engages in activity to detect the operating system or firmware version of a remote target by interrogating a device, server, or platform with a probe designed to solicit behavior that will reveal information about the operating systems or firmware in the environment. Operating System detection is possible because implementations of common protocols (Such as IP or TCP) differ in distinct ways. While the implementation differences are not sufficient to 'break' compatibility with the protocol the differences are detectable because the target will respond in unique ways to specific probing activity that breaks the semantic or logical rules of packet construction for a protocol. Different operating systems will have a unique response to the anomalous input, providing the basis to fingerprint the OS behavior. This type of OS fingerprinting can distinguish between operating system types and versions.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-200](/wiki/p/weakness/CWE-200)

**ATT&CK techniques:** [T1082](/wiki/p/technique/T1082)

## Prerequisites

- The ability to monitor and interact with network communications.Access to at least one host, and the privileges to interface with the network interface card.

## Consequences

- Confidentiality: Read Data
- Confidentiality, Access Control, Authorization: Hide Activities

## Source

- [MITRE CAPEC CAPEC-312](https://capec.mitre.org/data/definitions/312.html)
