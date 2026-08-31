---
slug: attack-pattern/CAPEC-385
title: "CAPEC-385 — Transaction or Event Tampering via Application API Manipulation"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-385]
cwe_ids: [CWE-311, CWE-345, CWE-346, CWE-471, CWE-602]
related: [weakness/CWE-311, weakness/CWE-345, weakness/CWE-346, weakness/CWE-471, weakness/CWE-602]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-385
updated_at: 2026-08-31
summary: "An attacker hosts or joins an event or transaction within an application framework in order to change the content of messages or items that are being exchanged. Performing this attack allows the attacker to manipulate content in such a way as to produce messages or content that l…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/385.html
---

# CAPEC-385: Transaction or Event Tampering via Application API Manipulation

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker hosts or joins an event or transaction within an application framework in order to change the content of messages or items that are being exchanged. Performing this attack allows the attacker to manipulate content in such a way as to produce messages or content that look authentic but may contain deceptive links, substitute one item or another, spoof an existing item and conduct a false exchange, or otherwise change the amounts or identity of what is being exchanged. The techniques require use of specialized software that allow the attacker to man-in-the-middle communications between the web browser and the remote system in order to change the content of various application elements. Often, items exchanged in game can be monetized via sales for coin, virtual dollars, etc. The purpose of the attack is for the attack to scam the victim by trapping the data packets involved the exchange and altering the integrity of the transfer process.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-311](/wiki/p/weakness/CWE-311), [CWE-345](/wiki/p/weakness/CWE-345), [CWE-346](/wiki/p/weakness/CWE-346), [CWE-471](/wiki/p/weakness/CWE-471), [CWE-602](/wiki/p/weakness/CWE-602)

## Prerequisites

- Targeted software is utilizing application framework APIs

## Source

- [MITRE CAPEC CAPEC-385](https://capec.mitre.org/data/definitions/385.html)
