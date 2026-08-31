---
slug: attack-pattern/CAPEC-480
title: "CAPEC-480 — Escaping Virtualization"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-480]
cwe_ids: [CWE-693]
mitre_ids: [T1611]
related: [weakness/CWE-693, technique/T1611]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-480
updated_at: 2026-08-31
summary: "An adversary gains access to an application, service, or device with the privileges of an authorized or privileged user by escaping the confines of a virtualized environment. The adversary is then able to access resources or execute unauthorized code within the host environment, …"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/480.html
---

# CAPEC-480: Escaping Virtualization

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Very High |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary gains access to an application, service, or device with the privileges of an authorized or privileged user by escaping the confines of a virtualized environment. The adversary is then able to access resources or execute unauthorized code within the host environment, generally with the privileges of the user running the virtualized process. Successfully executing an attack of this type is often the first step in executing more complex attacks.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-693](/wiki/p/weakness/CWE-693)

**ATT&CK techniques:** [T1611](/wiki/p/technique/T1611)

## Consequences

- Access Control, Authorization: Bypass Protection Mechanism
- Authorization: Execute Unauthorized Commands
- Accountability, Authentication, Authorization, Non-Repudiation: Gain Privileges

## Mitigations

- Ensure virtualization software is current and up-to-date.
- Abide by the least privilege principle to avoid assigning users more privileges than necessary.

## Source

- [MITRE CAPEC CAPEC-480](https://capec.mitre.org/data/definitions/480.html)
