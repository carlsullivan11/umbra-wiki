---
slug: attack-pattern/CAPEC-182
title: "CAPEC-182 — Flash Injection"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-182]
cwe_ids: [CWE-20, CWE-184, CWE-697]
related: [weakness/CWE-20, weakness/CWE-184, weakness/CWE-697]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-182
updated_at: 2026-08-31
summary: "An attacker tricks a victim to execute malicious flash content that executes commands or makes flash calls specified by the attacker. One example of this attack is cross-site flashing, an attacker controlled parameter to a reference call loads from content specified by the attack…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/182.html
---

# CAPEC-182: Flash Injection

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker tricks a victim to execute malicious flash content that executes commands or makes flash calls specified by the attacker. One example of this attack is cross-site flashing, an attacker controlled parameter to a reference call loads from content specified by the attacker.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-20](/wiki/p/weakness/CWE-20), [CWE-184](/wiki/p/weakness/CWE-184), [CWE-697](/wiki/p/weakness/CWE-697)

## Prerequisites

- The target must be capable of running Flash applications. In some cases, the victim must follow an attacker-supplied link.

## Skills required

- Medium: The attacker needs to have knowledge of Flash, especially how to insert content the executes commands.

## Consequences

- Confidentiality: Other
- Integrity: Modify Data
- Confidentiality: Read Data
- Authorization: Execute Unauthorized Commands
- Accountability, Authentication, Authorization, Non-Repudiation: Gain Privileges
- Access Control, Authorization: Bypass Protection Mechanism

## Mitigations

- Implementation: remove sensitive information such as user name and password in the SWF file.
- Implementation: use validation on both client and server side.
- Implementation: remove debug information.
- Implementation: use SSL when loading external data
- Implementation: use crossdomain.xml file to allow the application domain to load stuff or the SWF file called by other domain.

## Source

- [MITRE CAPEC CAPEC-182](https://capec.mitre.org/data/definitions/182.html)
