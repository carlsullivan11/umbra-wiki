---
slug: attack-pattern/CAPEC-57
title: "CAPEC-57 — Utilizing REST's Trust in the System Resource to Obtain Sensitive Data"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-57]
cwe_ids: [CWE-287, CWE-300, CWE-693]
mitre_ids: [T1040]
related: [weakness/CWE-287, weakness/CWE-300, weakness/CWE-693, technique/T1040]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-57
updated_at: 2026-08-31
summary: "This attack utilizes a REST(REpresentational State Transfer)-style applications' trust in the system resources and environment to obtain sensitive data once SSL is terminated."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/57.html
---

# CAPEC-57: Utilizing REST's Trust in the System Resource to Obtain Sensitive Data

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Very High |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

This attack utilizes a REST(REpresentational State Transfer)-style applications' trust in the system resources and environment to obtain sensitive data once SSL is terminated.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-287](/wiki/p/weakness/CWE-287), [CWE-300](/wiki/p/weakness/CWE-300), [CWE-693](/wiki/p/weakness/CWE-693)

**ATT&CK techniques:** [T1040](/wiki/p/technique/T1040)

## Prerequisites

- Opportunity to intercept must exist beyond the point where SSL is terminated.
- The adversary must be able to insert a listener actively (proxying the communication) or passively (sniffing the communication) in the client-server communication path.

## Skills required

- Low: To insert a network sniffer or other listener into the communication stream

## Consequences

- Confidentiality, Access Control, Authorization: Gain Privileges

## Mitigations

- Implementation: Implement message level security such as HMAC in the HTTP communication
- Design: Utilize defense in depth, do not rely on a single security mechanism like SSL
- Design: Enforce principle of least privilege

## Source

- [MITRE CAPEC CAPEC-57](https://capec.mitre.org/data/definitions/57.html)
