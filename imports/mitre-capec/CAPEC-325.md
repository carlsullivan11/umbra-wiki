---
slug: attack-pattern/CAPEC-325
title: "CAPEC-325 — TCP Congestion Control Flag (ECN) Probe"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-325]
cwe_ids: [CWE-200]
related: [weakness/CWE-200]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-325
updated_at: 2026-08-31
summary: "This OS fingerprinting probe checks to see if the remote host supports explicit congestion notification (ECN) messaging. ECN messaging was designed to allow routers to notify a remote host when signal congestion problems are occurring. Explicit Congestion Notification messaging i…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/325.html
---

# CAPEC-325: TCP Congestion Control Flag (ECN) Probe

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Low |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

This OS fingerprinting probe checks to see if the remote host supports explicit congestion notification (ECN) messaging. ECN messaging was designed to allow routers to notify a remote host when signal congestion problems are occurring. Explicit Congestion Notification messaging is defined by RFC 3168. Different operating systems and versions may or may not implement ECN notifications, or may respond uniquely to particular ECN flag types.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-200](/wiki/p/weakness/CWE-200)

## Prerequisites

- The ability to monitor and interact with network communications.Access to at least one host, and the privileges to interface with the network interface card.

## Consequences

- Confidentiality: Read Data
- Confidentiality, Access Control, Authorization: Bypass Protection Mechanism, Hide Activities

## Source

- [MITRE CAPEC CAPEC-325](https://capec.mitre.org/data/definitions/325.html)
