---
slug: attack-pattern/CAPEC-469
title: "CAPEC-469 — HTTP DoS"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-469]
cwe_ids: [CWE-770, CWE-772]
mitre_ids: [T1499.002]
related: [weakness/CWE-770, weakness/CWE-772, technique/T1499.002]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-469
updated_at: 2026-08-31
summary: "An attacker performs flooding at the HTTP level to bring down only a particular web application rather than anything listening on a TCP/IP connection. This denial of service attack requires substantially fewer packets to be sent which makes DoS harder to detect. This is an equiva…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/469.html
---

# CAPEC-469: HTTP DoS

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Low |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker performs flooding at the HTTP level to bring down only a particular web application rather than anything listening on a TCP/IP connection. This denial of service attack requires substantially fewer packets to be sent which makes DoS harder to detect. This is an equivalent of SYN flood in HTTP. The idea is to keep the HTTP session alive indefinitely and then repeat that hundreds of times. This attack targets resource depletion weaknesses in web server software. The web server will wait to attacker's responses on the initiated HTTP sessions while the connection threads are being exhausted.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-770](/wiki/p/weakness/CWE-770), [CWE-772](/wiki/p/weakness/CWE-772)

**ATT&CK techniques:** [T1499.002](/wiki/p/technique/T1499.002)

## Prerequisites

- HTTP protocol is usedWeb server used is vulnerable to denial of service via HTTP flooding

## Mitigations

- Configuration: Configure web server software to limit the waiting period on opened HTTP sessions
- Design: Use load balancing mechanisms

## Source

- [MITRE CAPEC CAPEC-469](https://capec.mitre.org/data/definitions/469.html)
