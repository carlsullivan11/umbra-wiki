---
slug: attack-pattern/CAPEC-71
title: "CAPEC-71 — Using Unicode Encoding to Bypass Validation Logic"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-71]
cwe_ids: [CWE-20, CWE-74, CWE-172, CWE-173, CWE-176, CWE-179, CWE-180, CWE-183, CWE-184, CWE-692, CWE-697]
related: [weakness/CWE-20, weakness/CWE-74, weakness/CWE-172, weakness/CWE-173, weakness/CWE-176, weakness/CWE-179, weakness/CWE-180, weakness/CWE-183, weakness/CWE-184, weakness/CWE-692, weakness/CWE-697]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-71
updated_at: 2026-08-31
summary: "An attacker may provide a Unicode string to a system component that is not Unicode aware and use that to circumvent the filter or cause the classifying mechanism to fail to properly understanding the request. That may allow the attacker to slip malicious data past the content fil…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/71.html
---

# CAPEC-71: Using Unicode Encoding to Bypass Validation Logic

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker may provide a Unicode string to a system component that is not Unicode aware and use that to circumvent the filter or cause the classifying mechanism to fail to properly understanding the request. That may allow the attacker to slip malicious data past the content filter and/or possibly cause the application to route the request incorrectly.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-20](/wiki/p/weakness/CWE-20), [CWE-74](/wiki/p/weakness/CWE-74), [CWE-172](/wiki/p/weakness/CWE-172), [CWE-173](/wiki/p/weakness/CWE-173), [CWE-176](/wiki/p/weakness/CWE-176), [CWE-179](/wiki/p/weakness/CWE-179), [CWE-180](/wiki/p/weakness/CWE-180), [CWE-183](/wiki/p/weakness/CWE-183), [CWE-184](/wiki/p/weakness/CWE-184), [CWE-692](/wiki/p/weakness/CWE-692), [CWE-697](/wiki/p/weakness/CWE-697)

## Prerequisites

- Filtering is performed on data that has not be properly canonicalized.

## Skills required

- Medium: An attacker needs to understand Unicode encodings and have an idea (or be able to find out) what system components may not be Unicode aware.

## Consequences

- Confidentiality, Access Control, Authorization: Bypass Protection Mechanism
- Confidentiality, Integrity, Availability: Execute Unauthorized Commands
- Integrity: Modify Data
- Availability: Unreliable Execution

## Mitigations

- Ensure that the system is Unicode aware and can properly process Unicode data. Do not make an assumption that data will be in ASCII.
- Ensure that filtering or input validation is applied to canonical data.
- Assume all input is malicious. Create an allowlist that defines all valid input to the software system based on the requirements specifications. Input that does not match against the allowlist should not be permitted to enter into the system.

## Source

- [MITRE CAPEC CAPEC-71](https://capec.mitre.org/data/definitions/71.html)
