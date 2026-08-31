---
slug: attack-pattern/CAPEC-155
title: "CAPEC-155 — Screen Temporary Files for Sensitive Information"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-155]
cwe_ids: [CWE-377]
related: [weakness/CWE-377]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-155
updated_at: 2026-08-31
summary: "An adversary exploits the temporary, insecure storage of information by monitoring the content of files used to store temp data during an application's routine execution flow. Many applications use temporary files to accelerate processing or to provide records of state across mul…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/155.html
---

# CAPEC-155: Screen Temporary Files for Sensitive Information

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary exploits the temporary, insecure storage of information by monitoring the content of files used to store temp data during an application's routine execution flow. Many applications use temporary files to accelerate processing or to provide records of state across multiple executions of the application. Sometimes, however, these temporary files may end up storing sensitive information. By screening an application's temporary files, an adversary might be able to discover such sensitive information. For example, web browsers often cache content to accelerate subsequent lookups. If the content contains sensitive information then the adversary could recover this from the web cache.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-377](/wiki/p/weakness/CWE-377)

## Prerequisites

- The target application must utilize temporary files and must fail to adequately secure them against other parties reading them.

## Source

- [MITRE CAPEC CAPEC-155](https://capec.mitre.org/data/definitions/155.html)
