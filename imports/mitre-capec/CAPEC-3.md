---
slug: attack-pattern/CAPEC-3
title: "CAPEC-3 — Using Leading 'Ghost' Character Sequences to Bypass Input Filters"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-3]
cwe_ids: [CWE-20, CWE-41, CWE-74, CWE-172, CWE-173, CWE-179, CWE-180, CWE-181, CWE-183, CWE-184, CWE-697, CWE-707]
related: [weakness/CWE-20, weakness/CWE-41, weakness/CWE-74, weakness/CWE-172, weakness/CWE-173, weakness/CWE-179, weakness/CWE-180, weakness/CWE-181, weakness/CWE-183, weakness/CWE-184, weakness/CWE-697, weakness/CWE-707]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-3
updated_at: 2026-08-31
summary: "Some APIs will strip certain leading characters from a string of parameters. An adversary can intentionally introduce leading 'ghost' characters (extra characters that don't affect the validity of the request at the API layer) that enable the input to pass the filters and therefo…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/3.html
---

# CAPEC-3: Using Leading 'Ghost' Character Sequences to Bypass Input Filters

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

Some APIs will strip certain leading characters from a string of parameters. An adversary can intentionally introduce leading "ghost" characters (extra characters that don't affect the validity of the request at the API layer) that enable the input to pass the filters and therefore process the adversary's input. This occurs when the targeted API will accept input data in several syntactic forms and interpret it in the equivalent semantic way, while the filter does not take into account the full spectrum of the syntactic forms acceptable to the targeted API.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-20](/wiki/p/weakness/CWE-20), [CWE-41](/wiki/p/weakness/CWE-41), [CWE-74](/wiki/p/weakness/CWE-74), [CWE-172](/wiki/p/weakness/CWE-172), [CWE-173](/wiki/p/weakness/CWE-173), [CWE-179](/wiki/p/weakness/CWE-179), [CWE-180](/wiki/p/weakness/CWE-180), [CWE-181](/wiki/p/weakness/CWE-181), [CWE-183](/wiki/p/weakness/CWE-183), [CWE-184](/wiki/p/weakness/CWE-184), [CWE-697](/wiki/p/weakness/CWE-697), [CWE-707](/wiki/p/weakness/CWE-707)

## Prerequisites

- The targeted API must ignore the leading ghost characters that are used to get past the filters for the semantics to be the same.

## Skills required

- Medium: The ability to make an API request, and knowledge of "ghost" characters that will not be filtered by any input validation. These "ghost" characters must be known to not affect the way in which the request will be interpreted.

## Consequences

- Confidentiality, Access Control, Authorization: Gain Privileges
- Integrity: Modify Data

## Mitigations

- Use an allowlist rather than a denylist input validation.
- Canonicalize all data prior to validation.
- Take an iterative approach to input validation (defense in depth).

## Source

- [MITRE CAPEC CAPEC-3](https://capec.mitre.org/data/definitions/3.html)
