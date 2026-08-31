---
slug: attack-pattern/CAPEC-139
title: "CAPEC-139 — Relative Path Traversal"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-139]
cwe_ids: [CWE-23]
related: [weakness/CWE-23]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-139
updated_at: 2026-08-31
summary: "An attacker exploits a weakness in input validation on the target by supplying a specially constructed path utilizing dot and slash characters for the purpose of obtaining access to arbitrary files or resources. An attacker modifies a known path on the target in order to reach ma…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/139.html
---

# CAPEC-139: Relative Path Traversal

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker exploits a weakness in input validation on the target by supplying a specially constructed path utilizing dot and slash characters for the purpose of obtaining access to arbitrary files or resources. An attacker modifies a known path on the target in order to reach material that is not available through intended channels. These attacks normally involve adding additional path separators (/ or \) and/or dots (.), or encodings thereof, in various combinations in order to reach parent directories or entirely separate trees of the target's directory structure.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-23](/wiki/p/weakness/CWE-23)

## Prerequisites

- The target application must accept a string as user input, fail to sanitize combinations of characters in the input that have a special meaning in the context of path navigation, and insert the user-supplied string into path navigation commands.

## Skills required

- Low: To inject the malicious payload in a web page
- High: To bypass non trivial filters in the application

## Consequences

- Integrity: Modify Data
- Confidentiality: Read Data
- Confidentiality, Integrity, Availability: Execute Unauthorized Commands
- Access Control: Bypass Protection Mechanism
- Availability: Unreliable Execution

## Mitigations

- Design: Input validation. Assume that user inputs are malicious. Utilize strict type, character, and encoding enforcement
- Implementation: Perform input validation for all remote content, including remote and user-generated content.
- Implementation: Validate user input by only accepting known good. Ensure all content that is delivered to client is sanitized against an acceptable content specification -- using an allowlist approach.
- Implementation: Prefer working without user input when using file system calls
- Implementation: Use indirect references rather than actual file names.
- Implementation: Use possible permissions on file access when developing and deploying web applications.

## Source

- [MITRE CAPEC CAPEC-139](https://capec.mitre.org/data/definitions/139.html)
