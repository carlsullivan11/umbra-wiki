---
slug: attack-pattern/CAPEC-202
title: "CAPEC-202 — Create Malicious Client"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-202]
cwe_ids: [CWE-602]
related: [weakness/CWE-602]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-202
updated_at: 2026-08-31
summary: "An adversary creates a client application to interface with a target service where the client violates assumptions the service makes about clients. Services that have designated client applications (as opposed to services that use general client applications, such as IMAP or POP …"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/202.html
---

# CAPEC-202: Create Malicious Client

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary creates a client application to interface with a target service where the client violates assumptions the service makes about clients. Services that have designated client applications (as opposed to services that use general client applications, such as IMAP or POP mail servers which can interact with any IMAP or POP client) may assume that the client will follow specific procedures.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-602](/wiki/p/weakness/CWE-602)

## Prerequisites

- The targeted service must make assumptions about the behavior of the client application that interacts with it, which can be abused by an adversary.

## Source

- [MITRE CAPEC CAPEC-202](https://capec.mitre.org/data/definitions/202.html)
