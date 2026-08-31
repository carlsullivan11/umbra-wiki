---
slug: attack-pattern/CAPEC-657
title: "CAPEC-657 — Malicious Automated Software Update via Spoofing"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-657]
cwe_ids: [CWE-494]
mitre_ids: [T1072]
related: [weakness/CWE-494, technique/T1072]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-657
updated_at: 2026-08-31
summary: "An attackers uses identify or content spoofing to trick a client into performing an automated software update from a malicious source. A malicious automated software update that leverages spoofing can include content or identity spoofing as well as protocol spoofing. Content or i…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/657.html
---

# CAPEC-657: Malicious Automated Software Update via Spoofing

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attackers uses identify or content spoofing to trick a client into performing an automated software update from a malicious source. A malicious automated software update that leverages spoofing can include content or identity spoofing as well as protocol spoofing. Content or identity spoofing attacks can trigger updates in software by embedding scripted mechanisms within a malicious web page, which masquerades as a legitimate update source. Scripting mechanisms communicate with software components and trigger updates from locations specified by the attackers' server. The result is the client believing there is a legitimate software update available but instead downloading a malicious update from the attacker.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-494](/wiki/p/weakness/CWE-494)

**ATT&CK techniques:** [T1072](/wiki/p/technique/T1072)

## Consequences

- Access Control, Availability, Confidentiality: Execute Unauthorized Commands

## Source

- [MITRE CAPEC CAPEC-657](https://capec.mitre.org/data/definitions/657.html)
