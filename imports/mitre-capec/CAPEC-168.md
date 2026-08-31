---
slug: attack-pattern/CAPEC-168
title: "CAPEC-168 — Windows ::DATA Alternate Data Stream"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-168]
cwe_ids: [CWE-69, CWE-212]
related: [weakness/CWE-69, weakness/CWE-212]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-168
updated_at: 2026-08-31
summary: "An attacker exploits the functionality of Microsoft NTFS Alternate Data Streams (ADS) to undermine system security. ADS allows multiple 'files' to be stored in one directory entry referenced as filename:streamname. One or more alternate data streams may be stored in any file or d…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/168.html
---

# CAPEC-168: Windows ::DATA Alternate Data Stream

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker exploits the functionality of Microsoft NTFS Alternate Data Streams (ADS) to undermine system security. ADS allows multiple "files" to be stored in one directory entry referenced as filename:streamname. One or more alternate data streams may be stored in any file or directory. Normal Microsoft utilities do not show the presence of an ADS stream attached to a file. The additional space for the ADS is not recorded in the displayed file size. The additional space for ADS is accounted for in the used space on the volume. An ADS can be any type of file. ADS are copied by standard Microsoft utilities between NTFS volumes. ADS can be used by an attacker or intruder to hide tools, scripts, and data from detection by normal system utilities. Many anti-virus programs do not check for or scan ADS. Windows Vista does have a switch (-R) on the command line DIR command that will display alternate streams.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-69](/wiki/p/weakness/CWE-69), [CWE-212](/wiki/p/weakness/CWE-212)

## Prerequisites

- The target must be running the Microsoft NTFS file system.

## Mitigations

- Design: Use FAT file systems which do not support Alternate Data Streams.
- Implementation: Use Vista dir with the -R switch or utility to find Alternate Data Streams and take appropriate action with those discovered.
- Implementation: Use products that are Alternate Data Stream aware for virus scanning and system security operations.

## Source

- [MITRE CAPEC CAPEC-168](https://capec.mitre.org/data/definitions/168.html)
