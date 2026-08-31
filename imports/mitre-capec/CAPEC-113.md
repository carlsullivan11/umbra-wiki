---
slug: attack-pattern/CAPEC-113
title: "CAPEC-113 — Interface Manipulation"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-113]
cwe_ids: [CWE-1192]
related: [weakness/CWE-1192]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-113
updated_at: 2026-08-31
summary: "An adversary manipulates the use or processing of an interface (e.g. Application Programming Interface (API) or System-on-Chip (SoC)) resulting in an adverse impact upon the security of the system implementing the interface. This can allow the adversary to bypass access control a…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/113.html
---

# CAPEC-113: Interface Manipulation

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary manipulates the use or processing of an interface (e.g. Application Programming Interface (API) or System-on-Chip (SoC)) resulting in an adverse impact upon the security of the system implementing the interface. This can allow the adversary to bypass access control and/or execute functionality not intended by the interface implementation, possibly compromising the system which integrates the interface. Interface manipulation can take on a number of forms including forcing the unexpected use of an interface or the use of an interface in an unintended way.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-1192](/wiki/p/weakness/CWE-1192)

## Prerequisites

- The target system must expose interface functionality in a manner that can be discovered and manipulated by an adversary. This may require reverse engineering the interface or decrypting/de-obfuscating client-server exchanges.

## Source

- [MITRE CAPEC CAPEC-113](https://capec.mitre.org/data/definitions/113.html)
