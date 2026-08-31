---
slug: attack-pattern/CAPEC-212
title: "CAPEC-212 — Functionality Misuse"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-212]
cwe_ids: [CWE-1242, CWE-1246, CWE-1281]
related: [weakness/CWE-1242, weakness/CWE-1246, weakness/CWE-1281]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-212
updated_at: 2026-08-31
summary: "An adversary leverages a legitimate capability of an application in such a way as to achieve a negative technical impact. The system functionality is not altered or modified but used in a way that was not intended. This is often accomplished through the overuse of a specific func…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/212.html
---

# CAPEC-212: Functionality Misuse

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Medium |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary leverages a legitimate capability of an application in such a way as to achieve a negative technical impact. The system functionality is not altered or modified but used in a way that was not intended. This is often accomplished through the overuse of a specific functionality or by leveraging functionality with design flaws that enables the adversary to gain access to unauthorized, sensitive data.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-1242](/wiki/p/weakness/CWE-1242), [CWE-1246](/wiki/p/weakness/CWE-1246), [CWE-1281](/wiki/p/weakness/CWE-1281)

## Prerequisites

- The adversary has the capability to interact with the application directly.The target system does not adequately implement safeguards to prevent misuse of authorized actions/processes.

## Skills required

- Low: General computer knowledge about how applications are launched, how they interact with input/output, and how they are configured.

## Consequences

- Confidentiality: Gain Privileges
- Confidentiality, Integrity, Availability: Other

## Mitigations

- Perform comprehensive threat modeling, a process of identifying, evaluating, and mitigating potential threats to the application. This effort can help reveal potentially obscure application functionality that can be manipulated for malicious purposes.
- When implementing security features, consider how they can be misused and compromised.

## Source

- [MITRE CAPEC CAPEC-212](https://capec.mitre.org/data/definitions/212.html)
