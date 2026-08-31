---
slug: attack-pattern/CAPEC-528
title: "CAPEC-528 — XML Flood"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-528]
cwe_ids: [CWE-770]
mitre_ids: [T1498.001, T1499.002]
related: [weakness/CWE-770, technique/T1498.001, technique/T1499.002]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-528
updated_at: 2026-08-31
summary: "An adversary may execute a flooding attack using XML messages with the intent to deny legitimate users access to a web service. These attacks are accomplished by sending a large number of XML based requests and letting the service attempt to parse each one. In many cases this typ…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/528.html
---

# CAPEC-528: XML Flood

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary may execute a flooding attack using XML messages with the intent to deny legitimate users access to a web service. These attacks are accomplished by sending a large number of XML based requests and letting the service attempt to parse each one. In many cases this type of an attack will result in a XML Denial of Service (XDoS) due to an application becoming unstable, freezing, or crashing.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-770](/wiki/p/weakness/CWE-770)

**ATT&CK techniques:** [T1498.001](/wiki/p/technique/T1498.001), [T1499.002](/wiki/p/technique/T1499.002)

## Prerequisites

- The target must receive and process XML transactions.
- An adverssary must possess the ability to generate a large amount of XML based messages to send to the target service.

## Skills required

- Low: Denial of service

## Consequences

- Availability: Resource Consumption

## Mitigations

- Design: Build throttling mechanism into the resource allocation. Provide for a timeout mechanism for allocated resources whose transaction does not complete within a specified interval.
- Implementation: Provide for network flow control and traffic shaping to control access to the resources.

## Source

- [MITRE CAPEC CAPEC-528](https://capec.mitre.org/data/definitions/528.html)
