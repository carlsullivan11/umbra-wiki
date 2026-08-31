---
slug: attack-pattern/CAPEC-279
title: "CAPEC-279 — SOAP Manipulation"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-279]
cwe_ids: [CWE-707]
related: [weakness/CWE-707]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-279
updated_at: 2026-08-31
summary: "Simple Object Access Protocol (SOAP) is used as a communication protocol between a client and server to invoke web services on the server. It is an XML-based protocol, and therefore suffers from many of the same shortcomings as other XML-based protocols. Adversaries can make use …"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/279.html
---

# CAPEC-279: SOAP Manipulation

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

Simple Object Access Protocol (SOAP) is used as a communication protocol between a client and server to invoke web services on the server. It is an XML-based protocol, and therefore suffers from many of the same shortcomings as other XML-based protocols. Adversaries can make use of these shortcomings and manipulate the content of SOAP paramters, leading to undesirable behavior on the server and allowing the adversary to carry out a number of further attacks.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-707](/wiki/p/weakness/CWE-707)

## Prerequisites

- An application uses SOAP-based web service api.
- An application does not perform sufficient input validation to ensure that user-controllable data is safe for an XML parser.
- The targeted server either fails to verify that data in SOAP messages conforms to the appropriate XML schema, or it fails to correctly handle the complete range of data allowed by the schema.

## Consequences

- Availability: Resource Consumption
- Confidentiality: Read Data
- Confidentiality, Integrity, Availability: Execute Unauthorized Commands

## Source

- [MITRE CAPEC CAPEC-279](https://capec.mitre.org/data/definitions/279.html)
