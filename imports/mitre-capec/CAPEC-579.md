---
slug: attack-pattern/CAPEC-579
title: "CAPEC-579 — Replace Winlogon Helper DLL"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-579]
cwe_ids: [CWE-15]
mitre_ids: [T1547.004]
related: [weakness/CWE-15, technique/T1547.004]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-579
updated_at: 2026-08-31
summary: "Winlogon is a part of Windows that performs logon actions. In Windows systems prior to Windows Vista, a registry key can be modified that causes Winlogon to load a DLL on startup. Adversaries may take advantage of this feature to load adversarial code at startup."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/579.html
---

# CAPEC-579: Replace Winlogon Helper DLL

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | — |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

Winlogon is a part of Windows that performs logon actions. In Windows systems prior to Windows Vista, a registry key can be modified that causes Winlogon to load a DLL on startup. Adversaries may take advantage of this feature to load adversarial code at startup.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-15](/wiki/p/weakness/CWE-15)

**ATT&CK techniques:** [T1547.004](/wiki/p/technique/T1547.004)

## Mitigations

- Changes to registry entries in "HKLM\Software\Microsoft\Windows NT\Winlogon\Notify" that do not correlate with known software, patch cycles, etc are suspicious. New DLLs written to System32 which do not correlate with known good software or patching may be suspicious.

## Source

- [MITRE CAPEC CAPEC-579](https://capec.mitre.org/data/definitions/579.html)
