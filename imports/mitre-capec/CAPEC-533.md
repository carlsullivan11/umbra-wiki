---
slug: attack-pattern/CAPEC-533
title: "CAPEC-533 — Malicious Manual Software Update"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-533]
cwe_ids: [CWE-494]
related: [weakness/CWE-494]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-533
updated_at: 2026-08-31
summary: "An attacker introduces malicious code to the victim's system by altering the payload of a software update, allowing for additional compromise or site disruption at the victim location. These manual, or user-assisted attacks, vary from requiring the user to download and run an exe…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/533.html
---

# CAPEC-533: Malicious Manual Software Update

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker introduces malicious code to the victim's system by altering the payload of a software update, allowing for additional compromise or site disruption at the victim location. These manual, or user-assisted attacks, vary from requiring the user to download and run an executable, to as streamlined as tricking the user to click a URL. Attacks which aim at penetrating a specific network infrastructure often rely upon secondary attack methods to achieve the desired impact. Spamming, for example, is a common method employed as an secondary attack vector. Thus the attacker has in their arsenal a choice of initial attack vectors ranging from traditional SMTP/POP/IMAP spamming and its varieties, to web-application mechanisms which commonly implement both chat and rich HTML messaging within the user interface.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-494](/wiki/p/weakness/CWE-494)

## Prerequisites

- Advanced knowledge about the download and update installation processes.
- Advanced knowledge about the deployed system and its various software subcomponents and processes.

## Skills required

- High: Able to develop malicious code that can be used on the victim's system while maintaining normal functionality.

## Mitigations

- Only accept software updates from an official source.

## Source

- [MITRE CAPEC CAPEC-533](https://capec.mitre.org/data/definitions/533.html)
