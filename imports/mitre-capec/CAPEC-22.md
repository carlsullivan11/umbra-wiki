---
slug: attack-pattern/CAPEC-22
title: "CAPEC-22 — Exploiting Trust in Client"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-22]
cwe_ids: [CWE-20, CWE-200, CWE-287, CWE-290, CWE-693]
related: [weakness/CWE-20, weakness/CWE-200, weakness/CWE-287, weakness/CWE-290, weakness/CWE-693]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-22
updated_at: 2026-08-31
summary: "An attack of this type exploits vulnerabilities in client/server communication channel authentication and data integrity. It leverages the implicit trust a server places in the client, or more importantly, that which the server believes is the client. An attacker executes this ty…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/22.html
---

# CAPEC-22: Exploiting Trust in Client

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attack of this type exploits vulnerabilities in client/server communication channel authentication and data integrity. It leverages the implicit trust a server places in the client, or more importantly, that which the server believes is the client. An attacker executes this type of attack by communicating directly with the server where the server believes it is communicating only with a valid client. There are numerous variations of this type of attack.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-20](/wiki/p/weakness/CWE-20), [CWE-200](/wiki/p/weakness/CWE-200), [CWE-287](/wiki/p/weakness/CWE-287), [CWE-290](/wiki/p/weakness/CWE-290), [CWE-693](/wiki/p/weakness/CWE-693)

## Prerequisites

- Server software must rely on client side formatted and validated values, and not reinforce these checks on the server side.

## Skills required

- Medium: The attacker must have fairly detailed knowledge of the syntax and semantics of client/server communications protocols and grammars

## Consequences

- Confidentiality, Integrity, Availability: Execute Unauthorized Commands
- Confidentiality, Access Control, Authorization: Gain Privileges
- Confidentiality: Read Data

## Mitigations

- Design: Ensure that client process and/or message is authenticated so that anonymous communications and/or messages are not accepted by the system.
- Design: Do not rely on client validation or encoding for security purposes.
- Design: Utilize digital signatures to increase authentication assurance.
- Design: Utilize two factor authentication to increase authentication assurance.
- Implementation: Perform input validation for all remote content.

## Source

- [MITRE CAPEC CAPEC-22](https://capec.mitre.org/data/definitions/22.html)
