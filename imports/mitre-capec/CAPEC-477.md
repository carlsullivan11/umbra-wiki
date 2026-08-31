---
slug: attack-pattern/CAPEC-477
title: "CAPEC-477 — Signature Spoofing by Mixing Signed and Unsigned Content"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-477]
cwe_ids: [CWE-311, CWE-319, CWE-693]
related: [weakness/CWE-311, weakness/CWE-319, weakness/CWE-693]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-477
updated_at: 2026-08-31
summary: "An attacker exploits the underlying complexity of a data structure that allows for both signed and unsigned content, to cause unsigned data to be processed as though it were signed data."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/477.html
---

# CAPEC-477: Signature Spoofing by Mixing Signed and Unsigned Content

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker exploits the underlying complexity of a data structure that allows for both signed and unsigned content, to cause unsigned data to be processed as though it were signed data.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-311](/wiki/p/weakness/CWE-311), [CWE-319](/wiki/p/weakness/CWE-319), [CWE-693](/wiki/p/weakness/CWE-693)

## Prerequisites

- Signer and recipient are using complex data storage structures that allow for a mix between signed and unsigned data
- Recipient is using signature verification software that does not maintain separation between signed and unsigned data once the signature has been verified.

## Skills required

- High: The attacker may need to continuously monitor a stream of signed data, waiting for an exploitable message to appear.
- High: Attacker must be able to create malformed data blobs and know how to insert them in a location that the recipient will visit.

## Mitigations

- Ensure the application is fully patched and does not allow the processing of unsigned data as if it is signed data.

## Source

- [MITRE CAPEC CAPEC-477](https://capec.mitre.org/data/definitions/477.html)
