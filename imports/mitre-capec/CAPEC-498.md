---
slug: attack-pattern/CAPEC-498
title: "CAPEC-498 — Probe iOS Screenshots"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-498]
cwe_ids: [CWE-359]
related: [weakness/CWE-359]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-498
updated_at: 2026-08-31
summary: "An adversary examines screenshot images created by iOS in an attempt to obtain sensitive information. This attack targets temporary screenshots created by the underlying OS while the application remains open in the background."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/498.html
---

# CAPEC-498: Probe iOS Screenshots

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | — |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary examines screenshot images created by iOS in an attempt to obtain sensitive information. This attack targets temporary screenshots created by the underlying OS while the application remains open in the background.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-359](/wiki/p/weakness/CWE-359)

## Prerequisites

- This type of an attack requires physical access to a device to either excavate the image files (potentially by leveraging a Jailbreak) or view the screenshots through the multitasking switcher (by double tapping the home button on the device).

## Mitigations

- To mitigate this type of an attack, an application that may display sensitive information should clear the screen contents before a screenshot is taken. This can be accomplished by setting the key window's hidden property to YES. This code to hide the contents should be placed in both the applicationWillResignActive() and applicationDidEnterBackground() methods.

## Source

- [MITRE CAPEC CAPEC-498](https://capec.mitre.org/data/definitions/498.html)
