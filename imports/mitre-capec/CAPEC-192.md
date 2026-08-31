---
slug: attack-pattern/CAPEC-192
title: "CAPEC-192 — Protocol Analysis"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-192]
cwe_ids: [CWE-326]
related: [weakness/CWE-326]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-192
updated_at: 2026-08-31
summary: "An adversary engages in activities to decipher and/or decode protocol information for a network or application communication protocol used for transmitting information between interconnected nodes or systems on a packet-switched data network. While this type of analysis involves …"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/192.html
---

# CAPEC-192: Protocol Analysis

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Low |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary engages in activities to decipher and/or decode protocol information for a network or application communication protocol used for transmitting information between interconnected nodes or systems on a packet-switched data network. While this type of analysis involves the analysis of a networking protocol inherently, it does not require the presence of an actual or physical network.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-326](/wiki/p/weakness/CWE-326)

## Prerequisites

- Access to a binary executable.
- The ability to observe and interact with a communication channel between communicating processes.

## Skills required

- High: Knowlegde of the Open Systems Interconnection model (OSI model), and famililarity with Wireshark or some other packet analyzer.

## Consequences

- Confidentiality: Read Data
- Integrity: Modify Data

## Source

- [MITRE CAPEC CAPEC-192](https://capec.mitre.org/data/definitions/192.html)
