---
slug: attack-pattern/CAPEC-268
title: "CAPEC-268 — Audit Log Manipulation"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-268]
cwe_ids: [CWE-117]
mitre_ids: [T1070, T1562.002, T1562.003, T1562.008]
related: [weakness/CWE-117, technique/T1070]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-268
updated_at: 2026-08-31
summary: "The attacker injects, manipulates, deletes, or forges malicious log entries into the log file, in an attempt to mislead an audit of the log file or cover tracks of an attack. Due to either insufficient access controls of the log files or the logging mechanism, the attacker is abl…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/268.html
---

# CAPEC-268: Audit Log Manipulation

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | — |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

The attacker injects, manipulates, deletes, or forges malicious log entries into the log file, in an attempt to mislead an audit of the log file or cover tracks of an attack. Due to either insufficient access controls of the log files or the logging mechanism, the attacker is able to perform such actions.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-117](/wiki/p/weakness/CWE-117)

**ATT&CK techniques:** [T1070](/wiki/p/technique/T1070), [T1562.002](/wiki/p/technique/T1562.002), [T1562.003](/wiki/p/technique/T1562.003), [T1562.008](/wiki/p/technique/T1562.008)

## Prerequisites

- The target host is logging the action and data of the user.
- The target host insufficiently protects access to the logs or logging mechanisms.

## Mappings that no longer resolve

CAPEC 3.9 (2023-01-24) maps this pattern to `T1562.002`, `T1562.003`, `T1562.008`, which the current ATT&CK corpus does not carry — MITRE has revoked or relocated them since CAPEC was last published. The mapping is recorded here rather than dropped, because a stale cross-reference is a fact about the taxonomies, not a gap in this page.

## Source

- [MITRE CAPEC CAPEC-268](https://capec.mitre.org/data/definitions/268.html)
