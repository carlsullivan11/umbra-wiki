---
slug: attack-pattern/CAPEC-496
title: "CAPEC-496 — ICMP Fragmentation"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-496]
cwe_ids: [CWE-404, CWE-770]
related: [weakness/CWE-404, weakness/CWE-770]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-496
updated_at: 2026-08-31
summary: "An attacker may execute a ICMP Fragmentation attack against a target with the intention of consuming resources or causing a crash. The attacker crafts a large number of identical fragmented IP packets containing a portion of a fragmented ICMP message. The attacker these sends the…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/496.html
---

# CAPEC-496: ICMP Fragmentation

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | — |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker may execute a ICMP Fragmentation attack against a target with the intention of consuming resources or causing a crash. The attacker crafts a large number of identical fragmented IP packets containing a portion of a fragmented ICMP message. The attacker these sends these messages to a target host which causes the host to become non-responsive. Another vector may be sending a fragmented ICMP message to a target host with incorrect sizes in the header which causes the host to hang.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-404](/wiki/p/weakness/CWE-404), [CWE-770](/wiki/p/weakness/CWE-770)

## Prerequisites

- This type of an attack requires the target system to be running a vulnerable implementation of IP, and the attacker needs to ability to send arbitrary sized ICMP packets to the target.

## Mitigations

- This attack may be mitigated through egress filtering based on ICMP payload so a network is a "good neighbor" to other networks. Bad IP implementations become patched, so using the proper version of a browser or OS is recommended.

## Source

- [MITRE CAPEC CAPEC-496](https://capec.mitre.org/data/definitions/496.html)
