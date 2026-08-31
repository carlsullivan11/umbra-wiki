---
slug: attack-pattern/CAPEC-472
title: "CAPEC-472 — Browser Fingerprinting"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-472]
cwe_ids: [CWE-200]
related: [weakness/CWE-200]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-472
updated_at: 2026-08-31
summary: "An attacker carefully crafts small snippets of Java Script to efficiently detect the type of browser the potential victim is using. Many web-based attacks need prior knowledge of the web browser including the version of browser to ensure successful exploitation of a vulnerability…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/472.html
---

# CAPEC-472: Browser Fingerprinting

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Low |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker carefully crafts small snippets of Java Script to efficiently detect the type of browser the potential victim is using. Many web-based attacks need prior knowledge of the web browser including the version of browser to ensure successful exploitation of a vulnerability. Having this knowledge allows an attacker to target the victim with attacks that specifically exploit known or zero day weaknesses in the type and version of the browser used by the victim. Automating this process via Java Script as a part of the same delivery system used to exploit the browser is considered more efficient as the attacker can supply a browser fingerprinting method and integrate it with exploit code, all contained in Java Script and in response to the same web page request by the browser.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-200](/wiki/p/weakness/CWE-200)

## Prerequisites

- Victim's browser visits a website that contains attacker's Java ScriptJava Script is not disabled in the victim's browser

## Mitigations

- Configuration: Disable Java Script in the browser

## Source

- [MITRE CAPEC CAPEC-472](https://capec.mitre.org/data/definitions/472.html)
