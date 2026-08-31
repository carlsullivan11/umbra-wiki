---
slug: attack-pattern/CAPEC-102
title: "CAPEC-102 — Session Sidejacking"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-102]
cwe_ids: [CWE-294, CWE-319, CWE-522, CWE-523, CWE-614]
related: [weakness/CWE-294, weakness/CWE-319, weakness/CWE-522, weakness/CWE-523, weakness/CWE-614]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-102
updated_at: 2026-08-31
summary: "Session sidejacking takes advantage of an unencrypted communication channel between a victim and target system. The attacker sniffs traffic on a network looking for session tokens in unencrypted traffic. Once a session token is captured, the attacker performs malicious actions by…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/102.html
---

# CAPEC-102: Session Sidejacking

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

Session sidejacking takes advantage of an unencrypted communication channel between a victim and target system. The attacker sniffs traffic on a network looking for session tokens in unencrypted traffic. Once a session token is captured, the attacker performs malicious actions by using the stolen token with the targeted application to impersonate the victim. This attack is a specific method of session hijacking, which is exploiting a valid session token to gain unauthorized access to a target system or information. Other methods to perform a session hijacking are session fixation, cross-site scripting, or compromising a user or server machine and stealing the session token.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-294](/wiki/p/weakness/CWE-294), [CWE-319](/wiki/p/weakness/CWE-319), [CWE-522](/wiki/p/weakness/CWE-522), [CWE-523](/wiki/p/weakness/CWE-523), [CWE-614](/wiki/p/weakness/CWE-614)

## Prerequisites

- An attacker and the victim are both using the same WiFi network.
- The victim has an active session with a target system.
- The victim is not using a secure channel to communicate with the target system (e.g. SSL, VPN, etc.)
- The victim initiated communication with a target system that requires transfer of the session token or the target application uses AJAX and thereby periodically "rings home" asynchronously using the session token

## Skills required

- Low: Easy to use tools exist to automate this attack.

## Consequences

- Confidentiality, Access Control, Authorization: Gain Privileges
- Integrity: Modify Data
- Confidentiality: Read Data
- Availability: Unreliable Execution

## Mitigations

- Make sure that HTTPS is used to communicate with the target system. Alternatively, use VPN if possible. It is important to ensure that all communication between the client and the server happens via an encrypted secure channel.
- Modify the session token with each transmission and protect it with cryptography. Add the idea of request sequencing that gives the server an ability to detect replay attacks.

## Source

- [MITRE CAPEC CAPEC-102](https://capec.mitre.org/data/definitions/102.html)
