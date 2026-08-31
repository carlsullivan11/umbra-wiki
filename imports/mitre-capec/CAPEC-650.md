---
slug: attack-pattern/CAPEC-650
title: "CAPEC-650 — Upload a Web Shell to a Web Server"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-650]
cwe_ids: [CWE-287, CWE-553]
mitre_ids: [T1505.003]
related: [weakness/CWE-287, weakness/CWE-553, technique/T1505.003]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-650
updated_at: 2026-08-31
summary: "By exploiting insufficient permissions, it is possible to upload a web shell to a web server in such a way that it can be executed remotely. This shell can have various capabilities, thereby acting as a 'gateway' to the underlying web server. The shell might execute at the higher…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/650.html
---

# CAPEC-650: Upload a Web Shell to a Web Server

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

By exploiting insufficient permissions, it is possible to upload a web shell to a web server in such a way that it can be executed remotely. This shell can have various capabilities, thereby acting as a "gateway" to the underlying web server. The shell might execute at the higher permission level of the web server, providing the ability the execute malicious code at elevated levels.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-287](/wiki/p/weakness/CWE-287), [CWE-553](/wiki/p/weakness/CWE-553)

**ATT&CK techniques:** [T1505.003](/wiki/p/technique/T1505.003)

## Prerequisites

- The web server is susceptible to one of the various web application exploits that allows for uploading a shell file.

## Consequences

- Confidentiality: Read Data
- Confidentiality, Access Control, Authorization: Gain Privileges
- Confidentiality, Integrity, Availability: Execute Unauthorized Commands

## Mitigations

- Make sure your web server is up-to-date with all patches to protect against known vulnerabilities.
- Ensure that the file permissions in directories on the web server from which files can be execute is set to the "least privilege" settings, and that those directories contents is controlled by an allowlist.

## Source

- [MITRE CAPEC CAPEC-650](https://capec.mitre.org/data/definitions/650.html)
