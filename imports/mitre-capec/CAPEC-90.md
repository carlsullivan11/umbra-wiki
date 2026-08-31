---
slug: attack-pattern/CAPEC-90
title: "CAPEC-90 — Reflection Attack in Authentication Protocol"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-90]
cwe_ids: [CWE-301, CWE-303]
related: [weakness/CWE-301, weakness/CWE-303]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-90
updated_at: 2026-08-31
summary: "An adversary can abuse an authentication protocol susceptible to reflection attack in order to defeat it. Doing so allows the adversary illegitimate access to the target system, without possessing the requisite credentials. Reflection attacks are of great concern to authenticatio…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/90.html
---

# CAPEC-90: Reflection Attack in Authentication Protocol

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary can abuse an authentication protocol susceptible to reflection attack in order to defeat it. Doing so allows the adversary illegitimate access to the target system, without possessing the requisite credentials. Reflection attacks are of great concern to authentication protocols that rely on a challenge-handshake or similar mechanism. An adversary can impersonate a legitimate user and can gain illegitimate access to the system by successfully mounting a reflection attack during authentication.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-301](/wiki/p/weakness/CWE-301), [CWE-303](/wiki/p/weakness/CWE-303)

## Prerequisites

- The attacker must have direct access to the target server in order to successfully mount a reflection attack. An intermediate entity, such as a router or proxy, that handles these exchanges on behalf of the attacker inhibits the attackers' ability to attack the authentication protocol.

## Skills required

- Medium: The attacker needs to have knowledge of observing the protocol exchange and managing the required connections in order to issue and respond to challenges

## Consequences

- Confidentiality, Access Control, Authorization: Gain Privileges, Bypass Protection Mechanism
- Confidentiality: Read Data

## Mitigations

- The server must initiate the handshake by issuing the challenge. This ensures that the client has to respond before the exchange can move any further
- The use of HMAC to hash the response from the server can also be used to thwart reflection. The server responds by returning its own challenge as well as hashing the client's challenge, its own challenge and the pre-shared secret. Requiring the client to respond with the HMAC of the two challenges ensures that only the possessor of a valid pre-shared secret can successfully hash in the two values.
- Introducing a random nonce with each new connection ensures that the attacker cannot employ two connections to attack the authentication protocol

## Source

- [MITRE CAPEC CAPEC-90](https://capec.mitre.org/data/definitions/90.html)
