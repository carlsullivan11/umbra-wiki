---
slug: attack-pattern/CAPEC-467
title: "CAPEC-467 — Cross Site Identification"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-467]
cwe_ids: [CWE-352, CWE-359]
related: [weakness/CWE-352, weakness/CWE-359]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-467
updated_at: 2026-08-31
summary: "An attacker harvests identifying information about a victim via an active session that the victim's browser has with a social networking site. A victim may have the social networking site open in one tab or perhaps is simply using the 'remember me' feature to keep their session w…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/467.html
---

# CAPEC-467: Cross Site Identification

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Low |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker harvests identifying information about a victim via an active session that the victim's browser has with a social networking site. A victim may have the social networking site open in one tab or perhaps is simply using the "remember me" feature to keep their session with the social networking site active. An attacker induces a payload to execute in the victim's browser that transparently to the victim initiates a request to the social networking site (e.g., via available social network site APIs) to retrieve identifying information about a victim. While some of this information may be public, the attacker is able to harvest this information in context and may use it for further attacks on the user (e.g., spear phishing).

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-352](/wiki/p/weakness/CWE-352), [CWE-359](/wiki/p/weakness/CWE-359)

## Prerequisites

- The victim has an active session with the social networking site.

## Skills required

- High: An attacker should be able to create a payload and deliver it to the victim's browser.
- Medium: An attacker needs to know how to interact with various social networking sites (e.g., via available APIs) to request information and how to send the harvested data back to the attacker.

## Mitigations

- Usage: Users should always explicitly log out from the social networking sites when done using them.
- Usage: Users should not open other tabs in the browser when using a social networking site.

## Source

- [MITRE CAPEC CAPEC-467](https://capec.mitre.org/data/definitions/467.html)
