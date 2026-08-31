---
slug: attack-pattern/CAPEC-104
title: "CAPEC-104 — Cross Zone Scripting"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-104]
cwe_ids: [CWE-20, CWE-116, CWE-250, CWE-285, CWE-638]
related: [weakness/CWE-20, weakness/CWE-116, weakness/CWE-250, weakness/CWE-285, weakness/CWE-638]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-104
updated_at: 2026-08-31
summary: "An attacker is able to cause a victim to load content into their web-browser that bypasses security zone controls and gain access to increased privileges to execute scripting code or other web objects such as unsigned ActiveX controls or applets. This is a privilege elevation att…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/104.html
---

# CAPEC-104: Cross Zone Scripting

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker is able to cause a victim to load content into their web-browser that bypasses security zone controls and gain access to increased privileges to execute scripting code or other web objects such as unsigned ActiveX controls or applets. This is a privilege elevation attack targeted at zone-based web-browser security.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-20](/wiki/p/weakness/CWE-20), [CWE-116](/wiki/p/weakness/CWE-116), [CWE-250](/wiki/p/weakness/CWE-250), [CWE-285](/wiki/p/weakness/CWE-285), [CWE-638](/wiki/p/weakness/CWE-638)

## Prerequisites

- The target must be using a zone-aware browser.

## Skills required

- Medium: Ability to craft malicious scripts or find them elsewhere and ability to identify functionality that is running web controls in the local zone and to find an injection vector into that functionality

## Consequences

- Integrity: Modify Data
- Confidentiality: Read Data
- Confidentiality, Access Control, Authorization: Gain Privileges
- Confidentiality, Integrity, Availability: Execute Unauthorized Commands

## Mitigations

- Disable script execution.
- Ensure that sufficient input validation is performed for any potentially untrusted data before it is used in any privileged context or zone
- Limit the flow of untrusted data into the privileged areas of the system that run in the higher trust zone
- Limit the sites that are being added to the local machine zone and restrict the privileges of the code running in that zone to the bare minimum
- Ensure proper HTML output encoding before writing user supplied data to the page

## Source

- [MITRE CAPEC CAPEC-104](https://capec.mitre.org/data/definitions/104.html)
