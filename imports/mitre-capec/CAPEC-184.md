---
slug: attack-pattern/CAPEC-184
title: "CAPEC-184 — Software Integrity Attack"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-184]
cwe_ids: [CWE-494]
related: [weakness/CWE-494]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-184
updated_at: 2026-08-31
summary: "An attacker initiates a series of events designed to cause a user, program, server, or device to perform actions which undermine the integrity of software code, device data structures, or device firmware, achieving the modification of the target's integrity to achieve an insecure…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/184.html
---

# CAPEC-184: Software Integrity Attack

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Low |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker initiates a series of events designed to cause a user, program, server, or device to perform actions which undermine the integrity of software code, device data structures, or device firmware, achieving the modification of the target's integrity to achieve an insecure state.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-494](/wiki/p/weakness/CWE-494)

## Skills required

- Medium: Manual or user-assisted attacks require deceptive mechanisms to trick the user into clicking a link or downloading and installing software. Automated update attacks require the attacker to host a payload and then trigger the installation of the payload code.

## Source

- [MITRE CAPEC CAPEC-184](https://capec.mitre.org/data/definitions/184.html)
