---
slug: attack-pattern/CAPEC-39
title: "CAPEC-39 — Manipulating Opaque Client-based Data Tokens"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-39]
cwe_ids: [CWE-233, CWE-285, CWE-302, CWE-315, CWE-353, CWE-384, CWE-472, CWE-539, CWE-565]
related: [weakness/CWE-233, weakness/CWE-285, weakness/CWE-302, weakness/CWE-315, weakness/CWE-353, weakness/CWE-384, weakness/CWE-472, weakness/CWE-539, weakness/CWE-565]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-39
updated_at: 2026-08-31
summary: "In circumstances where an application holds important data client-side in tokens (cookies, URLs, data files, and so forth) that data can be manipulated. If client or server-side application components reinterpret that data as authentication tokens or data (such as store item pric…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/39.html
---

# CAPEC-39: Manipulating Opaque Client-based Data Tokens

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

In circumstances where an application holds important data client-side in tokens (cookies, URLs, data files, and so forth) that data can be manipulated. If client or server-side application components reinterpret that data as authentication tokens or data (such as store item pricing or wallet information) then even opaquely manipulating that data may bear fruit for an Attacker. In this pattern an attacker undermines the assumption that client side tokens have been adequately protected from tampering through use of encryption or obfuscation.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-233](/wiki/p/weakness/CWE-233), [CWE-285](/wiki/p/weakness/CWE-285), [CWE-302](/wiki/p/weakness/CWE-302), [CWE-315](/wiki/p/weakness/CWE-315), [CWE-353](/wiki/p/weakness/CWE-353), [CWE-384](/wiki/p/weakness/CWE-384), [CWE-472](/wiki/p/weakness/CWE-472), [CWE-539](/wiki/p/weakness/CWE-539), [CWE-565](/wiki/p/weakness/CWE-565)

## Prerequisites

- An attacker already has some access to the system or can steal the client based data tokens from another user who has access to the system.
- For an Attacker to viably execute this attack, some data (later interpreted by the application) must be held client-side in a way that can be manipulated without detection. This means that the data or tokens are not CRCd as part of their value or through a separate meta-data store elsewhere.

## Skills required

- Medium: If the client site token is obfuscated.
- High: If the client site token is encrypted.

## Consequences

- Integrity: Modify Data
- Confidentiality, Access Control, Authorization: Gain Privileges

## Mitigations

- One solution to this problem is to protect encrypted data with a CRC of some sort. If knowing who last manipulated the data is important, then using a cryptographic "message authentication code" (or hMAC) is prescribed. However, this guidance is not a panacea. In particular, any value created by (and therefore encrypted by) the client, which itself is a "malicious" value, all the protective cryptography in the world can't make the value 'correct' again. Put simply, if the client has control over the whole process of generating and encoding the value, then simply protecting its integrity doesn't help.
- Make sure to protect client side authentication tokens for confidentiality (encryption) and integrity (signed hash)
- Make sure that all session tokens use a good source of randomness
- Perform validation on the server side to make sure that client side data tokens are consistent with what is expected.

## Source

- [MITRE CAPEC CAPEC-39](https://capec.mitre.org/data/definitions/39.html)
