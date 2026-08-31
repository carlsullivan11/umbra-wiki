---
slug: attack-pattern/CAPEC-215
title: "CAPEC-215 — Fuzzing for application mapping"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-215]
cwe_ids: [CWE-209, CWE-532]
related: [weakness/CWE-209, weakness/CWE-532]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-215
updated_at: 2026-08-31
summary: "An attacker sends random, malformed, or otherwise unexpected messages to a target application and observes the application's log or error messages returned. The attacker does not initially know how a target will respond to individual messages but by attempting a large number of m…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/215.html
---

# CAPEC-215: Fuzzing for application mapping

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Low |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker sends random, malformed, or otherwise unexpected messages to a target application and observes the application's log or error messages returned. The attacker does not initially know how a target will respond to individual messages but by attempting a large number of message variants they may find a variant that trigger's desired behavior. In this attack, the purpose of the fuzzing is to observe the application's log and error messages, although fuzzing a target can also sometimes cause the target to enter an unstable state, causing a crash.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-209](/wiki/p/weakness/CWE-209), [CWE-532](/wiki/p/weakness/CWE-532)

## Prerequisites

- The target application must fail to sanitize incoming messages adequately before processing.

## Skills required

- Medium: Although fuzzing parameters is not difficult, and often possible with automated fuzzing tools, interpreting the error conditions and modifying the parameters so as to move further in the process of mapping the application requires detailed knowledge of target platform, the languages and packages used as well as software design.

## Consequences

- Confidentiality: Other

## Mitigations

- Design: Construct a 'code book' for error messages. When using a code book, application error messages aren't generated in string or stack trace form, but are catalogued and replaced with a unique (often integer-based) value 'coding' for the error. Such a technique will require helpdesk and hosting personnel to use a 'code book' or similar mapping to decode application errors/logs in order to respond to them normally.
- Design: wrap application functionality (preferably through the underlying framework) in an output encoding scheme that obscures or cleanses error messages to prevent such attacks. Such a technique is often used in conjunction with the above 'code book' suggestion.
- Implementation: Obfuscate server fields of HTTP response.
- Implementation: Hide inner ordering of HTTP response header.
- Implementation: Customizing HTTP error codes such as 404 or 500.
- Implementation: Hide HTTP response header software information filed.
- Implementation: Hide cookie's software information filed.
- Implementation: Obfuscate database type in Database API's error message.

## Source

- [MITRE CAPEC CAPEC-215](https://capec.mitre.org/data/definitions/215.html)
