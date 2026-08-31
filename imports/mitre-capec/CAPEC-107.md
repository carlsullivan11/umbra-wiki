---
slug: attack-pattern/CAPEC-107
title: "CAPEC-107 — Cross Site Tracing"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-107]
cwe_ids: [CWE-648, CWE-693]
related: [weakness/CWE-648, weakness/CWE-693]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-107
updated_at: 2026-08-31
summary: "Cross Site Tracing (XST) enables an adversary to steal the victim's session cookie and possibly other authentication credentials transmitted in the header of the HTTP request when the victim's browser communicates to a destination system's web server."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/107.html
---

# CAPEC-107: Cross Site Tracing

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Very High |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

Cross Site Tracing (XST) enables an adversary to steal the victim's session cookie and possibly other authentication credentials transmitted in the header of the HTTP request when the victim's browser communicates to a destination system's web server.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-648](/wiki/p/weakness/CWE-648), [CWE-693](/wiki/p/weakness/CWE-693)

## Prerequisites

- HTTP TRACE is enabled on the web server
- The destination system is susceptible to XSS or an adversary can leverage some other weakness to bypass the same origin policy
- Scripting is enabled in the client's browser
- HTTP is used as the communication protocol between the server and the client

## Skills required

- Medium: Understanding of the HTTP protocol and an ability to craft a malicious script

## Consequences

- Confidentiality: Read Data
- Confidentiality, Access Control, Authorization: Gain Privileges
- Integrity: Modify Data

## Mitigations

- Administrators should disable support for HTTP TRACE at the destination's web server. Vendors should disable TRACE by default.
- Patch web browser against known security origin policy bypass exploits.

## Source

- [MITRE CAPEC CAPEC-107](https://capec.mitre.org/data/definitions/107.html)
