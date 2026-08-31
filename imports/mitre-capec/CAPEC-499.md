---
slug: attack-pattern/CAPEC-499
title: "CAPEC-499 — Android Intent Intercept"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-499]
cwe_ids: [CWE-925]
related: [weakness/CWE-925]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-499
updated_at: 2026-08-31
summary: "An adversary, through a previously installed malicious application, intercepts messages from a trusted Android-based application in an attempt to achieve a variety of different objectives including denial of service, information disclosure, and data injection. An implicit intent …"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/499.html
---

# CAPEC-499: Android Intent Intercept

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | — |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary, through a previously installed malicious application, intercepts messages from a trusted Android-based application in an attempt to achieve a variety of different objectives including denial of service, information disclosure, and data injection. An implicit intent sent from a trusted application can be received by any application that has declared an appropriate intent filter. If the intent is not protected by a permission that the malicious application lacks, then the attacker can gain access to the data contained within the intent. Further, the intent can be either blocked from reaching the intended destination, or modified and potentially forwarded along.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-925](/wiki/p/weakness/CWE-925)

## Prerequisites

- An adversary must be able install a purpose built malicious application onto the Android device and convince the user to execute it. The malicious application is used to intercept implicit intents.

## Consequences

- Confidentiality: Read Data
- Integrity: Modify Data
- Availability: Resource Consumption

## Mitigations

- To mitigate this type of an attack, explicit intents should be used whenever sensitive data is being sent. An explicit intent is delivered to a specific application as declared within the intent, whereas the Android operating system determines who receives an implicit intent which could potentially be a malicious application. If an implicit intent must be used, then it should be assumed that the intent will be received by an unknown application and any response should be treated accordingly. Implicit intents should never be used for inter-application communication.

## Source

- [MITRE CAPEC CAPEC-499](https://capec.mitre.org/data/definitions/499.html)
