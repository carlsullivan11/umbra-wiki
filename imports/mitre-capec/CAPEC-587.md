---
slug: attack-pattern/CAPEC-587
title: "CAPEC-587 — Cross Frame Scripting (XFS)"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-587]
cwe_ids: [CWE-1021]
related: [weakness/CWE-1021]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-587
updated_at: 2026-08-31
summary: "This attack pattern combines malicious Javascript and a legitimate webpage loaded into a concealed iframe. The malicious Javascript is then able to interact with a legitimate webpage in a manner that is unknown to the user. This attack usually leverages some element of social eng…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/587.html
---

# CAPEC-587: Cross Frame Scripting (XFS)

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

This attack pattern combines malicious Javascript and a legitimate webpage loaded into a concealed iframe. The malicious Javascript is then able to interact with a legitimate webpage in a manner that is unknown to the user. This attack usually leverages some element of social engineering in that an attacker must convinces a user to visit a web page that the attacker controls.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-1021](/wiki/p/weakness/CWE-1021)

## Prerequisites

- The user's browser must have vulnerabilities in its implementation of the same-origin policy. It allows certain data in a loaded page to originate from different servers/domains.

## Consequences

- Confidentiality: Read Data

## Mitigations

- Avoid clicking on untrusted links.
- Employ techniques such as frame busting, which is a method by which developers aim to prevent their site being loaded within a frame.

## Source

- [MITRE CAPEC CAPEC-587](https://capec.mitre.org/data/definitions/587.html)
