---
slug: attack-pattern/CAPEC-642
title: "CAPEC-642 — Replace Binaries"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-642]
cwe_ids: [CWE-732]
mitre_ids: [T1505.005, T1554, T1574.005]
related: [weakness/CWE-732, technique/T1505.005, technique/T1554, technique/T1574.005]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-642
updated_at: 2026-08-31
summary: "Adversaries know that certain binaries will be regularly executed as part of normal processing. If these binaries are not protected with the appropriate file system permissions, it could be possible to replace them with malware. This malware might be executed at higher system per…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/642.html
---

# CAPEC-642: Replace Binaries

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

Adversaries know that certain binaries will be regularly executed as part of normal processing. If these binaries are not protected with the appropriate file system permissions, it could be possible to replace them with malware. This malware might be executed at higher system permission levels. A variation of this pattern is to discover self-extracting installation packages that unpack binaries to directories with weak file permissions which it does not clean up appropriately. These binaries can be replaced by malware, which can then be executed.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-732](/wiki/p/weakness/CWE-732)

**ATT&CK techniques:** [T1505.005](/wiki/p/technique/T1505.005), [T1554](/wiki/p/technique/T1554), [T1574.005](/wiki/p/technique/T1574.005)

## Prerequisites

- The attacker must be able to place the malicious binary on the target machine.

## Mitigations

- Insure that binaries commonly used by the system have the correct file permissions. Set operating system policies that restrict privilege elevation of non-Administrators. Use auditing tools to observe changes to system services.

## Source

- [MITRE CAPEC CAPEC-642](https://capec.mitre.org/data/definitions/642.html)
