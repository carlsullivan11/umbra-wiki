---
slug: attack-pattern/CAPEC-85
title: "CAPEC-85 — AJAX Footprinting"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-85]
cwe_ids: [CWE-20, CWE-79, CWE-86, CWE-96, CWE-113, CWE-116, CWE-184, CWE-348, CWE-692]
related: [weakness/CWE-20, weakness/CWE-79, weakness/CWE-86, weakness/CWE-96, weakness/CWE-113, weakness/CWE-116, weakness/CWE-184, weakness/CWE-348, weakness/CWE-692]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-85
updated_at: 2026-08-31
summary: "This attack utilizes the frequent client-server roundtrips in Ajax conversation to scan a system. While Ajax does not open up new vulnerabilities per se, it does optimize them from an attacker point of view. A common first step for an attacker is to footprint the target environme…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/85.html
---

# CAPEC-85: AJAX Footprinting

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Low |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

This attack utilizes the frequent client-server roundtrips in Ajax conversation to scan a system. While Ajax does not open up new vulnerabilities per se, it does optimize them from an attacker point of view. A common first step for an attacker is to footprint the target environment to understand what attacks will work. Since footprinting relies on enumeration, the conversational pattern of rapid, multiple requests and responses that are typical in Ajax applications enable an attacker to look for many vulnerabilities, well-known ports, network locations and so on. The knowledge gained through Ajax fingerprinting can be used to support other attacks, such as XSS.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-20](/wiki/p/weakness/CWE-20), [CWE-79](/wiki/p/weakness/CWE-79), [CWE-86](/wiki/p/weakness/CWE-86), [CWE-96](/wiki/p/weakness/CWE-96), [CWE-113](/wiki/p/weakness/CWE-113), [CWE-116](/wiki/p/weakness/CWE-116), [CWE-184](/wiki/p/weakness/CWE-184), [CWE-348](/wiki/p/weakness/CWE-348), [CWE-692](/wiki/p/weakness/CWE-692)

## Prerequisites

- The user must allow JavaScript to execute in their browser

## Skills required

- Medium: To land and launch a script on victim's machine with appropriate footprinting logic for enumerating services and vulnerabilities in JavaScript

## Consequences

- Confidentiality: Read Data

## Mitigations

- Design: Use browser technologies that do not allow client side scripting.
- Implementation: Perform input validation for all remote content.

## Source

- [MITRE CAPEC CAPEC-85](https://capec.mitre.org/data/definitions/85.html)
