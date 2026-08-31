---
slug: attack-pattern/CAPEC-4
title: "CAPEC-4 — Using Alternative IP Address Encodings"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-4]
cwe_ids: [CWE-173, CWE-291]
related: [weakness/CWE-173, weakness/CWE-291]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-4
updated_at: 2026-08-31
summary: "This attack relies on the adversary using unexpected formats for representing IP addresses. Networked applications may expect network location information in a specific format, such as fully qualified domains names (FQDNs), URL, IP address, or IP Address ranges. If the location i…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/4.html
---

# CAPEC-4: Using Alternative IP Address Encodings

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

This attack relies on the adversary using unexpected formats for representing IP addresses. Networked applications may expect network location information in a specific format, such as fully qualified domains names (FQDNs), URL, IP address, or IP Address ranges. If the location information is not validated against a variety of different possible encodings and formats, the adversary can use an alternate format to bypass application access control.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-173](/wiki/p/weakness/CWE-173), [CWE-291](/wiki/p/weakness/CWE-291)

## Prerequisites

- The target software must fail to anticipate all of the possible valid encodings of an IP/web address.
- The adversary must have the ability to communicate with the server.

## Skills required

- Low: The adversary has only to try IP address format combinations.

## Consequences

- Confidentiality, Access Control, Authorization: Gain Privileges

## Mitigations

- Design: Default deny access control policies
- Design: Input validation routines should check and enforce both input data types and content against a positive specification. In regards to IP addresses, this should include the authorized manner for the application to represent IP addresses and not accept user specified IP addresses and IP address formats (such as ranges)
- Implementation: Perform input validation for all remote content.

## Source

- [MITRE CAPEC CAPEC-4](https://capec.mitre.org/data/definitions/4.html)
