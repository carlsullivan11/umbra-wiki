---
slug: attack-pattern/CAPEC-593
title: "CAPEC-593 — Session Hijacking"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-593]
cwe_ids: [CWE-287]
mitre_ids: [T1185, T1550.001, T1563]
related: [weakness/CWE-287, technique/T1185, technique/T1550.001, technique/T1563]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-593
updated_at: 2026-08-31
summary: "This type of attack involves an adversary that exploits weaknesses in an application's use of sessions in performing authentication. The adversary is able to steal or manipulate an active session and use it to gain unathorized access to the application."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/593.html
---

# CAPEC-593: Session Hijacking

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Very High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

This type of attack involves an adversary that exploits weaknesses in an application's use of sessions in performing authentication. The adversary is able to steal or manipulate an active session and use it to gain unathorized access to the application.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-287](/wiki/p/weakness/CWE-287)

**ATT&CK techniques:** [T1185](/wiki/p/technique/T1185), [T1550.001](/wiki/p/technique/T1550.001), [T1563](/wiki/p/technique/T1563)

## Prerequisites

- An application that leverages sessions to perform authentication.

## Skills required

- Low: Exploiting a poorly protected identity token is a well understood attack with many helpful resources available.

## Consequences

- Confidentiality, Integrity, Availability: Gain Privileges

## Mitigations

- Properly encrypt and sign identity tokens in transit, and use industry standard session key generation mechanisms that utilize high amount of entropy to generate the session key. Many standard web and application servers will perform this task on your behalf. Utilize a session timeout for all sessions. If the user does not explicitly logout, terminate their session after this period of inactivity. If the user logs back in then a new session key should be generated.

## Source

- [MITRE CAPEC CAPEC-593](https://capec.mitre.org/data/definitions/593.html)
