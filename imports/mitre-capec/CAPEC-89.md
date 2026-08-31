---
slug: attack-pattern/CAPEC-89
title: "CAPEC-89 — Pharming"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-89]
cwe_ids: [CWE-346, CWE-350]
related: [weakness/CWE-346, weakness/CWE-350]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-89
updated_at: 2026-08-31
summary: "A pharming attack occurs when the victim is fooled into entering sensitive data into supposedly trusted locations, such as an online bank site or a trading platform. An attacker can impersonate these supposedly trusted sites and have the victim be directed to their site rather th…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/89.html
---

# CAPEC-89: Pharming

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Very High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

A pharming attack occurs when the victim is fooled into entering sensitive data into supposedly trusted locations, such as an online bank site or a trading platform. An attacker can impersonate these supposedly trusted sites and have the victim be directed to their site rather than the originally intended one. Pharming does not require script injection or clicking on malicious links for the attack to succeed.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-346](/wiki/p/weakness/CWE-346), [CWE-350](/wiki/p/weakness/CWE-350)

## Prerequisites

- Vulnerable DNS software or improperly protected hosts file or router that can be poisoned
- A website that handles sensitive information but does not use a secure connection and a certificate that is valid is also prone to pharming

## Skills required

- Medium: The attacker needs to be able to poison the resolver - DNS entries or local hosts file or router entry pointing to a trusted DNS server - in order to successfully carry out a pharming attack. Setting up a fake website, identical to the targeted one, does not require special skills.

## Consequences

- Confidentiality: Read Data

## Mitigations

- All sensitive information must be handled over a secure connection.
- Known vulnerabilities in DNS or router software or in operating systems must be patched as soon as a fix has been released and tested.
- End users must ensure that they provide sensitive information only to websites that they trust, over a secure connection with a valid certificate issued by a well-known certificate authority.

## Source

- [MITRE CAPEC CAPEC-89](https://capec.mitre.org/data/definitions/89.html)
