---
slug: attack-pattern/CAPEC-493
title: "CAPEC-493 — SOAP Array Blowup"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-493]
cwe_ids: [CWE-770]
related: [weakness/CWE-770]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-493
updated_at: 2026-08-31
summary: "An adversary may execute an attack on a web service that uses SOAP messages in communication. By sending a very large SOAP array declaration to the web service, the attacker forces the web service to allocate space for the array elements before they are parsed by the XML parser. …"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/493.html
---

# CAPEC-493: SOAP Array Blowup

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | — |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary may execute an attack on a web service that uses SOAP messages in communication. By sending a very large SOAP array declaration to the web service, the attacker forces the web service to allocate space for the array elements before they are parsed by the XML parser. The attacker message is typically small in size containing a large array declaration of say 1,000,000 elements and a couple of array elements. This attack targets exhaustion of the memory resources of the web service.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-770](/wiki/p/weakness/CWE-770)

## Prerequisites

- This type of an attack requires the attacker to know the endpoint of the web service, and be able to reach the endpoint with a malicious SOAP message.

## Mitigations

- Enforce strict schema validation. The schema should enforce a maximum number of array elements. If the number of maximum array elements can't be limited another validation method should be used. One such method could be comparing the declared number of items in the array with the existing number of elements of the array. If these numbers don't match drop the SOAP packet at the web service layer.

## Source

- [MITRE CAPEC CAPEC-493](https://capec.mitre.org/data/definitions/493.html)
