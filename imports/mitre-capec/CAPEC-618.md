---
slug: attack-pattern/CAPEC-618
title: "CAPEC-618 — Cellular Broadcast Message Request"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-618]
cwe_ids: [CWE-201]
related: [weakness/CWE-201]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-618
updated_at: 2026-08-31
summary: "In this attack scenario, the attacker uses knowledge of the target’s mobile phone number (i.e., the number associated with the SIM used in the retransmission device) to cause the cellular network to send broadcast messages to alert the mobile device. Since the network knows which…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/618.html
---

# CAPEC-618: Cellular Broadcast Message Request

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Low |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

In this attack scenario, the attacker uses knowledge of the target’s mobile phone number (i.e., the number associated with the SIM used in the retransmission device) to cause the cellular network to send broadcast messages to alert the mobile device. Since the network knows which cell tower the target’s mobile device is attached to, the broadcast messages are only sent in the Location Area Code (LAC) where the target is currently located. By triggering the cellular broadcast message and then listening for the presence or absence of that message, an attacker could verify that the target is in (or not in) a given location.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-201](/wiki/p/weakness/CWE-201)

## Prerequisites

- The attacker must have knowledge of the target’s mobile phone number.

## Skills required

- Low: Open source and commercial tools are available for this attack.

## Consequences

- Other: Other

## Mitigations

- Frequent changing of mobile number.

## Source

- [MITRE CAPEC CAPEC-618](https://capec.mitre.org/data/definitions/618.html)
