---
slug: attack-pattern/CAPEC-291
title: "CAPEC-291 — DNS Zone Transfers"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-291]
cwe_ids: [CWE-200]
related: [weakness/CWE-200]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-291
updated_at: 2026-08-31
summary: "An attacker exploits a DNS misconfiguration that permits a ZONE transfer. Some external DNS servers will return a list of IP address and valid hostnames. Under certain conditions, it may even be possible to obtain Zone data about the organization's internal network. When successf…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/291.html
---

# CAPEC-291: DNS Zone Transfers

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Low |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker exploits a DNS misconfiguration that permits a ZONE transfer. Some external DNS servers will return a list of IP address and valid hostnames. Under certain conditions, it may even be possible to obtain Zone data about the organization's internal network. When successful the attacker learns valuable information about the topology of the target organization, including information about particular servers, their role within the IT structure, and possibly information about the operating systems running upon the network. This is configuration dependent behavior so it may also be required to search out multiple DNS servers while attempting to find one with ZONE transfers allowed.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-200](/wiki/p/weakness/CWE-200)

## Prerequisites

- Access to a DNS server that allows Zone transfers.

## Consequences

- Confidentiality: Read Data

## Source

- [MITRE CAPEC CAPEC-291](https://capec.mitre.org/data/definitions/291.html)
