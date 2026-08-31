---
slug: attack-pattern/CAPEC-464
title: "CAPEC-464 — Evercookie"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-464]
cwe_ids: [CWE-359]
mitre_ids: [T1606.001]
related: [weakness/CWE-359, technique/T1606.001]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-464
updated_at: 2026-08-31
summary: "An attacker creates a very persistent cookie that stays present even after the user thinks it has been removed. The cookie is stored on the victim's machine in over ten places. When the victim clears the cookie cache via traditional means inside the browser, that operation remove…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/464.html
---

# CAPEC-464: Evercookie

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker creates a very persistent cookie that stays present even after the user thinks it has been removed. The cookie is stored on the victim's machine in over ten places. When the victim clears the cookie cache via traditional means inside the browser, that operation removes the cookie from certain places but not others. The malicious code then replicates the cookie from all of the places where it was not deleted to all of the possible storage locations once again. So the victim again has the cookie in all of the original storage locations. In other words, failure to delete the cookie in even one location will result in the cookie's resurrection everywhere. The evercookie will also persist across different browsers because certain stores (e.g., Local Shared Objects) are shared between different browsers.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-359](/wiki/p/weakness/CWE-359)

**ATT&CK techniques:** [T1606.001](/wiki/p/technique/T1606.001)

## Prerequisites

- The victim's browser is not configured to reject all cookiesThe victim visits a website that serves the attackers' evercookie

## Mitigations

- Design: Browser's design needs to be changed to limit where cookies can be stored on the client side and provide an option to clear these cookies in all places, as well as another option to stop these cookies from being written in the first place.
- Design: Safari browser's private browsing mode is currently effective against evercookies.

## Source

- [MITRE CAPEC CAPEC-464](https://capec.mitre.org/data/definitions/464.html)
