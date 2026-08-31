---
slug: attack-pattern/CAPEC-165
title: "CAPEC-165 — File Manipulation"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-165]
mitre_ids: [T1036.003]
related: [technique/T1036.003]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-165
updated_at: 2026-08-31
summary: "An attacker modifies file contents or attributes (such as extensions or names) of files in a manner to cause incorrect processing by an application. Attackers use this class of attacks to cause applications to enter unstable states, overwrite or expose sensitive information, and …"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/165.html
---

# CAPEC-165: File Manipulation

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker modifies file contents or attributes (such as extensions or names) of files in a manner to cause incorrect processing by an application. Attackers use this class of attacks to cause applications to enter unstable states, overwrite or expose sensitive information, and even execute arbitrary code with the application's privileges. This class of attacks differs from attacks on configuration information (even if file-based) in that file manipulation causes the file processing to result in non-standard behaviors, such as buffer overflows or use of the incorrect interpreter. Configuration attacks rely on the application interpreting files correctly in order to insert harmful configuration information. Likewise, resource location attacks rely on controlling an application's ability to locate files, whereas File Manipulation attacks do not require the application to look in a non-default location, although the two classes of attacks are often combined.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**ATT&CK techniques:** [T1036.003](/wiki/p/technique/T1036.003)

## Prerequisites

- The target must use the affected file without verifying its integrity.

## Source

- [MITRE CAPEC CAPEC-165](https://capec.mitre.org/data/definitions/165.html)
