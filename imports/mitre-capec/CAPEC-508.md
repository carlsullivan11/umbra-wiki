---
slug: attack-pattern/CAPEC-508
title: "CAPEC-508 — Shoulder Surfing"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-508]
cwe_ids: [CWE-200, CWE-359]
related: [weakness/CWE-200, weakness/CWE-359]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-508
updated_at: 2026-08-31
summary: "In a shoulder surfing attack, an adversary observes an unaware individual's keystrokes, screen content, or conversations with the goal of obtaining sensitive information. One motive for this attack is to obtain sensitive information about the target for financial, personal, polit…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/508.html
---

# CAPEC-508: Shoulder Surfing

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

In a shoulder surfing attack, an adversary observes an unaware individual's keystrokes, screen content, or conversations with the goal of obtaining sensitive information. One motive for this attack is to obtain sensitive information about the target for financial, personal, political, or other gains. From an insider threat perspective, an additional motive could be to obtain system/application credentials or cryptographic keys. Shoulder surfing attacks are accomplished by observing the content "over the victim's shoulder", as implied by the name of this attack.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-200](/wiki/p/weakness/CWE-200), [CWE-359](/wiki/p/weakness/CWE-359)

## Prerequisites

- The adversary typically requires physical proximity to the target's environment, in order to observe their screen or conversation. This may not be the case if the adversary is able to record the target and obtain sensitive information upon review of the recording.

## Skills required

- Low: In most cases, an adversary can simply observe and retain the desired information.

## Consequences

- Confidentiality: Read Data

## Mitigations

- Be mindful of your surroundings when discussing or viewing sensitive information in public areas.
- Pertaining to insider threats, ensure that sensitive information is not displayed to nor discussed around individuals without need-to-know access to said information.

## Source

- [MITRE CAPEC CAPEC-508](https://capec.mitre.org/data/definitions/508.html)
