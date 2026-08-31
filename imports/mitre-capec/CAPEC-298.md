---
slug: attack-pattern/CAPEC-298
title: "CAPEC-298 — UDP Ping"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-298]
cwe_ids: [CWE-200]
related: [weakness/CWE-200]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-298
updated_at: 2026-08-31
summary: "An adversary sends a UDP datagram to the remote host to determine if the host is alive. If a UDP datagram is sent to an open UDP port there is very often no response, so a typical strategy for using a UDP ping is to send the datagram to a random high port on the target. The goal …"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/298.html
---

# CAPEC-298: UDP Ping

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Low |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary sends a UDP datagram to the remote host to determine if the host is alive. If a UDP datagram is sent to an open UDP port there is very often no response, so a typical strategy for using a UDP ping is to send the datagram to a random high port on the target. The goal is to solicit an 'ICMP port unreachable' message from the target, indicating that the host is alive. UDP pings are useful because some firewalls are not configured to block UDP datagrams sent to strange or typically unused ports, like ports in the 65K range. Additionally, while some firewalls may filter incoming ICMP, weaknesses in firewall rule-sets may allow certain types of ICMP (host unreachable, port unreachable) which are useful for UDP ping attempts.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-200](/wiki/p/weakness/CWE-200)

## Prerequisites

- The adversary requires the ability to send a UDP datagram to a remote host and receive a response.
- The adversary requires the ability to craft custom UDP Packets for use during network reconnaissance.
- The target's firewall must not be configured to block egress ICMP messages.

## Consequences

- Confidentiality: Other
- Confidentiality, Access Control, Authorization: Bypass Protection Mechanism, Hide Activities

## Mitigations

- Configure your firewall to block egress ICMP messages.

## Source

- [MITRE CAPEC CAPEC-298](https://capec.mitre.org/data/definitions/298.html)
