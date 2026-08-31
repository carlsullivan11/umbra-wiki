---
slug: attack-pattern/CAPEC-173
title: "CAPEC-173 — Action Spoofing"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-173]
cwe_ids: [CWE-451]
related: [weakness/CWE-451]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-173
updated_at: 2026-08-31
summary: "An adversary is able to disguise one action for another and therefore trick a user into initiating one type of action when they intend to initiate a different action. For example, a user might be led to believe that clicking a button will submit a query, but in fact it downloads …"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/173.html
---

# CAPEC-173: Action Spoofing

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Very High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary is able to disguise one action for another and therefore trick a user into initiating one type of action when they intend to initiate a different action. For example, a user might be led to believe that clicking a button will submit a query, but in fact it downloads software. Adversaries may perform this attack through social means, such as by simply convincing a victim to perform the action or relying on a user's natural inclination to do so, or through technical means, such as a clickjacking attack where a user sees one interface but is actually interacting with a second, invisible, interface.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-451](/wiki/p/weakness/CWE-451)

## Prerequisites

- The adversary must convince the victim into performing the decoy action.
- The adversary must have the means to control a user's interface to present them with a decoy action as well as the actual malicious action. Simple versions of this attack can be performed using web pages requiring only that the adversary be able to host (or control) content that the user visits.

## Consequences

- Confidentiality, Integrity, Availability: Other

## Mitigations

- Avoid interacting with suspicious sites or clicking suspicious links.
- An organization should provide regular, robust cybersecurity training to its employees.

## Source

- [MITRE CAPEC CAPEC-173](https://capec.mitre.org/data/definitions/173.html)
