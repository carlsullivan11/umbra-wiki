---
slug: attack-pattern/CAPEC-591
title: "CAPEC-591 — Reflected XSS"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-591]
cwe_ids: [CWE-79]
related: [weakness/CWE-79]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-591
updated_at: 2026-08-31
summary: "This type of attack is a form of Cross-Site Scripting (XSS) where a malicious script is 'reflected' off a vulnerable web application and then executed by a victim's browser. The process starts with an adversary delivering a malicious script to a victim and convincing the victim t…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/591.html
---

# CAPEC-591: Reflected XSS

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Very High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

This type of attack is a form of Cross-Site Scripting (XSS) where a malicious script is "reflected" off a vulnerable web application and then executed by a victim's browser. The process starts with an adversary delivering a malicious script to a victim and convincing the victim to send the script to the vulnerable web application.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-79](/wiki/p/weakness/CWE-79)

## Prerequisites

- An application that leverages a client-side web browser with scripting enabled.
- An application that fail to adequately sanitize or encode untrusted input.

## Skills required

- Medium: Requires the ability to write malicious scripts and embed them into HTTP requests.

## Consequences

- Confidentiality: Read Data
- Confidentiality, Authorization, Access Control: Gain Privileges
- Confidentiality, Integrity, Availability: Execute Unauthorized Commands
- Integrity: Modify Data

## Mitigations

- Use browser technologies that do not allow client-side scripting.
- Utilize strict type, character, and encoding enforcement.
- Ensure that all user-supplied input is validated before use.

## Source

- [MITRE CAPEC CAPEC-591](https://capec.mitre.org/data/definitions/591.html)
