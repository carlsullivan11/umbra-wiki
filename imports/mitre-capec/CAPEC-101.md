---
slug: attack-pattern/CAPEC-101
title: "CAPEC-101 — Server Side Include (SSI) Injection"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-101]
cwe_ids: [CWE-20, CWE-74, CWE-97]
related: [weakness/CWE-20, weakness/CWE-74, weakness/CWE-97]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-101
updated_at: 2026-08-31
summary: "An attacker can use Server Side Include (SSI) Injection to send code to a web application that then gets executed by the web server. Doing so enables the attacker to achieve similar results to Cross Site Scripting, viz., arbitrary code execution and information disclosure, albeit…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/101.html
---

# CAPEC-101: Server Side Include (SSI) Injection

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker can use Server Side Include (SSI) Injection to send code to a web application that then gets executed by the web server. Doing so enables the attacker to achieve similar results to Cross Site Scripting, viz., arbitrary code execution and information disclosure, albeit on a more limited scale, since the SSI directives are nowhere near as powerful as a full-fledged scripting language. Nonetheless, the attacker can conveniently gain access to sensitive files, such as password files, and execute shell commands.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-20](/wiki/p/weakness/CWE-20), [CWE-74](/wiki/p/weakness/CWE-74), [CWE-97](/wiki/p/weakness/CWE-97)

## Prerequisites

- A web server that supports server side includes and has them enabled
- User controllable input that can carry include directives to the web server

## Skills required

- Medium: The attacker needs to be aware of SSI technology, determine the nature of injection and be able to craft input that results in the SSI directives being executed.

## Consequences

- Confidentiality: Read Data
- Confidentiality, Integrity, Availability: Execute Unauthorized Commands

## Mitigations

- Set the OPTIONS IncludesNOEXEC in the global access.conf file or local .htaccess (Apache) file to deny SSI execution in directories that do not need them
- All user controllable input must be appropriately sanitized before use in the application. This includes omitting, or encoding, certain characters or strings that have the potential of being interpreted as part of an SSI directive
- Server Side Includes must be enabled only if there is a strong business reason to do so. Every additional component enabled on the web server increases the attack surface as well as administrative overhead

## Source

- [MITRE CAPEC CAPEC-101](https://capec.mitre.org/data/definitions/101.html)
