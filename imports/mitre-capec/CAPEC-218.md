---
slug: attack-pattern/CAPEC-218
title: "CAPEC-218 — Spoofing of UDDI/ebXML Messages"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-218]
cwe_ids: [CWE-345]
related: [weakness/CWE-345]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-218
updated_at: 2026-08-31
summary: "An attacker spoofs a UDDI, ebXML, or similar message in order to impersonate a service provider in an e-business transaction. UDDI, ebXML, and similar standards are used to identify businesses in e-business transactions. Among other things, they identify a particular participant,…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/218.html
---

# CAPEC-218: Spoofing of UDDI/ebXML Messages

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker spoofs a UDDI, ebXML, or similar message in order to impersonate a service provider in an e-business transaction. UDDI, ebXML, and similar standards are used to identify businesses in e-business transactions. Among other things, they identify a particular participant, WSDL information for SOAP transactions, and supported communication protocols, including security protocols. By spoofing one of these messages an attacker could impersonate a legitimate business in a transaction or could manipulate the protocols used between a client and business. This could result in disclosure of sensitive information, loss of message integrity, or even financial fraud.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-345](/wiki/p/weakness/CWE-345)

## Prerequisites

- The targeted business's UDDI or ebXML information must be served from a location that the attacker can spoof or compromise or the attacker must be able to intercept and modify unsecured UDDI/ebXML messages in transit.

## Mitigations

- Implementation: Clients should only trust UDDI, ebXML, or similar messages that are verifiably signed by a trusted party.

## Source

- [MITRE CAPEC CAPEC-218](https://capec.mitre.org/data/definitions/218.html)
