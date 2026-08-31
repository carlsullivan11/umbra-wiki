---
slug: attack-pattern/CAPEC-632
title: "CAPEC-632 — Homograph Attack via Homoglyphs"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-632]
cwe_ids: [CWE-1007]
related: [weakness/CWE-1007]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-632
updated_at: 2026-08-31
summary: "An adversary registers a domain name containing a homoglyph, leading the registered domain to appear the same as a trusted domain. A homograph attack leverages the fact that different characters among various character sets look the same to the user. Homograph attacks must genera…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/632.html
---

# CAPEC-632: Homograph Attack via Homoglyphs

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary registers a domain name containing a homoglyph, leading the registered domain to appear the same as a trusted domain. A homograph attack leverages the fact that different characters among various character sets look the same to the user. Homograph attacks must generally be combined with other attacks, such as phishing attacks, in order to direct Internet traffic to the adversary-controlled destinations.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-1007](/wiki/p/weakness/CWE-1007)

## Prerequisites

- An adversary requires knowledge of popular or high traffic domains, that could be used to deceive potential targets.

## Skills required

- Low: Adversaries must be able to register DNS hostnames/URL’s.

## Consequences

- Other: Other

## Mitigations

- Authenticate all servers and perform redundant checks when using DNS hostnames.
- Utilize browsers that can warn users if URLs contain characters from different character sets.

## Source

- [MITRE CAPEC CAPEC-632](https://capec.mitre.org/data/definitions/632.html)
