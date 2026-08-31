---
slug: attack-pattern/CAPEC-203
title: "CAPEC-203 — Manipulate Registry Information"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-203]
cwe_ids: [CWE-15]
mitre_ids: [T1112, T1647]
related: [weakness/CWE-15, technique/T1112, technique/T1647]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-203
updated_at: 2026-08-31
summary: "An adversary exploits a weakness in authorization in order to modify content within a registry (e.g., Windows Registry, Mac plist, application registry). Editing registry information can permit the adversary to hide configuration information or remove indicators of compromise to …"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/203.html
---

# CAPEC-203: Manipulate Registry Information

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Medium |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary exploits a weakness in authorization in order to modify content within a registry (e.g., Windows Registry, Mac plist, application registry). Editing registry information can permit the adversary to hide configuration information or remove indicators of compromise to cover up activity. Many applications utilize registries to store configuration and service information. As such, modification of registry information can affect individual services (affecting billing, authorization, or even allowing for identity spoofing) or the overall configuration of a targeted application. For example, both Java RMI and SOAP use registries to track available services. Changing registry values is sometimes a preliminary step towards completing another attack pattern, but given the long term usage of many registry values, manipulation of registry information could be its own end.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-15](/wiki/p/weakness/CWE-15)

**ATT&CK techniques:** [T1112](/wiki/p/technique/T1112), [T1647](/wiki/p/technique/T1647)

## Prerequisites

- The targeted application must rely on values stored in a registry.
- The adversary must have a means of elevating permissions in order to access and modify registry content through either administrator privileges (e.g., credentialed access), or a remote access tool capable of editing a registry through an API.

## Skills required

- High: The adversary requires privileged credentials or the development/acquiring of a tailored remote access tool.

## Mitigations

- Ensure proper permissions are set for Registry hives to prevent users from modifying keys.
- Employ a robust and layered defensive posture in order to prevent unauthorized users on your system.
- Employ robust identification and audit/blocking using an allowlist of applications on your system. Unnecessary applications, utilities, and configurations will have a presence in the system registry that can be leveraged by an adversary through this attack pattern.

## Source

- [MITRE CAPEC CAPEC-203](https://capec.mitre.org/data/definitions/203.html)
