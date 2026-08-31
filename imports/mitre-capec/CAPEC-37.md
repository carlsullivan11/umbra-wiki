---
slug: attack-pattern/CAPEC-37
title: "CAPEC-37 — Retrieve Embedded Sensitive Data"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-37]
cwe_ids: [CWE-226, CWE-311, CWE-312, CWE-314, CWE-315, CWE-318, CWE-525, CWE-1239, CWE-1258, CWE-1266, CWE-1272, CWE-1278, CWE-1301, CWE-1330]
mitre_ids: [T1005, T1552.004]
related: [weakness/CWE-226, weakness/CWE-311, weakness/CWE-312, weakness/CWE-314, weakness/CWE-315, weakness/CWE-318, weakness/CWE-525, weakness/CWE-1239, weakness/CWE-1258, weakness/CWE-1266, weakness/CWE-1272, weakness/CWE-1278, weakness/CWE-1301, weakness/CWE-1330, technique/T1005, technique/T1552.004]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-37
updated_at: 2026-08-31
summary: "An attacker examines a target system to find sensitive data that has been embedded within it. This information can reveal confidential contents, such as account numbers or individual keys/credentials that can be used as an intermediate step in a larger attack."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/37.html
---

# CAPEC-37: Retrieve Embedded Sensitive Data

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Very High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker examines a target system to find sensitive data that has been embedded within it. This information can reveal confidential contents, such as account numbers or individual keys/credentials that can be used as an intermediate step in a larger attack.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-226](/wiki/p/weakness/CWE-226), [CWE-311](/wiki/p/weakness/CWE-311), [CWE-312](/wiki/p/weakness/CWE-312), [CWE-314](/wiki/p/weakness/CWE-314), [CWE-315](/wiki/p/weakness/CWE-315), [CWE-318](/wiki/p/weakness/CWE-318), [CWE-525](/wiki/p/weakness/CWE-525), [CWE-1239](/wiki/p/weakness/CWE-1239), [CWE-1258](/wiki/p/weakness/CWE-1258), [CWE-1266](/wiki/p/weakness/CWE-1266), [CWE-1272](/wiki/p/weakness/CWE-1272), [CWE-1278](/wiki/p/weakness/CWE-1278), [CWE-1301](/wiki/p/weakness/CWE-1301), [CWE-1330](/wiki/p/weakness/CWE-1330)

**ATT&CK techniques:** [T1005](/wiki/p/technique/T1005), [T1552.004](/wiki/p/technique/T1552.004)

## Prerequisites

- In order to feasibly execute this type of attack, some valuable data must be present in client software.
- Additionally, this information must be unprotected, or protected in a flawed fashion, or through a mechanism that fails to resist reverse engineering, statistical, or other attack.

## Skills required

- Medium: The attacker must possess knowledge of client code structure as well as ability to reverse-engineer or decompile it or probe it in other ways. This knowledge is specific to the technology and language used for the client distribution

## Consequences

- Confidentiality: Read Data
- Integrity: Modify Data
- Confidentiality, Access Control, Authorization: Gain Privileges

## Source

- [MITRE CAPEC CAPEC-37](https://capec.mitre.org/data/definitions/37.html)
