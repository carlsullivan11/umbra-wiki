---
slug: attack-pattern/CAPEC-263
title: "CAPEC-263 — Force Use of Corrupted Files"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-263]
cwe_ids: [CWE-829]
related: [weakness/CWE-829]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-263
updated_at: 2026-08-31
summary: "This describes an attack where an application is forced to use a file that an attacker has corrupted. The result is often a denial of service caused by the application being unable to process the corrupted file, but other results, including the disabling of filters or access cont…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/263.html
---

# CAPEC-263: Force Use of Corrupted Files

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

This describes an attack where an application is forced to use a file that an attacker has corrupted. The result is often a denial of service caused by the application being unable to process the corrupted file, but other results, including the disabling of filters or access controls (if the application fails in an unsafe way rather than failing by locking down) or buffer overflows are possible.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-829](/wiki/p/weakness/CWE-829)

## Prerequisites

- The targeted application must utilize a configuration file that an attacker is able to corrupt. In some cases, the attacker must be able to force the (re-)reading of the corrupted file if the file is normally only consulted at startup.
- The severity of the attack hinges on how the application responds to the corrupted file. If the application detects the corruption and locks down, this may result in the denial of services provided by the application. If the application fails to detect the corruption, the result could be a more severe denial of service (crash or hang) or even an exploitable buffer overflow. If the application detects the corruption but fails in an unsafe way, this attack could result in the continuation of services but without certain security structures, such as filters or access controls. For example, if the corrupted file configures filters, an unsafe response from an application could result in simply disabling the filtering mechanisms due to the lack of usable configuration data.

## Source

- [MITRE CAPEC CAPEC-263](https://capec.mitre.org/data/definitions/263.html)
