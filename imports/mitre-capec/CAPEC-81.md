---
slug: attack-pattern/CAPEC-81
title: "CAPEC-81 — Web Server Logs Tampering"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-81]
cwe_ids: [CWE-20, CWE-75, CWE-93, CWE-96, CWE-116, CWE-117, CWE-150, CWE-221, CWE-276, CWE-279]
related: [weakness/CWE-20, weakness/CWE-75, weakness/CWE-93, weakness/CWE-96, weakness/CWE-116, weakness/CWE-117, weakness/CWE-150, weakness/CWE-221, weakness/CWE-276, weakness/CWE-279]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-81
updated_at: 2026-08-31
summary: "Web Logs Tampering attacks involve an attacker injecting, deleting or otherwise tampering with the contents of web logs typically for the purposes of masking other malicious behavior. Additionally, writing malicious data to log files may target jobs, filters, reports, and other a…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/81.html
---

# CAPEC-81: Web Server Logs Tampering

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

Web Logs Tampering attacks involve an attacker injecting, deleting or otherwise tampering with the contents of web logs typically for the purposes of masking other malicious behavior. Additionally, writing malicious data to log files may target jobs, filters, reports, and other agents that process the logs in an asynchronous attack pattern. This pattern of attack is similar to "Log Injection-Tampering-Forging" except that in this case, the attack is targeting the logs of the web server and not the application.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-20](/wiki/p/weakness/CWE-20), [CWE-75](/wiki/p/weakness/CWE-75), [CWE-93](/wiki/p/weakness/CWE-93), [CWE-96](/wiki/p/weakness/CWE-96), [CWE-116](/wiki/p/weakness/CWE-116), [CWE-117](/wiki/p/weakness/CWE-117), [CWE-150](/wiki/p/weakness/CWE-150), [CWE-221](/wiki/p/weakness/CWE-221), [CWE-276](/wiki/p/weakness/CWE-276), [CWE-279](/wiki/p/weakness/CWE-279)

## Prerequisites

- Target server software must be a HTTP server that performs web logging.

## Skills required

- Low: To input faked entries into Web logs

## Consequences

- Integrity: Modify Data

## Mitigations

- Design: Use input validation before writing to web log
- Design: Validate all log data before it is output

## Source

- [MITRE CAPEC CAPEC-81](https://capec.mitre.org/data/definitions/81.html)
