---
slug: attack-pattern/CAPEC-466
title: "CAPEC-466 — Leveraging Active Adversary in the Middle Attacks to Bypass Same Origin Policy"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-466]
cwe_ids: [CWE-300]
related: [weakness/CWE-300]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-466
updated_at: 2026-08-31
summary: "An attacker leverages an adversary in the middle attack (CAPEC-94) in order to bypass the same origin policy protection in the victim's browser. This active adversary in the middle attack could be launched, for instance, when the victim is connected to a public WIFI hot spot. An …"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/466.html
---

# CAPEC-466: Leveraging Active Adversary in the Middle Attacks to Bypass Same Origin Policy

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker leverages an adversary in the middle attack (CAPEC-94) in order to bypass the same origin policy protection in the victim's browser. This active adversary in the middle attack could be launched, for instance, when the victim is connected to a public WIFI hot spot. An attacker is able to intercept requests and responses between the victim's browser and some non-sensitive website that does not use TLS.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-300](/wiki/p/weakness/CWE-300)

## Prerequisites

- The victim and the attacker are both in an environment where an active adversary in the middle attack is possible (e.g., public WIFI hot spot)The victim visits at least one website that does not use TLS / SSL

## Skills required

- Low: Ability to intercept and modify requests / responses
- Medium: Ability to create iFrame and JavaScript code that would initiate unauthorized requests to sensitive sites from the victim's browser
- Medium: Solid understanding of the HTTP protocol

## Consequences

- Confidentiality: Read Data
- Authorization: Execute Unauthorized Commands

## Mitigations

- Design: Tunnel communications through a secure proxy
- Design: Trust level separation for privileged / non privileged interactions (e.g., two different browsers, two different users, two different operating systems, two different virtual machines)

## Source

- [MITRE CAPEC CAPEC-466](https://capec.mitre.org/data/definitions/466.html)
