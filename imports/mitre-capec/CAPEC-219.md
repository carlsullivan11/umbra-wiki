---
slug: attack-pattern/CAPEC-219
title: "CAPEC-219 — XML Routing Detour Attacks"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-219]
cwe_ids: [CWE-441, CWE-610]
related: [weakness/CWE-441, weakness/CWE-610]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-219
updated_at: 2026-08-31
summary: "An attacker subverts an intermediate system used to process XML content and forces the intermediate to modify and/or re-route the processing of the content. XML Routing Detour Attacks are Adversary in the Middle type attacks (CAPEC-94). The attacker compromises or inserts an inte…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/219.html
---

# CAPEC-219: XML Routing Detour Attacks

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker subverts an intermediate system used to process XML content and forces the intermediate to modify and/or re-route the processing of the content. XML Routing Detour Attacks are Adversary in the Middle type attacks (CAPEC-94). The attacker compromises or inserts an intermediate system in the processing of the XML message. For example, WS-Routing can be used to specify a series of nodes or intermediaries through which content is passed. If any of the intermediate nodes in this route are compromised by an attacker they could be used for a routing detour attack. From the compromised system the attacker is able to route the XML process to other nodes of their choice and modify the responses so that the normal chain of processing is unaware of the interception. This system can forward the message to an outside entity and hide the forwarding and processing from the legitimate processing systems by altering the header information.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-441](/wiki/p/weakness/CWE-441), [CWE-610](/wiki/p/weakness/CWE-610)

## Prerequisites

- The targeted system must have multiple stages processing of XML content.

## Skills required

- Low: To inject a bogus node in the XML routing table

## Consequences

- Integrity: Modify Data
- Confidentiality: Read Data
- Accountability, Authentication, Authorization, Non-Repudiation: Gain Privileges
- Access Control, Authorization: Bypass Protection Mechanism

## Mitigations

- Design: Specify maximum number intermediate nodes for the request and require SSL connections with mutual authentication.
- Implementation: Use SSL for connections between all parties with mutual authentication.

## Source

- [MITRE CAPEC CAPEC-219](https://capec.mitre.org/data/definitions/219.html)
