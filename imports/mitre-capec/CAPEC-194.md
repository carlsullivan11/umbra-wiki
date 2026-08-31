---
slug: attack-pattern/CAPEC-194
title: "CAPEC-194 — Fake the Source of Data"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-194]
cwe_ids: [CWE-287]
related: [weakness/CWE-287]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-194
updated_at: 2026-08-31
summary: "An adversary takes advantage of improper authentication to provide data or services under a falsified identity. The purpose of using the falsified identity may be to prevent traceability of the provided data or to assume the rights granted to another individual. One of the simple…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/194.html
---

# CAPEC-194: Fake the Source of Data

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Medium |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary takes advantage of improper authentication to provide data or services under a falsified identity. The purpose of using the falsified identity may be to prevent traceability of the provided data or to assume the rights granted to another individual. One of the simplest forms of this attack would be the creation of an email message with a modified "From" field in order to appear that the message was sent from someone other than the actual sender. The root of the attack (in this case the email system) fails to properly authenticate the source and this results in the reader incorrectly performing the instructed action. Results of the attack vary depending on the details of the attack, but common results include privilege escalation, obfuscation of other attacks, and data corruption/manipulation.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-287](/wiki/p/weakness/CWE-287)

## Prerequisites

- This attack is only applicable when a vulnerable entity associates data or services with an identity. Without such an association, there would be no reason to fake the source.

## Consequences

- Integrity: Alter Execution Logic
- Integrity: Gain Privileges
- Integrity: Hide Activities

## Source

- [MITRE CAPEC CAPEC-194](https://capec.mitre.org/data/definitions/194.html)
