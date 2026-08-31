---
slug: attack-pattern/CAPEC-564
title: "CAPEC-564 — Run Software at Logon"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-564]
cwe_ids: [CWE-284]
mitre_ids: [T1037, T1543.001, T1543.004, T1547]
related: [weakness/CWE-284, technique/T1037, technique/T1543.001, technique/T1543.004, technique/T1547]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-564
updated_at: 2026-08-31
summary: "Operating system allows logon scripts to be run whenever a specific user or users logon to a system. If adversaries can access these scripts, they may insert additional code into the logon script. This code can allow them to maintain persistence or move laterally within an enclav…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/564.html
---

# CAPEC-564: Run Software at Logon

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | — |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

Operating system allows logon scripts to be run whenever a specific user or users logon to a system. If adversaries can access these scripts, they may insert additional code into the logon script. This code can allow them to maintain persistence or move laterally within an enclave because it is executed every time the affected user or users logon to a computer. Modifying logon scripts can effectively bypass workstation and enclave firewalls. Depending on the access configuration of the logon scripts, either local credentials or a remote administrative account may be necessary.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-284](/wiki/p/weakness/CWE-284)

**ATT&CK techniques:** [T1037](/wiki/p/technique/T1037), [T1543.001](/wiki/p/technique/T1543.001), [T1543.004](/wiki/p/technique/T1543.004), [T1547](/wiki/p/technique/T1547)

## Mitigations

- Restrict write access to logon scripts to necessary administrators.

## Source

- [MITRE CAPEC CAPEC-564](https://capec.mitre.org/data/definitions/564.html)
