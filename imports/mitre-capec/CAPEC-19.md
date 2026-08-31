---
slug: attack-pattern/CAPEC-19
title: "CAPEC-19 — Embedding Scripts within Scripts"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-19]
cwe_ids: [CWE-284]
mitre_ids: [T1027.009, T1546.004, T1546.016]
related: [weakness/CWE-284, technique/T1027.009, technique/T1546.004, technique/T1546.016]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-19
updated_at: 2026-08-31
summary: "An adversary leverages the capability to execute their own script by embedding it within other scripts that the target software is likely to execute due to programs' vulnerabilities that are brought on by allowing remote hosts to execute scripts."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/19.html
---

# CAPEC-19: Embedding Scripts within Scripts

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary leverages the capability to execute their own script by embedding it within other scripts that the target software is likely to execute due to programs' vulnerabilities that are brought on by allowing remote hosts to execute scripts.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-284](/wiki/p/weakness/CWE-284)

**ATT&CK techniques:** [T1027.009](/wiki/p/technique/T1027.009), [T1546.004](/wiki/p/technique/T1546.004), [T1546.016](/wiki/p/technique/T1546.016)

## Prerequisites

- Target software must be able to execute scripts, and also grant the adversary privilege to write/upload scripts.

## Skills required

- Low: To load malicious script into open, e.g. world writable directory
- Medium: Executing remote scripts on host and collecting output

## Consequences

- Confidentiality, Integrity, Availability: Execute Unauthorized Commands
- Confidentiality, Access Control, Authorization: Gain Privileges

## Mitigations

- Use browser technologies that do not allow client side scripting.
- Utilize strict type, character, and encoding enforcement.
- Server side developers should not proxy content via XHR or other means. If a HTTP proxy for remote content is setup on the server side, the client's browser has no way of discerning where the data is originating from.
- Ensure all content that is delivered to client is sanitized against an acceptable content specification.
- Perform input validation for all remote content.
- Perform output validation for all remote content.
- Disable scripting languages such as JavaScript in browser
- Session tokens for specific host

## Source

- [MITRE CAPEC CAPEC-19](https://capec.mitre.org/data/definitions/19.html)
