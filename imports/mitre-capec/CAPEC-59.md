---
slug: attack-pattern/CAPEC-59
title: "CAPEC-59 — Session Credential Falsification through Prediction"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-59]
cwe_ids: [CWE-6, CWE-200, CWE-285, CWE-290, CWE-330, CWE-331, CWE-346, CWE-384, CWE-488, CWE-539, CWE-693]
related: [weakness/CWE-6, weakness/CWE-200, weakness/CWE-285, weakness/CWE-290, weakness/CWE-330, weakness/CWE-331, weakness/CWE-346, weakness/CWE-384, weakness/CWE-488, weakness/CWE-539, weakness/CWE-693]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-59
updated_at: 2026-08-31
summary: "This attack targets predictable session ID in order to gain privileges. The attacker can predict the session ID used during a transaction to perform spoofing and session hijacking."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/59.html
---

# CAPEC-59: Session Credential Falsification through Prediction

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

This attack targets predictable session ID in order to gain privileges. The attacker can predict the session ID used during a transaction to perform spoofing and session hijacking.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-6](/wiki/p/weakness/CWE-6), [CWE-200](/wiki/p/weakness/CWE-200), [CWE-285](/wiki/p/weakness/CWE-285), [CWE-290](/wiki/p/weakness/CWE-290), [CWE-330](/wiki/p/weakness/CWE-330), [CWE-331](/wiki/p/weakness/CWE-331), [CWE-346](/wiki/p/weakness/CWE-346), [CWE-384](/wiki/p/weakness/CWE-384), [CWE-488](/wiki/p/weakness/CWE-488), [CWE-539](/wiki/p/weakness/CWE-539), [CWE-693](/wiki/p/weakness/CWE-693)

## Prerequisites

- The target host uses session IDs to keep track of the users.
- Session IDs are used to control access to resources.
- The session IDs used by the target host are predictable. For example, the session IDs are generated using predictable information (e.g., time).

## Skills required

- Low: There are tools to brute force session ID. Those tools require a low level of knowledge.
- Medium: Predicting Session ID may require more computation work which uses advanced analysis such as statistical analysis.

## Consequences

- Confidentiality, Access Control, Authorization: Gain Privileges

## Mitigations

- Use a strong source of randomness to generate a session ID.
- Use adequate length session IDs
- Do not use information available to the user in order to generate session ID (e.g., time).
- Ideas for creating random numbers are offered by Eastlake [RFC1750]
- Encrypt the session ID if you expose it to the user. For instance session ID can be stored in a cookie in encrypted format.

## Source

- [MITRE CAPEC CAPEC-59](https://capec.mitre.org/data/definitions/59.html)
