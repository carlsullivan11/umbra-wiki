---
slug: attack-pattern/CAPEC-462
title: "CAPEC-462 — Cross-Domain Search Timing"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-462]
cwe_ids: [CWE-208, CWE-352, CWE-385]
related: [weakness/CWE-208, weakness/CWE-352, weakness/CWE-385]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-462
updated_at: 2026-08-31
summary: "An attacker initiates cross domain HTTP / GET requests and times the server responses. The timing of these responses may leak important information on what is happening on the server. Browser's same origin policy prevents the attacker from directly reading the server responses (i…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/462.html
---

# CAPEC-462: Cross-Domain Search Timing

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker initiates cross domain HTTP / GET requests and times the server responses. The timing of these responses may leak important information on what is happening on the server. Browser's same origin policy prevents the attacker from directly reading the server responses (in the absence of any other weaknesses), but does not prevent the attacker from timing the responses to requests that the attacker issued cross domain.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-208](/wiki/p/weakness/CWE-208), [CWE-352](/wiki/p/weakness/CWE-352), [CWE-385](/wiki/p/weakness/CWE-385)

## Prerequisites

- Ability to issue GET / POST requests cross domainJava Script is enabled in the victim's browserThe victim has an active session with the site from which the attacker would like to receive informationThe victim's site does not protect search functionality with cross site request forgery (CSRF) protection

## Skills required

- Low: Some knowledge of Java Script

## Consequences

- Confidentiality: Read Data

## Mitigations

- Design: The victim's site could protect all potentially sensitive functionality (e.g. search functions) with cross site request forgery (CSRF) protection and not perform any work on behalf of forged requests
- Design: The browser's security model could be fixed to not leak timing information for cross domain requests

## Source

- [MITRE CAPEC CAPEC-462](https://capec.mitre.org/data/definitions/462.html)
