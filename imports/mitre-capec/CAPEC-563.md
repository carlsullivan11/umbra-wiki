---
slug: attack-pattern/CAPEC-563
title: "CAPEC-563 — Add Malicious File to Shared Webroot"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-563]
cwe_ids: [CWE-284]
related: [weakness/CWE-284]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-563
updated_at: 2026-08-31
summary: "An adversaries may add malicious content to a website through the open file share and then browse to that content with a web browser to cause the server to execute the content. The malicious content will typically run under the context and permissions of the web server process, o…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/563.html
---

# CAPEC-563: Add Malicious File to Shared Webroot

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | — |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversaries may add malicious content to a website through the open file share and then browse to that content with a web browser to cause the server to execute the content. The malicious content will typically run under the context and permissions of the web server process, often resulting in local system or administrative privileges depending on how the web server is configured.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-284](/wiki/p/weakness/CWE-284)

## Mitigations

- Ensure proper permissions on directories that are accessible through a web server. Disallow remote access to the web root. Disable execution on directories within the web root. Ensure that permissions of the web server process are only what is required by not using built-in accounts and instead create specific accounts to limit unnecessary access or permissions overlap across multiple systems.

## Source

- [MITRE CAPEC CAPEC-563](https://capec.mitre.org/data/definitions/563.html)
