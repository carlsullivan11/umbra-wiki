---
slug: attack-pattern/CAPEC-631
title: "CAPEC-631 — SoundSquatting"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-631]
related: []
provenance: imported
import_source: mitre-capec
import_id: CAPEC-631
updated_at: 2026-08-31
summary: "An adversary registers a domain name that sounds the same as a trusted domain, but has a different spelling. A SoundSquatting attack takes advantage of a user's confusion of the two words to direct Internet traffic to adversary-controlled destinations. SoundSquatting does not req…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/631.html
---

# CAPEC-631: SoundSquatting

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary registers a domain name that sounds the same as a trusted domain, but has a different spelling. A SoundSquatting attack takes advantage of a user's confusion of the two words to direct Internet traffic to adversary-controlled destinations. SoundSquatting does not require an attack against the trusted domain or complicated reverse engineering.

## Prerequisites

- An adversary requires knowledge of popular or high traffic domains, that could be used to deceive potential targets.

## Skills required

- Low: Adversaries must be able to register DNS hostnames/URL’s.

## Consequences

- Other: Other

## Mitigations

- Authenticate all servers and perform redundant checks when using DNS hostnames.
- Purchase potential SoundSquatted domains and forward to legitimate domain.

## Source

- [MITRE CAPEC CAPEC-631](https://capec.mitre.org/data/definitions/631.html)
