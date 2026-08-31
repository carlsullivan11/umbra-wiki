---
slug: attack-pattern/CAPEC-267
title: "CAPEC-267 — Leverage Alternate Encoding"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-267]
cwe_ids: [CWE-20, CWE-73, CWE-74, CWE-172, CWE-173, CWE-180, CWE-181, CWE-692, CWE-697]
mitre_ids: [T1027]
related: [weakness/CWE-20, weakness/CWE-73, weakness/CWE-74, weakness/CWE-172, weakness/CWE-173, weakness/CWE-180, weakness/CWE-181, weakness/CWE-692, weakness/CWE-697, technique/T1027]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-267
updated_at: 2026-08-31
summary: "An adversary leverages the possibility to encode potentially harmful input or content used by applications such that the applications are ineffective at validating this encoding standard."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/267.html
---

# CAPEC-267: Leverage Alternate Encoding

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary leverages the possibility to encode potentially harmful input or content used by applications such that the applications are ineffective at validating this encoding standard.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-20](/wiki/p/weakness/CWE-20), [CWE-73](/wiki/p/weakness/CWE-73), [CWE-74](/wiki/p/weakness/CWE-74), [CWE-172](/wiki/p/weakness/CWE-172), [CWE-173](/wiki/p/weakness/CWE-173), [CWE-180](/wiki/p/weakness/CWE-180), [CWE-181](/wiki/p/weakness/CWE-181), [CWE-692](/wiki/p/weakness/CWE-692), [CWE-697](/wiki/p/weakness/CWE-697)

**ATT&CK techniques:** [T1027](/wiki/p/technique/T1027)

## Prerequisites

- The application's decoder accepts and interprets encoded characters. Data canonicalization, input filtering and validating is not done properly leaving the door open to harmful characters for the target host.

## Skills required

- Low: An adversary can inject different representation of a filtered character in a different encoding.
- Medium: An adversary may craft subtle encoding of input data by using the knowledge that they have gathered about the target host.

## Consequences

- Integrity: Modify Data
- Confidentiality: Read Data
- Authorization: Execute Unauthorized Commands
- Accountability, Authentication, Authorization, Non-Repudiation: Gain Privileges
- Access Control, Authorization: Bypass Protection Mechanism
- Availability: Unreliable Execution, Resource Consumption

## Mitigations

- Assume all input might use an improper representation. Use canonicalized data inside the application; all data must be converted into the representation used inside the application (UTF-8, UTF-16, etc.)
- Assume all input is malicious. Create an allowlist that defines all valid input to the software system based on the requirements specifications. Input that does not match against the allowlist should not be permitted to enter into the system. Test your decoding process against malicious input.

## Source

- [MITRE CAPEC CAPEC-267](https://capec.mitre.org/data/definitions/267.html)
