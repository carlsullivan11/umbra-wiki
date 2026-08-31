---
slug: attack-pattern/CAPEC-84
title: "CAPEC-84 — XQuery Injection"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-84]
cwe_ids: [CWE-74, CWE-707]
related: [weakness/CWE-74, weakness/CWE-707]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-84
updated_at: 2026-08-31
summary: "This attack utilizes XQuery to probe and attack server systems; in a similar manner that SQL Injection allows an attacker to exploit SQL calls to RDBMS, XQuery Injection uses improperly validated data that is passed to XQuery commands to traverse and execute commands that the XQu…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/84.html
---

# CAPEC-84: XQuery Injection

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Very High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

This attack utilizes XQuery to probe and attack server systems; in a similar manner that SQL Injection allows an attacker to exploit SQL calls to RDBMS, XQuery Injection uses improperly validated data that is passed to XQuery commands to traverse and execute commands that the XQuery routines have access to. XQuery injection can be used to enumerate elements on the victim's environment, inject commands to the local host, or execute queries to remote files and data sources.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-74](/wiki/p/weakness/CWE-74), [CWE-707](/wiki/p/weakness/CWE-707)

## Prerequisites

- The XQL must execute unvalidated data

## Skills required

- Low: Basic understanding of XQuery

## Consequences

- Integrity: Modify Data
- Confidentiality: Read Data
- Confidentiality, Access Control, Authorization: Gain Privileges
- Confidentiality, Integrity, Availability: Execute Unauthorized Commands

## Mitigations

- Design: Perform input allowlist validation on all XML input
- Implementation: Run xml parsing and query infrastructure with minimal privileges so that an attacker is limited in their ability to probe other system resources from XQL.

## Source

- [MITRE CAPEC CAPEC-84](https://capec.mitre.org/data/definitions/84.html)
