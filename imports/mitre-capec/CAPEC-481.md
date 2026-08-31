---
slug: attack-pattern/CAPEC-481
title: "CAPEC-481 — Contradictory Destinations in Traffic Routing Schemes"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-481]
cwe_ids: [CWE-923]
mitre_ids: [T1090.004]
related: [weakness/CWE-923, technique/T1090.004]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-481
updated_at: 2026-08-31
summary: "Adversaries can provide contradictory destinations when sending messages. Traffic is routed in networks using the domain names in various headers available at different levels of the OSI model. In a Content Delivery Network (CDN) multiple domains might be available, and if there …"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/481.html
---

# CAPEC-481: Contradictory Destinations in Traffic Routing Schemes

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

Adversaries can provide contradictory destinations when sending messages. Traffic is routed in networks using the domain names in various headers available at different levels of the OSI model. In a Content Delivery Network (CDN) multiple domains might be available, and if there are contradictory domain names provided it is possible to route traffic to an inappropriate destination. The technique, called Domain Fronting, involves using different domain names in the SNI field of the TLS header and the Host field of the HTTP header. An alternative technique, called Domainless Fronting, is similar, but the SNI field is left blank.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-923](/wiki/p/weakness/CWE-923)

**ATT&CK techniques:** [T1090.004](/wiki/p/technique/T1090.004)

## Prerequisites

- An adversary must be aware that their message will be routed using a CDN, and that both of the contradictory domains are served from that CDN.
- If the purpose of the Domain Fronting is to hide redirected C2 traffic, the C2 server must have been created in the CDN.

## Skills required

- Medium: The adversary must have some knowledge of how messages are routed.

## Consequences

- Confidentiality: Read Data, Modify Data

## Mitigations

- Monitor connections, checking headers in traffic for contradictory domain names, or empty domain names.

## Source

- [MITRE CAPEC CAPEC-481](https://capec.mitre.org/data/definitions/481.html)
