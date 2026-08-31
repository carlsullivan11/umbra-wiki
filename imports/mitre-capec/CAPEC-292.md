---
slug: attack-pattern/CAPEC-292
title: "CAPEC-292 — Host Discovery"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-292]
cwe_ids: [CWE-200]
mitre_ids: [T1018]
related: [weakness/CWE-200, technique/T1018]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-292
updated_at: 2026-08-31
summary: "An adversary sends a probe to an IP address to determine if the host is alive. Host discovery is one of the earliest phases of network reconnaissance. The adversary usually starts with a range of IP addresses belonging to a target network and uses various methods to determine if …"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/292.html
---

# CAPEC-292: Host Discovery

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Low |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary sends a probe to an IP address to determine if the host is alive. Host discovery is one of the earliest phases of network reconnaissance. The adversary usually starts with a range of IP addresses belonging to a target network and uses various methods to determine if a host is present at that IP address. Host discovery is usually referred to as 'Ping' scanning using a sonar analogy. The goal is to send a packet through to the IP address and solicit a response from the host. As such, a 'ping' can be virtually any crafted packet whatsoever, provided the adversary can identify a functional host based on its response. An attack of this nature is usually carried out with a 'ping sweep,' where a particular kind of ping is sent to a range of IP addresses.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-200](/wiki/p/weakness/CWE-200)

**ATT&CK techniques:** [T1018](/wiki/p/technique/T1018)

## Prerequisites

- The adversary requires logical access to the target network in order to carry out host discovery.

## Consequences

- Confidentiality: Other
- Confidentiality, Access Control, Authorization: Bypass Protection Mechanism, Hide Activities

## Source

- [MITRE CAPEC CAPEC-292](https://capec.mitre.org/data/definitions/292.html)
