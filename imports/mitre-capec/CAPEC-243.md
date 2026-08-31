---
slug: attack-pattern/CAPEC-243
title: "CAPEC-243 — XSS Targeting HTML Attributes"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-243]
cwe_ids: [CWE-83]
related: [weakness/CWE-83]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-243
updated_at: 2026-08-31
summary: "An adversary inserts commands to perform cross-site scripting (XSS) actions in HTML attributes. Many filters do not adequately sanitize attributes against the presence of potentially dangerous commands even if they adequately sanitize tags. For example, dangerous expressions coul…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/243.html
---

# CAPEC-243: XSS Targeting HTML Attributes

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary inserts commands to perform cross-site scripting (XSS) actions in HTML attributes. Many filters do not adequately sanitize attributes against the presence of potentially dangerous commands even if they adequately sanitize tags. For example, dangerous expressions could be inserted into a style attribute in an anchor tag, resulting in the execution of malicious code when the resulting page is rendered. If a victim is tricked into viewing the rendered page the attack proceeds like a normal XSS attack, possibly resulting in the loss of sensitive cookies or other malicious activities.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-83](/wiki/p/weakness/CWE-83)

## Prerequisites

- The target application must fail to adequately sanitize HTML attributes against the presence of dangerous commands.

## Mitigations

- Design: Use libraries and templates that minimize unfiltered input.
- Implementation: Normalize, filter and use an allowlist for all input including that which is not expected to have any scripting content.
- Implementation: The victim should configure the browser to minimize active content from untrusted sources.

## Source

- [MITRE CAPEC CAPEC-243](https://capec.mitre.org/data/definitions/243.html)
