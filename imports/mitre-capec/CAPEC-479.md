---
slug: attack-pattern/CAPEC-479
title: "CAPEC-479 — Malicious Root Certificate"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-479]
cwe_ids: [CWE-284]
mitre_ids: [T1553.004]
related: [weakness/CWE-284, technique/T1553.004]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-479
updated_at: 2026-08-31
summary: "An adversary exploits a weakness in authorization and installs a new root certificate on a compromised system. Certificates are commonly used for establishing secure TLS/SSL communications within a web browser. When a user attempts to browse a website that presents a certificate …"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/479.html
---

# CAPEC-479: Malicious Root Certificate

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Low |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary exploits a weakness in authorization and installs a new root certificate on a compromised system. Certificates are commonly used for establishing secure TLS/SSL communications within a web browser. When a user attempts to browse a website that presents a certificate that is not trusted an error message will be displayed to warn the user of the security risk. Depending on the security settings, the browser may not allow the user to establish a connection to the website. Adversaries have used this technique to avoid security warnings prompting users when compromised systems connect over HTTPS to adversary controlled web servers that spoof legitimate websites in order to collect login credentials.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-284](/wiki/p/weakness/CWE-284)

**ATT&CK techniques:** [T1553.004](/wiki/p/technique/T1553.004)

## Prerequisites

- The adversary must have the ability to create a new root certificate.

## Source

- [MITRE CAPEC CAPEC-479](https://capec.mitre.org/data/definitions/479.html)
