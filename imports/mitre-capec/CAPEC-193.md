---
slug: attack-pattern/CAPEC-193
title: "CAPEC-193 — PHP Remote File Inclusion"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-193]
cwe_ids: [CWE-80, CWE-98]
related: [weakness/CWE-80, weakness/CWE-98]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-193
updated_at: 2026-08-31
summary: "In this pattern the adversary is able to load and execute arbitrary code remotely available from the application. This is usually accomplished through an insecurely configured PHP runtime environment and an improperly sanitized 'include' or 'require' call, which the user can then…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/193.html
---

# CAPEC-193: PHP Remote File Inclusion

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

In this pattern the adversary is able to load and execute arbitrary code remotely available from the application. This is usually accomplished through an insecurely configured PHP runtime environment and an improperly sanitized "include" or "require" call, which the user can then control to point to any web-accessible file. This allows adversaries to hijack the targeted application and force it to execute their own instructions.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-80](/wiki/p/weakness/CWE-80), [CWE-98](/wiki/p/weakness/CWE-98)

## Prerequisites

- Target application server must allow remote files to be included in the "require", "include", etc. PHP directives
- The adversary must have the ability to make HTTP requests to the target web application.

## Skills required

- Low: To inject the malicious payload in a web page
- Medium: To bypass filters in the application

## Consequences

- Integrity: Modify Data
- Confidentiality: Read Data
- Authorization: Execute Unauthorized Commands
- Accountability, Authentication, Authorization, Non-Repudiation: Gain Privileges
- Access Control, Authorization: Bypass Protection Mechanism

## Mitigations

- Implementation: Perform input validation for all remote content, including remote and user-generated content
- Implementation: Only allow known files to be included (allowlist)
- Implementation: Make use of indirect references passed in URL parameters instead of file names
- Configuration: Ensure that remote scripts cannot be include in the "include" or "require" PHP directives

## Source

- [MITRE CAPEC CAPEC-193](https://capec.mitre.org/data/definitions/193.html)
