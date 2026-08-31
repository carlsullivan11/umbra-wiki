---
slug: attack-pattern/CAPEC-545
title: "CAPEC-545 — Pull Data from System Resources"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-545]
cwe_ids: [CWE-1239, CWE-1243, CWE-1258, CWE-1266, CWE-1272, CWE-1278, CWE-1323, CWE-1330]
mitre_ids: [T1005, T1555.001]
related: [weakness/CWE-1239, weakness/CWE-1243, weakness/CWE-1258, weakness/CWE-1266, weakness/CWE-1272, weakness/CWE-1278, weakness/CWE-1323, weakness/CWE-1330, technique/T1005, technique/T1555.001]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-545
updated_at: 2026-08-31
summary: "An adversary who is authorized or has the ability to search known system resources, does so with the intention of gathering useful information. System resources include files, memory, and other aspects of the target system. In this pattern of attack, the adversary does not necess…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/545.html
---

# CAPEC-545: Pull Data from System Resources

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | — |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary who is authorized or has the ability to search known system resources, does so with the intention of gathering useful information. System resources include files, memory, and other aspects of the target system. In this pattern of attack, the adversary does not necessarily know what they are going to find when they start pulling data. This is different than CAPEC-150 where the adversary knows what they are looking for due to the common location.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-1239](/wiki/p/weakness/CWE-1239), [CWE-1243](/wiki/p/weakness/CWE-1243), [CWE-1258](/wiki/p/weakness/CWE-1258), [CWE-1266](/wiki/p/weakness/CWE-1266), [CWE-1272](/wiki/p/weakness/CWE-1272), [CWE-1278](/wiki/p/weakness/CWE-1278), [CWE-1323](/wiki/p/weakness/CWE-1323), [CWE-1330](/wiki/p/weakness/CWE-1330)

**ATT&CK techniques:** [T1005](/wiki/p/technique/T1005), [T1555.001](/wiki/p/technique/T1555.001)

## Source

- [MITRE CAPEC CAPEC-545](https://capec.mitre.org/data/definitions/545.html)
