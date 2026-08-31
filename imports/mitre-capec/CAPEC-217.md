---
slug: attack-pattern/CAPEC-217
title: "CAPEC-217 — Exploiting Incorrectly Configured SSL/TLS"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-217]
cwe_ids: [CWE-201]
related: [weakness/CWE-201]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-217
updated_at: 2026-08-31
summary: "An adversary takes advantage of incorrectly configured SSL/TLS communications that enables access to data intended to be encrypted. The adversary may also use this type of attack to inject commands or other traffic into the encrypted stream to cause compromise of either the clien…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/217.html
---

# CAPEC-217: Exploiting Incorrectly Configured SSL/TLS

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | — |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary takes advantage of incorrectly configured SSL/TLS communications that enables access to data intended to be encrypted. The adversary may also use this type of attack to inject commands or other traffic into the encrypted stream to cause compromise of either the client or server.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-201](/wiki/p/weakness/CWE-201)

## Prerequisites

- Access to the client/server stream.

## Skills required

- High: The adversary needs real-time access to network traffic in such a manner that the adversary can grab needed information from the SSL stream, possibly influence the decided-upon encryption method and options, and perform automated analysis to decipher encrypted material recovered. Tools exist to automate part of the tasks, but to successfully use these tools in an attack scenario requires detailed understanding of the underlying principles.

## Consequences

- Confidentiality: Read Data
- Confidentiality, Access Control, Authorization: Gain Privileges

## Mitigations

- Do not use SSL, as all SSL versions have been broken and should not be used. If TLS is not an option for the client or server, consider setting timeouts on SSL sessions to extremely low values to lessen the potential impact.
- Only use TLS version 1.2+, as versions 1.0 and 1.1 are insecure.
- Configure TLS to use secure algorithms. The current recommendation is to use ECDH, ECDSA, AES256-GCM, and SHA384 for the most security.

## Source

- [MITRE CAPEC CAPEC-217](https://capec.mitre.org/data/definitions/217.html)
