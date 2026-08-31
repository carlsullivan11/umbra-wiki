---
slug: attack-pattern/CAPEC-220
title: "CAPEC-220 — Client-Server Protocol Manipulation"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-220]
cwe_ids: [CWE-757]
related: [weakness/CWE-757]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-220
updated_at: 2026-08-31
summary: "An adversary takes advantage of weaknesses in the protocol by which a client and server are communicating to perform unexpected actions. Communication protocols are necessary to transfer messages between client and server applications. Moreover, different protocols may be used fo…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/220.html
---

# CAPEC-220: Client-Server Protocol Manipulation

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary takes advantage of weaknesses in the protocol by which a client and server are communicating to perform unexpected actions. Communication protocols are necessary to transfer messages between client and server applications. Moreover, different protocols may be used for different types of interactions.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-757](/wiki/p/weakness/CWE-757)

## Prerequisites

- The client and/or server must utilize a protocol that has a weakness allowing manipulation of the interaction.

## Source

- [MITRE CAPEC CAPEC-220](https://capec.mitre.org/data/definitions/220.html)
