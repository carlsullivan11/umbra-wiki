---
slug: attack-pattern/CAPEC-494
title: "CAPEC-494 — TCP Fragmentation"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-494]
cwe_ids: [CWE-404, CWE-770]
related: [weakness/CWE-404, weakness/CWE-770]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-494
updated_at: 2026-08-31
summary: "An adversary may execute a TCP Fragmentation attack against a target with the intention of avoiding filtering rules of network controls, by attempting to fragment the TCP packet such that the headers flag field is pushed into the second fragment which typically is not filtered."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/494.html
---

# CAPEC-494: TCP Fragmentation

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | — |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary may execute a TCP Fragmentation attack against a target with the intention of avoiding filtering rules of network controls, by attempting to fragment the TCP packet such that the headers flag field is pushed into the second fragment which typically is not filtered.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-404](/wiki/p/weakness/CWE-404), [CWE-770](/wiki/p/weakness/CWE-770)

## Prerequisites

- This type of an attack requires the target system to be running a vulnerable implementation of IP, and the adversary needs to ability to send TCP packets of arbitrary size with crafted data.

## Mitigations

- This attack may be mitigated by enforcing rules at the router following the guidance of RFC1858. The essential part of the guidance is creating the following rule "IF FO=1 and PROTOCOL=TCP then DROP PACKET" as this mitigated both tiny fragment and overlapping fragment attacks in IPv4. In IPv6 overlapping(RFC5722) additional steps may be required such as deep packet inspection. The delayed fragments may be mitigated by enforcing a timeout on the transmission to receive all packets by a certain time since the first packet is received. According to RFC2460 IPv6 implementations should enforce a rule to discard all fragments if the fragments are not ALL received within 60 seconds of the FIRST arriving fragment.

## Source

- [MITRE CAPEC CAPEC-494](https://capec.mitre.org/data/definitions/494.html)
