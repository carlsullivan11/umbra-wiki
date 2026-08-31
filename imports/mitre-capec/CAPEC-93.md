---
slug: attack-pattern/CAPEC-93
title: "CAPEC-93 — Log Injection-Tampering-Forging"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-93]
cwe_ids: [CWE-75, CWE-117, CWE-150]
related: [weakness/CWE-75, weakness/CWE-117, weakness/CWE-150]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-93
updated_at: 2026-08-31
summary: "This attack targets the log files of the target host. The attacker injects, manipulates or forges malicious log entries in the log file, allowing them to mislead a log audit, cover traces of attack, or perform other malicious actions. The target host is not properly controlling l…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/93.html
---

# CAPEC-93: Log Injection-Tampering-Forging

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

This attack targets the log files of the target host. The attacker injects, manipulates or forges malicious log entries in the log file, allowing them to mislead a log audit, cover traces of attack, or perform other malicious actions. The target host is not properly controlling log access. As a result tainted data is resulting in the log files leading to a failure in accountability, non-repudiation and incident forensics capability.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-75](/wiki/p/weakness/CWE-75), [CWE-117](/wiki/p/weakness/CWE-117), [CWE-150](/wiki/p/weakness/CWE-150)

## Prerequisites

- The target host is logging the action and data of the user.
- The target host insufficiently protects access to the logs or logging mechanisms.

## Skills required

- Low: This attack can be as simple as adding extra characters to the logged data (e.g. username). Adding entries is typically easier than removing entries.
- Medium: A more sophisticated attack can try to defeat the input validation mechanism.

## Consequences

- Integrity: Modify Data

## Mitigations

- Carefully control access to physical log files.
- Do not allow tainted data to be written in the log file without prior input validation. An allowlist may be used to properly validate the data.
- Use synchronization to control the flow of execution.
- Use static analysis tools to identify log forging vulnerabilities.
- Avoid viewing logs with tools that may interpret control characters in the file, such as command-line shells.

## Source

- [MITRE CAPEC CAPEC-93](https://capec.mitre.org/data/definitions/93.html)
