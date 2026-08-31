---
slug: attack-pattern/CAPEC-611
title: "CAPEC-611 — BitSquatting"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-611]
related: []
provenance: imported
import_source: mitre-capec
import_id: CAPEC-611
updated_at: 2026-08-31
summary: "An adversary registers a domain name one bit different than a trusted domain. A BitSquatting attack leverages random errors in memory to direct Internet traffic to adversary-controlled destinations. BitSquatting requires no exploitation or complicated reverse engineering, and is …"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/611.html
---

# CAPEC-611: BitSquatting

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary registers a domain name one bit different than a trusted domain. A BitSquatting attack leverages random errors in memory to direct Internet traffic to adversary-controlled destinations. BitSquatting requires no exploitation or complicated reverse engineering, and is operating system and architecture agnostic. Experimental observations show that BitSquatting popular websites could redirect non-trivial amounts of Internet traffic to a malicious entity.

## Prerequisites

- An adversary requires knowledge of popular or high traffic domains, that could be used to deceive potential targets.

## Skills required

- Low: Adversaries must be able to register DNS hostnames/URL’s.

## Consequences

- Other: Other

## Mitigations

- Authenticate all servers and perform redundant checks when using DNS hostnames.
- When possible, use error-correcting (ECC) memory in local devices as non-ECC memory is significantly more vulnerable to faults.

## Source

- [MITRE CAPEC CAPEC-611](https://capec.mitre.org/data/definitions/611.html)
