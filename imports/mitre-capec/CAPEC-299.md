---
slug: attack-pattern/CAPEC-299
title: "CAPEC-299 — TCP SYN Ping"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-299]
cwe_ids: [CWE-200]
related: [weakness/CWE-200]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-299
updated_at: 2026-08-31
summary: "An adversary uses TCP SYN packets as a means towards host discovery. Typical RFC 793 behavior specifies that when a TCP port is open, a host must respond to an incoming SYN 'synchronize' packet by completing stage two of the 'three-way handshake' - by sending an SYN/ACK in respon…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/299.html
---

# CAPEC-299: TCP SYN Ping

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Low |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary uses TCP SYN packets as a means towards host discovery. Typical RFC 793 behavior specifies that when a TCP port is open, a host must respond to an incoming SYN "synchronize" packet by completing stage two of the 'three-way handshake' - by sending an SYN/ACK in response. When a port is closed, RFC 793 behavior is to respond with a RST "reset" packet. This behavior can be used to 'ping' a target to see if it is alive by sending a TCP SYN packet to a port and then looking for a RST or an ACK packet in response.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-200](/wiki/p/weakness/CWE-200)

## Prerequisites

- The ability to send a TCP SYN packet to a remote target. Depending upon the operating system, the ability to craft SYN packets may require elevated privileges.

## Skills required

- Low: The adversary needs to know how to craft and send protocol commands from the command line or within a tool.

## Consequences

- Confidentiality: Other
- Confidentiality, Access Control, Authorization: Bypass Protection Mechanism, Hide Activities

## Source

- [MITRE CAPEC CAPEC-299](https://capec.mitre.org/data/definitions/299.html)
