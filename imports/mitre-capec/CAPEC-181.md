---
slug: attack-pattern/CAPEC-181
title: "CAPEC-181 — Flash File Overlay"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-181]
cwe_ids: [CWE-1021]
related: [weakness/CWE-1021]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-181
updated_at: 2026-08-31
summary: "An attacker creates a transparent overlay using flash in order to intercept user actions for the purpose of performing a clickjacking attack. In this technique, the Flash file provides a transparent overlay over HTML content. Because the Flash application is on top of the content…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/181.html
---

# CAPEC-181: Flash File Overlay

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker creates a transparent overlay using flash in order to intercept user actions for the purpose of performing a clickjacking attack. In this technique, the Flash file provides a transparent overlay over HTML content. Because the Flash application is on top of the content, user actions, such as clicks, are caught by the Flash application rather than the underlying HTML. The action is then interpreted by the overlay to perform the actions the attacker wishes.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-1021](/wiki/p/weakness/CWE-1021)

## Prerequisites

- The victim must be tricked into navigating to the attackers' decoy site and performing the actions on the decoy page.
- The victim's browser must support invisible Flash overlays.

## Source

- [MITRE CAPEC CAPEC-181](https://capec.mitre.org/data/definitions/181.html)
