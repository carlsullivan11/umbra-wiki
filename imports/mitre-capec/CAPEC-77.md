---
slug: attack-pattern/CAPEC-77
title: "CAPEC-77 — Manipulating User-Controlled Variables"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-77]
cwe_ids: [CWE-15, CWE-94, CWE-96, CWE-285, CWE-302, CWE-473, CWE-1321]
related: [weakness/CWE-15, weakness/CWE-94, weakness/CWE-96, weakness/CWE-285, weakness/CWE-302, weakness/CWE-473, weakness/CWE-1321]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-77
updated_at: 2026-08-31
summary: "This attack targets user controlled variables (DEBUG=1, PHP Globals, and So Forth). An adversary can override variables leveraging user-supplied, untrusted query variables directly used on the application server without any data sanitization. In extreme cases, the adversary can c…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/77.html
---

# CAPEC-77: Manipulating User-Controlled Variables

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Very High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

This attack targets user controlled variables (DEBUG=1, PHP Globals, and So Forth). An adversary can override variables leveraging user-supplied, untrusted query variables directly used on the application server without any data sanitization. In extreme cases, the adversary can change variables controlling the business logic of the application. For instance, in languages like PHP, a number of poorly set default configurations may allow the user to override variables.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-15](/wiki/p/weakness/CWE-15), [CWE-94](/wiki/p/weakness/CWE-94), [CWE-96](/wiki/p/weakness/CWE-96), [CWE-285](/wiki/p/weakness/CWE-285), [CWE-302](/wiki/p/weakness/CWE-302), [CWE-473](/wiki/p/weakness/CWE-473), [CWE-1321](/wiki/p/weakness/CWE-1321)

## Prerequisites

- A variable consumed by the application server is exposed to the client.
- A variable consumed by the application server can be overwritten by the user.
- The application server trusts user supplied data to compute business logic.
- The application server does not perform proper input validation.

## Skills required

- Low: The malicious user can easily try some well-known global variables and find one which matches.
- Medium: The adversary can use automated tools to probe for variables that they can control.

## Consequences

- Integrity: Modify Data
- Confidentiality, Integrity, Availability: Execute Unauthorized Commands
- Confidentiality: Read Data
- Confidentiality, Access Control, Authorization: Gain Privileges

## Mitigations

- Do not allow override of global variables and do Not Trust Global Variables. If the register_globals option is enabled, PHP will create global variables for each GET, POST, and cookie variable included in the HTTP request. This means that a malicious user may be able to set variables unexpectedly. For instance make sure that the server setting for PHP does not expose global variables.
- A software system should be reluctant to trust variables that have been initialized outside of its trust boundary. Ensure adequate checking is performed when relying on input from outside a trust boundary.
- Separate the presentation layer and the business logic layer. Variables at the business logic layer should not be exposed at the presentation layer. This is to prevent computation of business logic from user controlled input data.
- Use encapsulation when declaring your variables. This is to lower the exposure of your variables.
- Assume all input is malicious. Create an allowlist that defines all valid input to the software system based on the requirements specifications. Input that does not match against the allowlist should be rejected by the program.

## Source

- [MITRE CAPEC CAPEC-77](https://capec.mitre.org/data/definitions/77.html)
