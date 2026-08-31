---
slug: attack-pattern/CAPEC-647
title: "CAPEC-647 — Collect Data from Registries"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-647]
cwe_ids: [CWE-285]
mitre_ids: [T1005, T1012, T1552.002]
related: [weakness/CWE-285, technique/T1005, technique/T1012, technique/T1552.002]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-647
updated_at: 2026-08-31
summary: "An adversary exploits a weakness in authorization to gather system-specific data and sensitive information within a registry (e.g., Windows Registry, Mac plist). These contain information about the system configuration, software, operating system, and security. The adversary can …"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/647.html
---

# CAPEC-647: Collect Data from Registries

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary exploits a weakness in authorization to gather system-specific data and sensitive information within a registry (e.g., Windows Registry, Mac plist). These contain information about the system configuration, software, operating system, and security. The adversary can leverage information gathered in order to carry out further attacks.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-285](/wiki/p/weakness/CWE-285)

**ATT&CK techniques:** [T1005](/wiki/p/technique/T1005), [T1012](/wiki/p/technique/T1012), [T1552.002](/wiki/p/technique/T1552.002)

## Prerequisites

- The adversary must have obtained logical access to the system by some means (e.g., via obtained credentials or planting malware on the system).
- The adversary must have capability to navigate the operating system to peruse the registry.

## Skills required

- Low: Once the adversary has logical access (which can potentially require high knowledge and skill level), the adversary needs only the capability and facility to navigate the system through the OS graphical user interface or the command line.

## Consequences

- Confidentiality: Read Data

## Mitigations

- Employ a robust and layered defensive posture in order to prevent unauthorized users on your system.
- Employ robust identification and audit/blocking via using an allowlist of applications on your system. Unnecessary applications, utilities, and configurations will have a presence in the system registry that can be leveraged by an adversary through this attack pattern.

## Source

- [MITRE CAPEC CAPEC-647](https://capec.mitre.org/data/definitions/647.html)
