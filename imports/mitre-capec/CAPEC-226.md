---
slug: attack-pattern/CAPEC-226
title: "CAPEC-226 — Session Credential Falsification through Manipulation"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-226]
cwe_ids: [CWE-472, CWE-565]
related: [weakness/CWE-472, weakness/CWE-565]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-226
updated_at: 2026-08-31
summary: "An attacker manipulates an existing credential in order to gain access to a target application. Session credentials allow users to identify themselves to a service after an initial authentication without needing to resend the authentication information (usually a username and pas…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/226.html
---

# CAPEC-226: Session Credential Falsification through Manipulation

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker manipulates an existing credential in order to gain access to a target application. Session credentials allow users to identify themselves to a service after an initial authentication without needing to resend the authentication information (usually a username and password) with every message. An attacker may be able to manipulate a credential sniffed from an existing connection in order to gain access to a target server.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-472](/wiki/p/weakness/CWE-472), [CWE-565](/wiki/p/weakness/CWE-565)

## Prerequisites

- The targeted application must use session credentials to identify legitimate users.

## Source

- [MITRE CAPEC CAPEC-226](https://capec.mitre.org/data/definitions/226.html)
