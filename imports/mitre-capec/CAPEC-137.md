---
slug: attack-pattern/CAPEC-137
title: "CAPEC-137 — Parameter Injection"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-137]
cwe_ids: [CWE-88]
related: [weakness/CWE-88]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-137
updated_at: 2026-08-31
summary: "An adversary manipulates the content of request parameters for the purpose of undermining the security of the target. Some parameter encodings use text characters as separators. For example, parameters in a HTTP GET message are encoded as name-value pairs separated by an ampersan…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/137.html
---

# CAPEC-137: Parameter Injection

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Medium |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary manipulates the content of request parameters for the purpose of undermining the security of the target. Some parameter encodings use text characters as separators. For example, parameters in a HTTP GET message are encoded as name-value pairs separated by an ampersand (&). If an attacker can supply text strings that are used to fill in these parameters, then they can inject special characters used in the encoding scheme to add or modify parameters. For example, if user input is fed directly into an HTTP GET request and the user provides the value "myInput&new_param=myValue", then the input parameter is set to myInput, but a new parameter (new_param) is also added with a value of myValue. This can significantly change the meaning of the query that is processed by the server. Any encoding scheme where parameters are identified and separated by text characters is potentially vulnerable to this attack - the HTTP GET encoding used above is just one example.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-88](/wiki/p/weakness/CWE-88)

## Prerequisites

- The target application must use a parameter encoding where separators and parameter identifiers are expressed in regular text.
- The target application must accept a string as user input, fail to sanitize characters that have a special meaning in the parameter encoding, and insert the user-supplied string in an encoding which is then processed.

## Consequences

- Integrity: Modify Data

## Mitigations

- Implement an audit log written to a separate host. In the event of a compromise, the audit log may be able to provide evidence and details of the compromise.
- Treat all user input as untrusted data that must be validated before use.

## Source

- [MITRE CAPEC CAPEC-137](https://capec.mitre.org/data/definitions/137.html)
