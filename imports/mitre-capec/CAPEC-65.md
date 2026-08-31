---
slug: attack-pattern/CAPEC-65
title: "CAPEC-65 — Sniff Application Code"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-65]
cwe_ids: [CWE-311, CWE-318, CWE-319, CWE-693]
mitre_ids: [T1040]
related: [weakness/CWE-311, weakness/CWE-318, weakness/CWE-319, weakness/CWE-693, technique/T1040]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-65
updated_at: 2026-08-31
summary: "An adversary passively sniffs network communications and captures application code bound for an authorized client. Once obtained, they can use it as-is, or through reverse-engineering glean sensitive information or exploit the trust relationship between the client and server. Suc…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/65.html
---

# CAPEC-65: Sniff Application Code

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary passively sniffs network communications and captures application code bound for an authorized client. Once obtained, they can use it as-is, or through reverse-engineering glean sensitive information or exploit the trust relationship between the client and server. Such code may belong to a dynamic update to the client, a patch being applied to a client component or any such interaction where the client is authorized to communicate with the server.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-311](/wiki/p/weakness/CWE-311), [CWE-318](/wiki/p/weakness/CWE-318), [CWE-319](/wiki/p/weakness/CWE-319), [CWE-693](/wiki/p/weakness/CWE-693)

**ATT&CK techniques:** [T1040](/wiki/p/technique/T1040)

## Prerequisites

- The attacker must have the ability to place themself in the communication path between the client and server.
- The targeted application must receive some application code from the server; for example, dynamic updates, patches, applets or scripts.
- The attacker must be able to employ a sniffer on the network without being detected.

## Skills required

- Medium: The attacker needs to setup a sniffer for a sufficient period of time so as to capture meaningful quantities of code. The presence of the sniffer should not be detected on the network. Also if the attacker plans to employ an adversary-in-the-middle attack (CAPEC-94), the client or server must not realize this. Finally, the attacker needs to regenerate source code from binary code if the need be.

## Consequences

- Confidentiality: Read Data
- Confidentiality, Access Control, Authorization: Gain Privileges

## Mitigations

- Design: Encrypt all communication between the client and server.
- Implementation: Use SSL, SSH, SCP.
- Operation: Use "ifconfig/ipconfig" or other tools to detect the sniffer installed in the network.

## Source

- [MITRE CAPEC CAPEC-65](https://capec.mitre.org/data/definitions/65.html)
