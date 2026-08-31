---
slug: attack-pattern/CAPEC-170
title: "CAPEC-170 — Web Application Fingerprinting"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-170]
cwe_ids: [CWE-497]
related: [weakness/CWE-497]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-170
updated_at: 2026-08-31
summary: "An attacker sends a series of probes to a web application in order to elicit version-dependent and type-dependent behavior that assists in identifying the target. An attacker could learn information such as software versions, error pages, and response headers, variations in imple…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/170.html
---

# CAPEC-170: Web Application Fingerprinting

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Low |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker sends a series of probes to a web application in order to elicit version-dependent and type-dependent behavior that assists in identifying the target. An attacker could learn information such as software versions, error pages, and response headers, variations in implementations of the HTTP protocol, directory structures, and other similar information about the targeted service. This information can then be used by an attacker to formulate a targeted attack plan. While web application fingerprinting is not intended to be damaging (although certain activities, such as network scans, can sometimes cause disruptions to vulnerable applications inadvertently) it may often pave the way for more damaging attacks.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-497](/wiki/p/weakness/CWE-497)

## Prerequisites

- Any web application can be fingerprinted. However, some configuration choices can limit the useful information an attacker may collect during a fingerprinting attack.

## Skills required

- Low: Attacker knows how to send HTTP request, SQL query to a web application.

## Consequences

- Confidentiality: Other

## Mitigations

- Implementation: Obfuscate server fields of HTTP response.
- Implementation: Hide inner ordering of HTTP response header.
- Implementation: Customizing HTTP error codes such as 404 or 500.
- Implementation: Hide URL file extension.
- Implementation: Hide HTTP response header software information filed.
- Implementation: Hide cookie's software information filed.
- Implementation: Appropriately deal with error messages.
- Implementation: Obfuscate database type in Database API's error message.

## Source

- [MITRE CAPEC CAPEC-170](https://capec.mitre.org/data/definitions/170.html)
