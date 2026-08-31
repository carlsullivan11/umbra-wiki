---
slug: attack-pattern/CAPEC-506
title: "CAPEC-506 — Tapjacking"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-506]
cwe_ids: [CWE-1021]
related: [weakness/CWE-1021]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-506
updated_at: 2026-08-31
summary: "An adversary, through a previously installed malicious application, displays an interface that misleads the user and convinces them to tap on an attacker desired location on the screen. This is often accomplished by overlaying one screen on top of another while giving the appeara…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/506.html
---

# CAPEC-506: Tapjacking

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Low |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary, through a previously installed malicious application, displays an interface that misleads the user and convinces them to tap on an attacker desired location on the screen. This is often accomplished by overlaying one screen on top of another while giving the appearance of a single interface. There are two main techniques used to accomplish this. The first is to leverage transparent properties that allow taps on the screen to pass through the visible application to an application running in the background. The second is to strategically place a small object (e.g., a button or text field) on top of the visible screen and make it appear to be a part of the underlying application. In both cases, the user is convinced to tap on the screen but does not realize the application that they are interacting with.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-1021](/wiki/p/weakness/CWE-1021)

## Prerequisites

- This pattern of attack requires the ability to execute a malicious application on the user's device. This malicious application is used to present the interface to the user and make the attack possible.

## Source

- [MITRE CAPEC CAPEC-506](https://capec.mitre.org/data/definitions/506.html)
