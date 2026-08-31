---
slug: attack-pattern/CAPEC-21
title: "CAPEC-21 — Exploitation of Trusted Identifiers"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-21]
cwe_ids: [CWE-6, CWE-290, CWE-302, CWE-346, CWE-384, CWE-539, CWE-602, CWE-642, CWE-664]
mitre_ids: [T1134, T1528, T1539]
related: [weakness/CWE-6, weakness/CWE-290, weakness/CWE-302, weakness/CWE-346, weakness/CWE-384, weakness/CWE-539, weakness/CWE-602, weakness/CWE-642, weakness/CWE-664, technique/T1134, technique/T1528, technique/T1539]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-21
updated_at: 2026-08-31
summary: "An adversary guesses, obtains, or 'rides' a trusted identifier (e.g. session ID, resource ID, cookie, etc.) to perform authorized actions under the guise of an authenticated user or service."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/21.html
---

# CAPEC-21: Exploitation of Trusted Identifiers

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary guesses, obtains, or "rides" a trusted identifier (e.g. session ID, resource ID, cookie, etc.) to perform authorized actions under the guise of an authenticated user or service.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-6](/wiki/p/weakness/CWE-6), [CWE-290](/wiki/p/weakness/CWE-290), [CWE-302](/wiki/p/weakness/CWE-302), [CWE-346](/wiki/p/weakness/CWE-346), [CWE-384](/wiki/p/weakness/CWE-384), [CWE-539](/wiki/p/weakness/CWE-539), [CWE-602](/wiki/p/weakness/CWE-602), [CWE-642](/wiki/p/weakness/CWE-642), [CWE-664](/wiki/p/weakness/CWE-664)

**ATT&CK techniques:** [T1134](/wiki/p/technique/T1134), [T1528](/wiki/p/technique/T1528), [T1539](/wiki/p/technique/T1539)

## Prerequisites

- Server software must rely on weak identifier proof and/or verification schemes.
- Identifiers must have long lifetimes and potential for reusability.
- Server software must allow concurrent sessions to exist.

## Skills required

- Low: To achieve a direct connection with the weak or non-existent server session access control, and pose as an authorized user

## Consequences

- Confidentiality, Access Control, Authentication: Gain Privileges
- Confidentiality: Read Data
- Integrity: Modify Data

## Mitigations

- Design: utilize strong federated identity such as SAML to encrypt and sign identity tokens in transit.
- Implementation: Use industry standards session key generation mechanisms that utilize high amount of entropy to generate the session key. Many standard web and application servers will perform this task on your behalf.
- Implementation: If the identifier is used for authentication, such as in the so-called single sign on use cases, then ensure that it is protected at the same level of assurance as authentication tokens.
- Implementation: If the web or application server supports it, then encrypting and/or signing the identifier (such as cookie) can protect the ID if intercepted.
- Design: Use strong session identifiers that are protected in transit and at rest.
- Implementation: Utilize a session timeout for all sessions, for example 20 minutes. If the user does not explicitly logout, the server terminates their session after this period of inactivity. If the user logs back in then a new session key is generated.
- Implementation: Verify authenticity of all identifiers at runtime.

## Source

- [MITRE CAPEC CAPEC-21](https://capec.mitre.org/data/definitions/21.html)
