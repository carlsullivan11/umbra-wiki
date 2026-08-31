---
slug: attack-pattern/CAPEC-636
title: "CAPEC-636 — Hiding Malicious Data or Code within Files"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-636]
cwe_ids: [CWE-506]
mitre_ids: [T1001.002, T1027.003, T1027.004, T1218.001, T1221]
related: [weakness/CWE-506, technique/T1001.002, technique/T1027.003, technique/T1027.004, technique/T1218.001, technique/T1221]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-636
updated_at: 2026-08-31
summary: "Files on various operating systems can have a complex format which allows for the storage of other data, in addition to its contents. Often this is metadata about the file, such as a cached thumbnail for an image file. Unless utilities are invoked in a particular way, this data i…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/636.html
---

# CAPEC-636: Hiding Malicious Data or Code within Files

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

Files on various operating systems can have a complex format which allows for the storage of other data, in addition to its contents. Often this is metadata about the file, such as a cached thumbnail for an image file. Unless utilities are invoked in a particular way, this data is not visible during the normal use of the file. It is possible for an attacker to store malicious data or code using these facilities, which would be difficult to discover.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-506](/wiki/p/weakness/CWE-506)

**ATT&CK techniques:** [T1001.002](/wiki/p/technique/T1001.002), [T1027.003](/wiki/p/technique/T1027.003), [T1027.004](/wiki/p/technique/T1027.004), [T1218.001](/wiki/p/technique/T1218.001), [T1221](/wiki/p/technique/T1221)

## Prerequisites

- The operating system must support a file system that allows for alternate data storage for a file.

## Mitigations

- Many tools are available to search for the hidden data. Scan regularly for such data using one of these tools.

## Source

- [MITRE CAPEC CAPEC-636](https://capec.mitre.org/data/definitions/636.html)
