---
slug: attack-pattern/CAPEC-51
title: "CAPEC-51 — Poison Web Service Registry"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-51]
cwe_ids: [CWE-74, CWE-285, CWE-693]
related: [weakness/CWE-74, weakness/CWE-285, weakness/CWE-693]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-51
updated_at: 2026-08-31
summary: "SOA and Web Services often use a registry to perform look up, get schema information, and metadata about services. A poisoned registry can redirect (think phishing for servers) the service requester to a malicious service provider, provide incorrect information in schema or metad…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/51.html
---

# CAPEC-51: Poison Web Service Registry

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Very High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

SOA and Web Services often use a registry to perform look up, get schema information, and metadata about services. A poisoned registry can redirect (think phishing for servers) the service requester to a malicious service provider, provide incorrect information in schema or metadata, and delete information about service provider interfaces.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-74](/wiki/p/weakness/CWE-74), [CWE-285](/wiki/p/weakness/CWE-285), [CWE-693](/wiki/p/weakness/CWE-693)

## Prerequisites

- The attacker must be able to write to resources or redirect access to the service registry.

## Skills required

- Low: To identify and execute against an over-privileged system interface

## Consequences

- Confidentiality, Integrity, Availability: Execute Unauthorized Commands
- Confidentiality: Read Data
- Integrity: Modify Data

## Mitigations

- Design: Enforce principle of least privilege
- Design: Harden registry server and file access permissions
- Implementation: Implement communications to and from the registry using secure protocols

## Source

- [MITRE CAPEC CAPEC-51](https://capec.mitre.org/data/definitions/51.html)
