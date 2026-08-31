---
slug: attack-pattern/CAPEC-662
title: "CAPEC-662 — Adversary in the Browser (AiTB)"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-662]
cwe_ids: [CWE-300, CWE-494]
mitre_ids: [T1185]
related: [weakness/CWE-300, weakness/CWE-494, technique/T1185]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-662
updated_at: 2026-08-31
summary: "An adversary exploits security vulnerabilities or inherent functionalities of a web browser, in order to manipulate traffic between two endpoints."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/662.html
---

# CAPEC-662: Adversary in the Browser (AiTB)

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Very High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary exploits security vulnerabilities or inherent functionalities of a web browser, in order to manipulate traffic between two endpoints.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-300](/wiki/p/weakness/CWE-300), [CWE-494](/wiki/p/weakness/CWE-494)

**ATT&CK techniques:** [T1185](/wiki/p/technique/T1185)

## Prerequisites

- The adversary must install or convince a user to install a Trojan.
- There are two components communicating with each other.
- An attacker is able to identify the nature and mechanism of communication between the two target components.
- Strong mutual authentication is not used between the two target components yielding opportunity for adversarial interposition.
- For browser pivoting, the SeDebugPrivilege and a high-integrity process must both exist to execute this attack.

## Skills required

- Medium: Tricking the victim into installing the Trojan is often the most difficult aspect of this attack. Afterwards, the remainder of this attack is fairly trivial.

## Consequences

- Integrity: Modify Data
- Confidentiality, Access Control, Authorization: Gain Privileges
- Confidentiality: Read Data

## Mitigations

- Ensure software and applications are only downloaded from legitimate and reputable sources, in addition to conducting integrity checks on the downloaded component.
- Leverage anti-malware tools, which can detect Trojan Horse malware.
- Use strong, out-of-band mutual authentication to always fully authenticate both ends of any communications channel.
- Limit user permissions to prevent browser pivoting.
- Ensure browser sessions are regularly terminated and when their effective lifetime ends.

## Source

- [MITRE CAPEC CAPEC-662](https://capec.mitre.org/data/definitions/662.html)
