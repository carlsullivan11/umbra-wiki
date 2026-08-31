---
slug: attack-pattern/CAPEC-471
title: "CAPEC-471 — Search Order Hijacking"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-471]
cwe_ids: [CWE-427]
mitre_ids: [T1574.001, T1574.004, T1574.008]
related: [weakness/CWE-427, technique/T1574.001, technique/T1574.004, technique/T1574.008]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-471
updated_at: 2026-08-31
summary: "An adversary exploits a weakness in an application's specification of external libraries to exploit the functionality of the loader where the process loading the library searches first in the same directory in which the process binary resides and then in other directories. Exploi…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/471.html
---

# CAPEC-471: Search Order Hijacking

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Medium |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary exploits a weakness in an application's specification of external libraries to exploit the functionality of the loader where the process loading the library searches first in the same directory in which the process binary resides and then in other directories. Exploitation of this preferential search order can allow an attacker to make the loading process load the adversary's rogue library rather than the legitimate library. This attack can be leveraged with many different libraries and with many different loading processes. No forensic trails are left in the system's registry or file system that an incorrect library had been loaded.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-427](/wiki/p/weakness/CWE-427)

**ATT&CK techniques:** [T1574.001](/wiki/p/technique/T1574.001), [T1574.004](/wiki/p/technique/T1574.004), [T1574.008](/wiki/p/technique/T1574.008)

## Prerequisites

- Attacker has a mechanism to place its malicious libraries in the needed location on the file system.

## Skills required

- Medium: Ability to create a malicious library.

## Mitigations

- Design: Fix the Windows loading process to eliminate the preferential search order by looking for DLLs in the precise location where they are expected
- Design: Sign system DLLs so that unauthorized DLLs can be detected.

## Source

- [MITRE CAPEC CAPEC-471](https://capec.mitre.org/data/definitions/471.html)
