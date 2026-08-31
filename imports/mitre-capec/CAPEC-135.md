---
slug: attack-pattern/CAPEC-135
title: "CAPEC-135 — Format String Injection"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-135]
cwe_ids: [CWE-20, CWE-74, CWE-134]
related: [weakness/CWE-20, weakness/CWE-74, weakness/CWE-134]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-135
updated_at: 2026-08-31
summary: "An adversary includes formatting characters in a string input field on the target application. Most applications assume that users will provide static text and may respond unpredictably to the presence of formatting character. For example, in certain functions of the C programmin…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/135.html
---

# CAPEC-135: Format String Injection

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary includes formatting characters in a string input field on the target application. Most applications assume that users will provide static text and may respond unpredictably to the presence of formatting character. For example, in certain functions of the C programming languages such as printf, the formatting character %s will print the contents of a memory location expecting this location to identify a string and the formatting character %n prints the number of DWORD written in the memory. An adversary can use this to read or write to memory locations or files, or simply to manipulate the value of the resulting text in unexpected ways. Reading or writing memory may result in program crashes and writing memory could result in the execution of arbitrary code if the adversary can write to the program stack.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-20](/wiki/p/weakness/CWE-20), [CWE-74](/wiki/p/weakness/CWE-74), [CWE-134](/wiki/p/weakness/CWE-134)

## Prerequisites

- The target application must accept a strings as user input, fail to sanitize string formatting characters in the user input, and process this string using functions that interpret string formatting characters.

## Skills required

- High: In order to discover format string vulnerabilities it takes only low skill, however, converting this discovery into a working exploit requires advanced knowledge on the part of the adversary.

## Consequences

- Integrity: Modify Data
- Confidentiality: Read Data
- Access Control: Gain Privileges
- Integrity: Execute Unauthorized Commands
- Access Control: Bypass Protection Mechanism

## Mitigations

- Limit the usage of formatting string functions.
- Strong input validation - All user-controllable input must be validated and filtered for illegal formatting characters.

## Source

- [MITRE CAPEC CAPEC-135](https://capec.mitre.org/data/definitions/135.html)
