---
slug: attack-pattern/CAPEC-552
title: "CAPEC-552 — Install Rootkit"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-552]
cwe_ids: [CWE-284]
mitre_ids: [T1014, T1542.003, T1547.006]
related: [weakness/CWE-284, technique/T1014, technique/T1542.003, technique/T1547.006]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-552
updated_at: 2026-08-31
summary: "An adversary exploits a weakness in authentication to install malware that alters the functionality and information provide by targeted operating system API calls. Often referred to as rootkits, it is often used to hide the presence of programs, files, network connections, servic…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/552.html
---

# CAPEC-552: Install Rootkit

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary exploits a weakness in authentication to install malware that alters the functionality and information provide by targeted operating system API calls. Often referred to as rootkits, it is often used to hide the presence of programs, files, network connections, services, drivers, and other system components.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-284](/wiki/p/weakness/CWE-284)

**ATT&CK techniques:** [T1014](/wiki/p/technique/T1014), [T1542.003](/wiki/p/technique/T1542.003), [T1547.006](/wiki/p/technique/T1547.006)

## Mitigations

- Prevent adversary access to privileged accounts necessary to install rootkits.

## Source

- [MITRE CAPEC CAPEC-552](https://capec.mitre.org/data/definitions/552.html)
