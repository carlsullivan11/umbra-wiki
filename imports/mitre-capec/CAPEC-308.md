---
slug: attack-pattern/CAPEC-308
title: "CAPEC-308 — UDP Scan"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-308]
cwe_ids: [CWE-200]
related: [weakness/CWE-200]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-308
updated_at: 2026-08-31
summary: "An adversary engages in UDP scanning to gather information about UDP port status on the target system. UDP scanning methods involve sending a UDP datagram to the target port and looking for evidence that the port is closed. Open UDP ports usually do not respond to UDP datagrams a…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/308.html
---

# CAPEC-308: UDP Scan

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Low |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary engages in UDP scanning to gather information about UDP port status on the target system. UDP scanning methods involve sending a UDP datagram to the target port and looking for evidence that the port is closed. Open UDP ports usually do not respond to UDP datagrams as there is no stateful mechanism within the protocol that requires building or establishing a session. Responses to UDP datagrams are therefore application specific and cannot be relied upon as a method of detecting an open port. UDP scanning relies heavily upon ICMP diagnostic messages in order to determine the status of a remote port.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-200](/wiki/p/weakness/CWE-200)

## Prerequisites

- The ability to send UDP datagrams to a host and receive ICMP error messages from that host. In cases where particular types of ICMP messaging is disallowed, the reliability of UDP scanning drops off sharply.

## Consequences

- Confidentiality: Other
- Confidentiality, Access Control, Authorization: Bypass Protection Mechanism, Hide Activities

## Mitigations

- Firewalls or ACLs which block egress ICMP error types effectively prevent UDP scans from returning any useful information.
- UDP scanning is complicated by rate limiting mechanisms governing ICMP error messages.

## Source

- [MITRE CAPEC CAPEC-308](https://capec.mitre.org/data/definitions/308.html)
