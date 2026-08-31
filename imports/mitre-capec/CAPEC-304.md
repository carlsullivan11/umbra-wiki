---
slug: attack-pattern/CAPEC-304
title: "CAPEC-304 — TCP Null Scan"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-304]
cwe_ids: [CWE-200]
related: [weakness/CWE-200]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-304
updated_at: 2026-08-31
summary: "An adversary uses a TCP NULL scan to determine if ports are closed on the target machine. This scan type is accomplished by sending TCP segments with no flags in the packet header, generating packets that are illegal based on RFC 793. The RFC 793 expected behavior is that any TCP…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/304.html
---

# CAPEC-304: TCP Null Scan

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Low |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary uses a TCP NULL scan to determine if ports are closed on the target machine. This scan type is accomplished by sending TCP segments with no flags in the packet header, generating packets that are illegal based on RFC 793. The RFC 793 expected behavior is that any TCP segment with an out-of-state Flag sent to an open port is discarded, whereas segments with out-of-state flags sent to closed ports should be handled with a RST in response. This behavior should allow an attacker to scan for closed ports by sending certain types of rule-breaking packets (out of sync or disallowed by the TCB) and detect closed ports via RST packets.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-200](/wiki/p/weakness/CWE-200)

## Prerequisites

- The adversary requires logical access to the target network. NULL scanning requires the use of raw sockets, and thus cannot be performed from some Windows systems (Windows XP SP 2, for example). On Unix and Linux, raw socket manipulations require root privileges.

## Consequences

- Confidentiality: Other
- Confidentiality, Access Control, Authorization: Bypass Protection Mechanism, Hide Activities

## Mitigations

- Employ a robust network defensive posture that includes a managed IDS/IPS.

## Source

- [MITRE CAPEC CAPEC-304](https://capec.mitre.org/data/definitions/304.html)
