---
slug: attack-pattern/CAPEC-158
title: "CAPEC-158 — Sniffing Network Traffic"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-158]
cwe_ids: [CWE-311]
mitre_ids: [T1040, T1111]
related: [weakness/CWE-311, technique/T1040, technique/T1111]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-158
updated_at: 2026-08-31
summary: "In this attack pattern, the adversary monitors network traffic between nodes of a public or multicast network in an attempt to capture sensitive information at the protocol level. Network sniffing applications can reveal TCP/IP, DNS, Ethernet, and other low-level network communic…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/158.html
---

# CAPEC-158: Sniffing Network Traffic

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

In this attack pattern, the adversary monitors network traffic between nodes of a public or multicast network in an attempt to capture sensitive information at the protocol level. Network sniffing applications can reveal TCP/IP, DNS, Ethernet, and other low-level network communication information. The adversary takes a passive role in this attack pattern and simply observes and analyzes the traffic. The adversary may precipitate or indirectly influence the content of the observed transaction, but is never the intended recipient of the target information.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-311](/wiki/p/weakness/CWE-311)

**ATT&CK techniques:** [T1040](/wiki/p/technique/T1040), [T1111](/wiki/p/technique/T1111)

## Prerequisites

- The target must be communicating on a network protocol visible by a network sniffing application.
- The adversary must obtain a logical position on the network from intercepting target network traffic is possible. Depending on the network topology, traffic sniffing may be simple or challenging. If both the target sender and target recipient are members of a single subnet, the adversary must also be on that subnet in order to see their traffic communication.

## Skills required

- Low: Adversaries can obtain and set up open-source network sniffing tools easily.

## Consequences

- Confidentiality: Read Data

## Mitigations

- Obfuscate network traffic through encryption to prevent its readability by network sniffers.
- Employ appropriate levels of segmentation to your network in accordance with best practices.

## Source

- [MITRE CAPEC CAPEC-158](https://capec.mitre.org/data/definitions/158.html)
