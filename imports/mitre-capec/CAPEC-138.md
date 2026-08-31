---
slug: attack-pattern/CAPEC-138
title: "CAPEC-138 — Reflection Injection"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-138]
cwe_ids: [CWE-470]
related: [weakness/CWE-470]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-138
updated_at: 2026-08-31
summary: "An adversary supplies a value to the target application which is then used by reflection methods to identify a class, method, or field. For example, in the Java programming language the reflection libraries permit an application to inspect, load, and invoke classes and their comp…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/138.html
---

# CAPEC-138: Reflection Injection

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Very High |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary supplies a value to the target application which is then used by reflection methods to identify a class, method, or field. For example, in the Java programming language the reflection libraries permit an application to inspect, load, and invoke classes and their components by name. If an adversary can control the input into these methods including the name of the class/method/field or the parameters passed to methods, they can cause the targeted application to invoke incorrect methods, read random fields, or even to load and utilize malicious classes that the adversary created. This can lead to the application revealing sensitive information, returning incorrect results, or even having the adversary take control of the targeted application.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-470](/wiki/p/weakness/CWE-470)

## Prerequisites

- The target application must utilize reflection libraries and allow users to directly control the parameters to these methods. If the adversary can host classes where the target can invoke them, more powerful variants of this attack are possible.
- The target application must accept a string as user input, fail to sanitize characters that have a special meaning in the parameter encoding, and insert the user-supplied string in an encoding which is then processed.

## Source

- [MITRE CAPEC CAPEC-138](https://capec.mitre.org/data/definitions/138.html)
