---
slug: attack-pattern/CAPEC-134
title: "CAPEC-134 — Email Injection"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-134]
cwe_ids: [CWE-150]
related: [weakness/CWE-150]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-134
updated_at: 2026-08-31
summary: "An adversary manipulates the headers and content of an email message by injecting data via the use of delimiter characters native to the protocol."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/134.html
---

# CAPEC-134: Email Injection

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary manipulates the headers and content of an email message by injecting data via the use of delimiter characters native to the protocol.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-150](/wiki/p/weakness/CWE-150)

## Prerequisites

- The target application must allow the user to send email to some recipient, to specify the content at least one header field in the message, and must fail to sanitize against the injection of command separators.
- The adversary must have the ability to access the target mail application.

## Source

- [MITRE CAPEC CAPEC-134](https://capec.mitre.org/data/definitions/134.html)
