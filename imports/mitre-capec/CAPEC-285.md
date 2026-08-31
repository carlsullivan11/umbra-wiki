---
slug: attack-pattern/CAPEC-285
title: "CAPEC-285 — ICMP Echo Request Ping"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-285]
cwe_ids: [CWE-200]
related: [weakness/CWE-200]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-285
updated_at: 2026-08-31
summary: "An adversary sends out an ICMP Type 8 Echo Request, commonly known as a 'Ping', in order to determine if a target system is responsive. If the request is not blocked by a firewall or ACL, the target host will respond with an ICMP Type 0 Echo Reply datagram. This type of exchange …"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/285.html
---

# CAPEC-285: ICMP Echo Request Ping

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Low |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary sends out an ICMP Type 8 Echo Request, commonly known as a 'Ping', in order to determine if a target system is responsive. If the request is not blocked by a firewall or ACL, the target host will respond with an ICMP Type 0 Echo Reply datagram. This type of exchange is usually referred to as a 'Ping' due to the Ping utility present in almost all operating systems. Ping, as commonly implemented, allows a user to test for alive hosts, measure round-trip time, and measure the percentage of packet loss.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-200](/wiki/p/weakness/CWE-200)

## Prerequisites

- The ability to send an ICMP type 8 query (Echo Request) to a remote target and receive an ICMP type 0 message (ICMP Echo Reply) in response. Any firewalls or access control lists between the sender and receiver must allow ICMP Type 8 and ICMP Type 0 messages in order for a ping operation to succeed.

## Skills required

- Low: The adversary needs to know certain linux commands for this type of attack.

## Consequences

- Confidentiality: Other

## Mitigations

- Consider configuring firewall rules to block ICMP Echo requests and prevent replies. If not practical, monitor and consider action when a system has fast and a repeated pattern of requests that move incrementally through port numbers.

## Source

- [MITRE CAPEC CAPEC-285](https://capec.mitre.org/data/definitions/285.html)
