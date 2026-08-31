---
slug: attack-pattern/CAPEC-448
title: "CAPEC-448 — Embed Virus into DLL"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-448]
cwe_ids: [CWE-506]
mitre_ids: [T1027.009]
related: [weakness/CWE-506, technique/T1027.009]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-448
updated_at: 2026-08-31
summary: "An adversary tampers with a DLL and embeds a computer virus into gaps between legitimate machine instructions. These gaps may be the result of compiler optimizations that pad memory blocks for performance gains. The embedded virus then attempts to infect any machine which interfa…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/448.html
---

# CAPEC-448: Embed Virus into DLL

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | High |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary tampers with a DLL and embeds a computer virus into gaps between legitimate machine instructions. These gaps may be the result of compiler optimizations that pad memory blocks for performance gains. The embedded virus then attempts to infect any machine which interfaces with the product, and possibly steal private data or eavesdrop.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-506](/wiki/p/weakness/CWE-506)

**ATT&CK techniques:** [T1027.009](/wiki/p/technique/T1027.009)

## Prerequisites

- Access to the software currently deployed at a victim location. This access is often obtained by leveraging another attack pattern to gain permissions that the adversary wouldn't normally have.

## Consequences

- Authorization: Execute Unauthorized Commands

## Mitigations

- Leverage anti-virus products to detect and quarantine software with known virus.

## Source

- [MITRE CAPEC CAPEC-448](https://capec.mitre.org/data/definitions/448.html)
