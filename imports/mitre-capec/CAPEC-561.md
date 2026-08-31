---
slug: attack-pattern/CAPEC-561
title: "CAPEC-561 — Windows Admin Shares with Stolen Credentials"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-561]
cwe_ids: [CWE-262, CWE-263, CWE-294, CWE-308, CWE-309, CWE-521, CWE-522]
mitre_ids: [T1021.002]
related: [weakness/CWE-262, weakness/CWE-263, weakness/CWE-294, weakness/CWE-308, weakness/CWE-309, weakness/CWE-521, weakness/CWE-522, technique/T1021.002]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-561
updated_at: 2026-08-31
summary: "An adversary guesses or obtains (i.e. steals or purchases) legitimate Windows administrator credentials (e.g. userID/password) to access Windows Admin Shares on a local machine or within a Windows domain."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/561.html
---

# CAPEC-561: Windows Admin Shares with Stolen Credentials

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | — |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary guesses or obtains (i.e. steals or purchases) legitimate Windows administrator credentials (e.g. userID/password) to access Windows Admin Shares on a local machine or within a Windows domain.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-262](/wiki/p/weakness/CWE-262), [CWE-263](/wiki/p/weakness/CWE-263), [CWE-294](/wiki/p/weakness/CWE-294), [CWE-308](/wiki/p/weakness/CWE-308), [CWE-309](/wiki/p/weakness/CWE-309), [CWE-521](/wiki/p/weakness/CWE-521), [CWE-522](/wiki/p/weakness/CWE-522)

**ATT&CK techniques:** [T1021.002](/wiki/p/technique/T1021.002)

## Prerequisites

- The system/application is connected to the Windows domain.
- The target administrative share allows remote use of local admin credentials to log into domain systems.
- The adversary possesses a list of known Windows administrator credentials that exist on the target domain.

## Skills required

- Low: Once an adversary obtains a known Windows credential, leveraging it is trivial.

## Consequences

- Confidentiality, Access Control, Authentication: Gain Privileges
- Confidentiality, Authorization: Read Data
- Integrity: Modify Data

## Mitigations

- Do not reuse local administrator account credentials across systems.
- Deny remote use of local admin credentials to log into domain systems.
- Do not allow accounts to be a local administrator on more than one system.

## Source

- [MITRE CAPEC CAPEC-561](https://capec.mitre.org/data/definitions/561.html)
