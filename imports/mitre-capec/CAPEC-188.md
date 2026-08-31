---
slug: attack-pattern/CAPEC-188
title: "CAPEC-188 — Reverse Engineering"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-188]
cwe_ids: [CWE-1278]
related: [weakness/CWE-1278]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-188
updated_at: 2026-08-31
summary: "An adversary discovers the structure, function, and composition of an object, resource, or system by using a variety of analysis techniques to effectively determine how the analyzed entity was constructed or operates. The goal of reverse engineering is often to duplicate the func…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/188.html
---

# CAPEC-188: Reverse Engineering

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Low |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary discovers the structure, function, and composition of an object, resource, or system by using a variety of analysis techniques to effectively determine how the analyzed entity was constructed or operates. The goal of reverse engineering is often to duplicate the function, or a part of the function, of an object in order to duplicate or "back engineer" some aspect of its functioning. Reverse engineering techniques can be applied to mechanical objects, electronic devices, or software, although the methodology and techniques involved in each type of analysis differ widely.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-1278](/wiki/p/weakness/CWE-1278)

## Prerequisites

- Access to targeted system, resources, and information.

## Skills required

- High: Understanding of low level programming languages or technologies can be very helpful. For example, when reverse engineering a binary file, an understanding of assembly languages can help to determine the purpose and inner-workings of the code. Another example is reverse engineering an application that relies on networking. Here, an understanding networking protocols can provide insight into application details.

## Mitigations

- Employ code obfuscation techniques to prevent the adversary from reverse engineering the targeted entity.

## Source

- [MITRE CAPEC CAPEC-188](https://capec.mitre.org/data/definitions/188.html)
