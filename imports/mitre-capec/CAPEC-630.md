---
slug: attack-pattern/CAPEC-630
title: "CAPEC-630 — TypoSquatting"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-630]
related: []
provenance: imported
import_source: mitre-capec
import_id: CAPEC-630
updated_at: 2026-08-31
summary: "An adversary registers a domain name with at least one character different than a trusted domain. A TypoSquatting attack takes advantage of instances where a user mistypes a URL (e.g. www.goggle.com) or not does visually verify a URL before clicking on it (e.g. phishing attack). …"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/630.html
---

# CAPEC-630: TypoSquatting

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary registers a domain name with at least one character different than a trusted domain. A TypoSquatting attack takes advantage of instances where a user mistypes a URL (e.g. www.goggle.com) or not does visually verify a URL before clicking on it (e.g. phishing attack). As a result, the user is directed to an adversary-controlled destination. TypoSquatting does not require an attack against the trusted domain or complicated reverse engineering.

## Prerequisites

- An adversary requires knowledge of popular or high traffic domains, that could be used to deceive potential targets.

## Skills required

- Low: Adversaries must be able to register DNS hostnames/URL’s.

## Consequences

- Other: Other

## Mitigations

- Authenticate all servers and perform redundant checks when using DNS hostnames.
- Purchase potential TypoSquatted domains and forward to legitimate domain.

## Source

- [MITRE CAPEC CAPEC-630](https://capec.mitre.org/data/definitions/630.html)
