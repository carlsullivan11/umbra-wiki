---
slug: attack-pattern/CAPEC-510
title: "CAPEC-510 — SaaS User Request Forgery"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-510]
cwe_ids: [CWE-346]
related: [weakness/CWE-346]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-510
updated_at: 2026-08-31
summary: "An adversary, through a previously installed malicious application, performs malicious actions against a third-party Software as a Service (SaaS) application (also known as a cloud based application) by leveraging the persistent and implicit trust placed on a trusted user's sessi…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/510.html
---

# CAPEC-510: SaaS User Request Forgery

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary, through a previously installed malicious application, performs malicious actions against a third-party Software as a Service (SaaS) application (also known as a cloud based application) by leveraging the persistent and implicit trust placed on a trusted user's session. This attack is executed after a trusted user is authenticated into a cloud service, "piggy-backing" on the authenticated session, and exploiting the fact that the cloud service believes it is only interacting with the trusted user. If successful, the actions embedded in the malicious application will be processed and accepted by the targeted SaaS application and executed at the trusted user's privilege level.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-346](/wiki/p/weakness/CWE-346)

## Prerequisites

- An adversary must be able install a purpose built malicious application onto the trusted user's system and convince the user to execute it while authenticated to the SaaS application.

## Skills required

- Medium: This attack pattern often requires the technical ability to modify a malicious software package (e.g. Zeus) to spider a targeted site and a way to trick a user into a malicious software download.

## Mitigations

- To limit one's exposure to this type of attack, tunnel communications through a secure proxy service.
- Detection of this type of attack can be done through heuristic analysis of behavioral anomalies (a la credit card fraud detection) which can be used to identify inhuman behavioral patterns. (e.g., spidering)

## Source

- [MITRE CAPEC CAPEC-510](https://capec.mitre.org/data/definitions/510.html)
