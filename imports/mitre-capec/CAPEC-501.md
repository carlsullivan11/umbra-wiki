---
slug: attack-pattern/CAPEC-501
title: "CAPEC-501 — Android Activity Hijack"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-501]
cwe_ids: [CWE-923]
related: [weakness/CWE-923]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-501
updated_at: 2026-08-31
summary: "An adversary intercepts an implicit intent sent to launch a Android-based trusted activity and instead launches a counterfeit activity in its place. The malicious activity is then used to mimic the trusted activity's user interface and prompt the target to enter sensitive data as…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/501.html
---

# CAPEC-501: Android Activity Hijack

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary intercepts an implicit intent sent to launch a Android-based trusted activity and instead launches a counterfeit activity in its place. The malicious activity is then used to mimic the trusted activity's user interface and prompt the target to enter sensitive data as if they were interacting with the trusted activity.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-923](/wiki/p/weakness/CWE-923)

## Prerequisites

- The adversary must have previously installed the malicious application onto the Android device that will run in place of the trusted activity.

## Skills required

- High: The adversary must typically overcome network and host defenses in order to place malware on the system.

## Consequences

- Confidentiality: Read Data

## Mitigations

- To mitigate this type of an attack, explicit intents should be used whenever sensitive data is being sent. An 'explicit intent' is delivered to a specific application as declared within the intent, whereas an 'implicit intent' is directed to an application as defined by the Android operating system. If an implicit intent must be used, then it should be assumed that the intent will be received by an unknown application and any response should be treated accordingly (i.e., with appropriate security controls).
- Never use implicit intents for inter-application communication.

## Source

- [MITRE CAPEC CAPEC-501](https://capec.mitre.org/data/definitions/501.html)
