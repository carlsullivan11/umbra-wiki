---
slug: attack-pattern/CAPEC-277
title: "CAPEC-277 — Data Interchange Protocol Manipulation"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-277]
cwe_ids: [CWE-707]
related: [weakness/CWE-707]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-277
updated_at: 2026-08-31
summary: "Data Interchange Protocols are used to transmit structured data between entities. These protocols are often specific to a particular domain (B2B: purchase orders, invoices, transport logistics and waybills, medical records). They are often, but not always, XML-based. Subverting t…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/277.html
---

# CAPEC-277: Data Interchange Protocol Manipulation

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | — |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

Data Interchange Protocols are used to transmit structured data between entities. These protocols are often specific to a particular domain (B2B: purchase orders, invoices, transport logistics and waybills, medical records). They are often, but not always, XML-based. Subverting the protocol can allow an adversary to impersonate others, discover sensitive information, control the outcome of a session, or perform other attacks. This type of attack targets invalid assumptions that may be inherent in implementers of the protocol, incorrect implementations of the protocol, or vulnerabilities in the protocol itself.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-707](/wiki/p/weakness/CWE-707)

## Source

- [MITRE CAPEC CAPEC-277](https://capec.mitre.org/data/definitions/277.html)
