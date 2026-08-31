---
slug: attack-pattern/CAPEC-569
title: "CAPEC-569 — Collect Data as Provided by Users"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-569]
mitre_ids: [T1056]
related: [technique/T1056]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-569
updated_at: 2026-08-31
summary: "An attacker leverages a tool, device, or program to obtain specific information as provided by a user of the target system. This information is often needed by the attacker to launch a follow-on attack. This attack is different than Social Engineering as the adversary is not tric…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/569.html
---

# CAPEC-569: Collect Data as Provided by Users

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | — |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker leverages a tool, device, or program to obtain specific information as provided by a user of the target system. This information is often needed by the attacker to launch a follow-on attack. This attack is different than Social Engineering as the adversary is not tricking or deceiving the user. Instead the adversary is putting a mechanism in place that captures the information that a user legitimately enters into a system. Deploying a keylogger, performing a UAC prompt, or wrapping the Windows default credential provider are all examples of such interactions.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**ATT&CK techniques:** [T1056](/wiki/p/technique/T1056)

## Source

- [MITRE CAPEC CAPEC-569](https://capec.mitre.org/data/definitions/569.html)
