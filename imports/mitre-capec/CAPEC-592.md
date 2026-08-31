---
slug: attack-pattern/CAPEC-592
title: "CAPEC-592 — Stored XSS"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-592]
cwe_ids: [CWE-79]
related: [weakness/CWE-79]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-592
updated_at: 2026-08-31
summary: "An adversary utilizes a form of Cross-site Scripting (XSS) where a malicious script is persistently 'stored' within the data storage of a vulnerable web application as valid input."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/592.html
---

# CAPEC-592: Stored XSS

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Very High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary utilizes a form of Cross-site Scripting (XSS) where a malicious script is persistently "stored" within the data storage of a vulnerable web application as valid input.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-79](/wiki/p/weakness/CWE-79)

## Prerequisites

- An application that leverages a client-side web browser with scripting enabled.
- An application that fails to adequately sanitize or encode untrusted input.
- An application that stores information provided by the user in data storage of some kind.

## Skills required

- Medium: Requires the ability to write scripts of varying complexity and to inject them through user controlled fields within the application.

## Consequences

- Confidentiality: Read Data
- Confidentiality, Authorization, Access Control: Gain Privileges
- Confidentiality, Integrity, Availability: Execute Unauthorized Commands
- Integrity: Modify Data

## Mitigations

- Use browser technologies that do not allow client-side scripting.
- Utilize strict type, character, and encoding enforcement.
- Ensure that all user-supplied input is validated before being stored.

## Source

- [MITRE CAPEC CAPEC-592](https://capec.mitre.org/data/definitions/592.html)
