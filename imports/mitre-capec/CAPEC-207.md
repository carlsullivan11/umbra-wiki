---
slug: attack-pattern/CAPEC-207
title: "CAPEC-207 — Removing Important Client Functionality"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-207]
cwe_ids: [CWE-602]
related: [weakness/CWE-602]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-207
updated_at: 2026-08-31
summary: "An adversary removes or disables functionality on the client that the server assumes to be present and trustworthy."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/207.html
---

# CAPEC-207: Removing Important Client Functionality

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary removes or disables functionality on the client that the server assumes to be present and trustworthy.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-602](/wiki/p/weakness/CWE-602)

## Prerequisites

- The targeted server must assume the client performs important actions to protect the server or the server functionality. For example, the server may assume the client filters outbound traffic or that the client performs all price calculations correctly. Moreover, the server must fail to detect when these assumptions are violated by a client.

## Skills required

- High: To reverse engineer the client-side code to disable/remove the functionality on the client that the server relies on.
- Low: The adversary installs a web tool that allows scripts or the DOM model of web-based applications to be modified before they are executed in a browser. GreaseMonkey and Firebug are two examples of such tools.

## Consequences

- Confidentiality: Other
- Integrity: Modify Data
- Confidentiality: Read Data
- Accountability, Authentication, Authorization, Non-Repudiation: Gain Privileges
- Access Control, Authorization: Bypass Protection Mechanism

## Mitigations

- Design: For any security checks that are performed on the client side, ensure that these checks are duplicated on the server side.
- Design: Ship client-side application with integrity checks (code signing) when possible.
- Design: Use obfuscation and other techniques to prevent reverse engineering the client code.

## Source

- [MITRE CAPEC CAPEC-207](https://capec.mitre.org/data/definitions/207.html)
