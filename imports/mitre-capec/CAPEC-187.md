---
slug: attack-pattern/CAPEC-187
title: "CAPEC-187 — Malicious Automated Software Update via Redirection"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-187]
cwe_ids: [CWE-494]
mitre_ids: [T1072]
related: [weakness/CWE-494, technique/T1072]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-187
updated_at: 2026-08-31
summary: "An attacker exploits two layers of weaknesses in server or client software for automated update mechanisms to undermine the integrity of the target code-base. The first weakness involves a failure to properly authenticate a server as a source of update or patch content. This type…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/187.html
---

# CAPEC-187: Malicious Automated Software Update via Redirection

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker exploits two layers of weaknesses in server or client software for automated update mechanisms to undermine the integrity of the target code-base. The first weakness involves a failure to properly authenticate a server as a source of update or patch content. This type of weakness typically results from authentication mechanisms which can be defeated, allowing a hostile server to satisfy the criteria that establish a trust relationship. The second weakness is a systemic failure to validate the identity and integrity of code downloaded from a remote location, hence the inability to distinguish malicious code from a legitimate update.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-494](/wiki/p/weakness/CWE-494)

**ATT&CK techniques:** [T1072](/wiki/p/technique/T1072)

## Consequences

- Access Control, Availability, Confidentiality: Execute Unauthorized Commands

## Source

- [MITRE CAPEC CAPEC-187](https://capec.mitre.org/data/definitions/187.html)
