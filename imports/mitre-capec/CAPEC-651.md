---
slug: attack-pattern/CAPEC-651
title: "CAPEC-651 — Eavesdropping"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-651]
cwe_ids: [CWE-200]
mitre_ids: [T1111]
related: [weakness/CWE-200, technique/T1111]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-651
updated_at: 2026-08-31
summary: "An adversary intercepts a form of communication (e.g. text, audio, video) by way of software (e.g., microphone and audio recording application), hardware (e.g., recording equipment), or physical means (e.g., physical proximity). The goal of eavesdropping is typically to gain unau…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/651.html
---

# CAPEC-651: Eavesdropping

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary intercepts a form of communication (e.g. text, audio, video) by way of software (e.g., microphone and audio recording application), hardware (e.g., recording equipment), or physical means (e.g., physical proximity). The goal of eavesdropping is typically to gain unauthorized access to sensitive information about the target for financial, personal, political, or other gains. Eavesdropping is different from a sniffing attack as it does not take place on a network-based communication channel (e.g., IP traffic). Instead, it entails listening in on the raw audio source of a conversation between two or more parties.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-200](/wiki/p/weakness/CWE-200)

**ATT&CK techniques:** [T1111](/wiki/p/technique/T1111)

## Prerequisites

- The adversary typically requires physical proximity to the target's environment, whether for physical eavesdropping or for placing recording equipment. This is not always the case for software-based eavesdropping, if the adversary has the capability to install malware on the target system that can activate a microphone and record audio digitally.

## Consequences

- Confidentiality: Other

## Mitigations

- Be mindful of your surroundings when discussing sensitive information in public areas.
- Implement proper software restriction policies to only allow authorized software on your environment. Use of anti-virus and other security monitoring and detecting tools can aid in this too. Closely monitor installed software for unusual behavior or activity, and implement patches as soon as they become available.
- If possible, physically disable the microphone on your machine if it is not needed.

## Source

- [MITRE CAPEC CAPEC-651](https://capec.mitre.org/data/definitions/651.html)
