---
slug: attack-pattern/CAPEC-150
title: "CAPEC-150 — Collect Data from Common Resource Locations"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-150]
cwe_ids: [CWE-552, CWE-1239, CWE-1258, CWE-1266, CWE-1272, CWE-1323, CWE-1330]
mitre_ids: [T1003, T1119, T1213, T1530, T1555, T1602]
related: [weakness/CWE-552, weakness/CWE-1239, weakness/CWE-1258, weakness/CWE-1266, weakness/CWE-1272, weakness/CWE-1323, weakness/CWE-1330, technique/T1003, technique/T1119, technique/T1213, technique/T1530, technique/T1555, technique/T1602]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-150
updated_at: 2026-08-31
summary: "An adversary exploits well-known locations for resources for the purposes of undermining the security of the target. In many, if not most systems, files and resources are organized in a default tree structure. This can be useful for adversaries because they often know where to lo…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/150.html
---

# CAPEC-150: Collect Data from Common Resource Locations

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary exploits well-known locations for resources for the purposes of undermining the security of the target. In many, if not most systems, files and resources are organized in a default tree structure. This can be useful for adversaries because they often know where to look for resources or files that are necessary for attacks. Even when the precise location of a targeted resource may not be known, naming conventions may indicate a small area of the target machine's file tree where the resources are typically located. For example, configuration files are normally stored in the /etc director on Unix systems. Adversaries can take advantage of this to commit other types of attacks.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-552](/wiki/p/weakness/CWE-552), [CWE-1239](/wiki/p/weakness/CWE-1239), [CWE-1258](/wiki/p/weakness/CWE-1258), [CWE-1266](/wiki/p/weakness/CWE-1266), [CWE-1272](/wiki/p/weakness/CWE-1272), [CWE-1323](/wiki/p/weakness/CWE-1323), [CWE-1330](/wiki/p/weakness/CWE-1330)

**ATT&CK techniques:** [T1003](/wiki/p/technique/T1003), [T1119](/wiki/p/technique/T1119), [T1213](/wiki/p/technique/T1213), [T1530](/wiki/p/technique/T1530), [T1555](/wiki/p/technique/T1555), [T1602](/wiki/p/technique/T1602)

## Prerequisites

- The targeted applications must either expect files to be located at a specific location or, if the location of the files can be configured by the user, the user either failed to move the files from the default location or placed them in a conventional location for files of the given type.

## Source

- [MITRE CAPEC CAPEC-150](https://capec.mitre.org/data/definitions/150.html)
