---
slug: attack-pattern/CAPEC-11
title: "CAPEC-11 — Cause Web Server Misclassification"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-11]
cwe_ids: [CWE-430]
mitre_ids: [T1036.006]
related: [weakness/CWE-430, technique/T1036.006]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-11
updated_at: 2026-08-31
summary: "An attack of this type exploits a Web server's decision to take action based on filename or file extension. Because different file types are handled by different server processes, misclassification may force the Web server to take unexpected action, or expected actions in an unex…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/11.html
---

# CAPEC-11: Cause Web Server Misclassification

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attack of this type exploits a Web server's decision to take action based on filename or file extension. Because different file types are handled by different server processes, misclassification may force the Web server to take unexpected action, or expected actions in an unexpected sequence. This may cause the server to exhaust resources, supply debug or system data to the attacker, or bind an attacker to a remote process.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-430](/wiki/p/weakness/CWE-430)

**ATT&CK techniques:** [T1036.006](/wiki/p/technique/T1036.006)

## Prerequisites

- Web server software must rely on file name or file extension for processing.
- The attacker must be able to make HTTP requests to the web server.

## Skills required

- Low: To modify file name or file extension
- Medium: To use misclassification to force the Web server to disclose configuration information, source, or binary data

## Consequences

- Confidentiality: Read Data
- Confidentiality, Access Control, Authorization: Gain Privileges

## Mitigations

- Implementation: Server routines should be determined by content not determined by filename or file extension.

## Source

- [MITRE CAPEC CAPEC-11](https://capec.mitre.org/data/definitions/11.html)
