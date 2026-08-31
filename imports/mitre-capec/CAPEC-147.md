---
slug: attack-pattern/CAPEC-147
title: "CAPEC-147 — XML Ping of the Death"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-147]
cwe_ids: [CWE-400, CWE-770]
related: [weakness/CWE-400, weakness/CWE-770]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-147
updated_at: 2026-08-31
summary: "An attacker initiates a resource depletion attack where a large number of small XML messages are delivered at a sufficiently rapid rate to cause a denial of service or crash of the target. Transactions such as repetitive SOAP transactions can deplete resources faster than a simpl…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/147.html
---

# CAPEC-147: XML Ping of the Death

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker initiates a resource depletion attack where a large number of small XML messages are delivered at a sufficiently rapid rate to cause a denial of service or crash of the target. Transactions such as repetitive SOAP transactions can deplete resources faster than a simple flooding attack because of the additional resources used by the SOAP protocol and the resources necessary to process SOAP messages. The transactions used are immaterial as long as they cause resource utilization on the target. In other words, this is a normal flooding attack augmented by using messages that will require extra processing on the target.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-400](/wiki/p/weakness/CWE-400), [CWE-770](/wiki/p/weakness/CWE-770)

## Prerequisites

- The target must receive and process XML transactions.

## Skills required

- Low: To send small XML messages
- High: To use distributed network to launch the attack

## Consequences

- Availability: Resource Consumption

## Mitigations

- Design: Build throttling mechanism into the resource allocation. Provide for a timeout mechanism for allocated resources whose transaction does not complete within a specified interval.
- Implementation: Provide for network flow control and traffic shaping to control access to the resources.

## Source

- [MITRE CAPEC CAPEC-147](https://capec.mitre.org/data/definitions/147.html)
