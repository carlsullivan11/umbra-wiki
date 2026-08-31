---
slug: attack-pattern/CAPEC-568
title: "CAPEC-568 — Capture Credentials via Keylogger"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-568]
mitre_ids: [T1056.001]
related: [technique/T1056.001]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-568
updated_at: 2026-08-31
summary: "An adversary deploys a keylogger in an effort to obtain credentials directly from a system's user. After capturing all the keystrokes made by a user, the adversary can analyze the data and determine which string are likely to be passwords or other credential related information."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/568.html
---

# CAPEC-568: Capture Credentials via Keylogger

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary deploys a keylogger in an effort to obtain credentials directly from a system's user. After capturing all the keystrokes made by a user, the adversary can analyze the data and determine which string are likely to be passwords or other credential related information.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**ATT&CK techniques:** [T1056.001](/wiki/p/technique/T1056.001)

## Prerequisites

- The ability to install the keylogger, either in person or remote.

## Mitigations

- Strong physical security can help reduce the ability of an adversary to install a keylogger.

## Source

- [MITRE CAPEC CAPEC-568](https://capec.mitre.org/data/definitions/568.html)
