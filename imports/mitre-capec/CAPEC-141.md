---
slug: attack-pattern/CAPEC-141
title: "CAPEC-141 — Cache Poisoning"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-141]
cwe_ids: [CWE-345, CWE-346, CWE-348, CWE-349]
mitre_ids: [T1557.002]
related: [weakness/CWE-345, weakness/CWE-346, weakness/CWE-348, weakness/CWE-349, technique/T1557.002]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-141
updated_at: 2026-08-31
summary: "An attacker exploits the functionality of cache technologies to cause specific data to be cached that aids the attackers' objectives. This describes any attack whereby an attacker places incorrect or harmful material in cache. The targeted cache can be an application's cache (e.g…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/141.html
---

# CAPEC-141: Cache Poisoning

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker exploits the functionality of cache technologies to cause specific data to be cached that aids the attackers' objectives. This describes any attack whereby an attacker places incorrect or harmful material in cache. The targeted cache can be an application's cache (e.g. a web browser cache) or a public cache (e.g. a DNS or ARP cache). Until the cache is refreshed, most applications or clients will treat the corrupted cache value as valid. This can lead to a wide range of exploits including redirecting web browsers towards sites that install malware and repeatedly incorrect calculations based on the incorrect value.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-345](/wiki/p/weakness/CWE-345), [CWE-346](/wiki/p/weakness/CWE-346), [CWE-348](/wiki/p/weakness/CWE-348), [CWE-349](/wiki/p/weakness/CWE-349)

**ATT&CK techniques:** [T1557.002](/wiki/p/technique/T1557.002)

## Prerequisites

- The attacker must be able to modify the value stored in a cache to match a desired value.
- The targeted application must not be able to detect the illicit modification of the cache and must trust the cache value in its calculations.

## Skills required

- Medium: To overwrite/modify targeted cache

## Mitigations

- Configuration: Disable client side caching.
- Implementation: Listens for query replies on a network, and sends a notification via email when an entry changes.

## Source

- [MITRE CAPEC CAPEC-141](https://capec.mitre.org/data/definitions/141.html)
