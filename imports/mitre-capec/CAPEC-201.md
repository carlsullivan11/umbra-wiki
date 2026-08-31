---
slug: attack-pattern/CAPEC-201
title: "CAPEC-201 — Serialized Data External Linking"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-201]
cwe_ids: [CWE-829]
related: [weakness/CWE-829]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-201
updated_at: 2026-08-31
summary: "An adversary creates a serialized data file (e.g. XML, YAML, etc...) that contains an external data reference. Because serialized data parsers may not validate documents with external references, there may be no checks on the nature of the reference in the external data. This can…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/201.html
---

# CAPEC-201: Serialized Data External Linking

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary creates a serialized data file (e.g. XML, YAML, etc...) that contains an external data reference. Because serialized data parsers may not validate documents with external references, there may be no checks on the nature of the reference in the external data. This can allow an adversary to open arbitrary files or connections, which may further lead to the adversary gaining access to information on the system that they would normally be unable to obtain.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-829](/wiki/p/weakness/CWE-829)

## Prerequisites

- The target must follow external data references without validating the validity of the reference target.

## Skills required

- Low: To send serialized data messages with maliciously crafted schema.

## Consequences

- Confidentiality: Read Data

## Mitigations

- Configure the serialized data processor to only retrieve external entities from trusted sources.

## Source

- [MITRE CAPEC CAPEC-201](https://capec.mitre.org/data/definitions/201.html)
