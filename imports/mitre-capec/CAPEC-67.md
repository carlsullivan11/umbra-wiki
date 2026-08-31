---
slug: attack-pattern/CAPEC-67
title: "CAPEC-67 — String Format Overflow in syslog()"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-67]
cwe_ids: [CWE-20, CWE-74, CWE-120, CWE-134, CWE-680, CWE-697]
related: [weakness/CWE-20, weakness/CWE-74, weakness/CWE-120, weakness/CWE-134, weakness/CWE-680, weakness/CWE-697]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-67
updated_at: 2026-08-31
summary: "This attack targets applications and software that uses the syslog() function insecurely. If an application does not explicitely use a format string parameter in a call to syslog(), user input can be placed in the format string parameter leading to a format string injection attac…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/67.html
---

# CAPEC-67: String Format Overflow in syslog()

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Very High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

This attack targets applications and software that uses the syslog() function insecurely. If an application does not explicitely use a format string parameter in a call to syslog(), user input can be placed in the format string parameter leading to a format string injection attack. Adversaries can then inject malicious format string commands into the function call leading to a buffer overflow. There are many reported software vulnerabilities with the root cause being a misuse of the syslog() function.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-20](/wiki/p/weakness/CWE-20), [CWE-74](/wiki/p/weakness/CWE-74), [CWE-120](/wiki/p/weakness/CWE-120), [CWE-134](/wiki/p/weakness/CWE-134), [CWE-680](/wiki/p/weakness/CWE-680), [CWE-697](/wiki/p/weakness/CWE-697)

## Prerequisites

- The Syslog function is used without specifying a format string argument, allowing user input to be placed direct into the function call as a format string.

## Consequences

- Confidentiality, Integrity, Availability: Execute Unauthorized Commands
- Availability: Unreliable Execution
- Confidentiality, Access Control, Authorization: Gain Privileges
- Integrity: Modify Data

## Mitigations

- The code should be reviewed for misuse of the Syslog function call. Manual or automated code review can be used. The reviewer needs to ensure that all format string functions are passed a static string which cannot be controlled by the user and that the proper number of arguments are always sent to that function as well. If at all possible, do not use the %n operator in format strings. The following code shows a correct usage of Syslog(): syslog(LOG_ERR, "%s", cmdBuf); The following code shows a vulnerable usage of Syslog(): syslog(LOG_ERR, cmdBuf); // the buffer cmdBuff is taking user supplied data.

## Source

- [MITRE CAPEC CAPEC-67](https://capec.mitre.org/data/definitions/67.html)
