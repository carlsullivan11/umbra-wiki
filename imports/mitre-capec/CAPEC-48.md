---
slug: attack-pattern/CAPEC-48
title: "CAPEC-48 — Passing Local Filenames to Functions That Expect a URL"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-48]
cwe_ids: [CWE-241, CWE-706]
related: [weakness/CWE-241, weakness/CWE-706]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-48
updated_at: 2026-08-31
summary: "This attack relies on client side code to access local files and resources instead of URLs. When the client browser is expecting a URL string, but instead receives a request for a local file, that execution is likely to occur in the browser process space with the browser's author…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/48.html
---

# CAPEC-48: Passing Local Filenames to Functions That Expect a URL

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

This attack relies on client side code to access local files and resources instead of URLs. When the client browser is expecting a URL string, but instead receives a request for a local file, that execution is likely to occur in the browser process space with the browser's authority to local files. The attacker can send the results of this request to the local files out to a site that they control. This attack may be used to steal sensitive authentication data (either local or remote), or to gain system profile information to launch further attacks.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-241](/wiki/p/weakness/CWE-241), [CWE-706](/wiki/p/weakness/CWE-706)

## Prerequisites

- The victim's software must not differentiate between the location and type of reference passed the client software, e.g. browser

## Skills required

- Medium: Attacker identifies known local files to exploit

## Consequences

- Confidentiality: Read Data
- Integrity: Modify Data

## Mitigations

- Implementation: Ensure all content that is delivered to client is sanitized against an acceptable content specification.
- Implementation: Ensure all configuration files and resource are either removed or protected when promoting code into production.
- Design: Use browser technologies that do not allow client side scripting.
- Implementation: Perform input validation for all remote content.
- Implementation: Perform output validation for all remote content.
- Implementation: Disable scripting languages such as JavaScript in browser

## Source

- [MITRE CAPEC CAPEC-48](https://capec.mitre.org/data/definitions/48.html)
