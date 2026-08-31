---
slug: attack-pattern/CAPEC-384
title: "CAPEC-384 — Application API Message Manipulation via Man-in-the-Middle"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-384]
cwe_ids: [CWE-311, CWE-345, CWE-346, CWE-471, CWE-602]
related: [weakness/CWE-311, weakness/CWE-345, weakness/CWE-346, weakness/CWE-471, weakness/CWE-602]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-384
updated_at: 2026-08-31
summary: "An attacker manipulates either egress or ingress data from a client within an application framework in order to change the content of messages. Performing this attack can allow the attacker to gain unauthorized privileges within the application, or conduct attacks such as phishin…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/384.html
---

# CAPEC-384: Application API Message Manipulation via Man-in-the-Middle

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Low |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker manipulates either egress or ingress data from a client within an application framework in order to change the content of messages. Performing this attack can allow the attacker to gain unauthorized privileges within the application, or conduct attacks such as phishing, deceptive strategies to spread malware, or traditional web-application attacks. The techniques require use of specialized software that allow the attacker to perform adversary-in-the-middle (CAPEC-94) communications between the web browser and the remote system. Despite the use of AiTH software, the attack is actually directed at the server, as the client is one node in a series of content brokers that pass information along to the application framework. Additionally, it is not true "Adversary-in-the-Middle" attack at the network layer, but an application-layer attack the root cause of which is the master applications trust in the integrity of code supplied by the client.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-311](/wiki/p/weakness/CWE-311), [CWE-345](/wiki/p/weakness/CWE-345), [CWE-346](/wiki/p/weakness/CWE-346), [CWE-471](/wiki/p/weakness/CWE-471), [CWE-602](/wiki/p/weakness/CWE-602)

## Prerequisites

- Targeted software is utilizing application framework APIs

## Source

- [MITRE CAPEC CAPEC-384](https://capec.mitre.org/data/definitions/384.html)
