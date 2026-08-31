---
slug: attack-pattern/CAPEC-644
title: "CAPEC-644 — Use of Captured Hashes (Pass The Hash)"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-644]
cwe_ids: [CWE-294, CWE-308, CWE-522, CWE-836]
mitre_ids: [T1550.002]
related: [weakness/CWE-294, weakness/CWE-308, weakness/CWE-522, weakness/CWE-836, technique/T1550.002]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-644
updated_at: 2026-08-31
summary: "An adversary obtains (i.e. steals or purchases) legitimate Windows domain credential hash values to access systems within the domain that leverage the Lan Man (LM) and/or NT Lan Man (NTLM) authentication protocols."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/644.html
---

# CAPEC-644: Use of Captured Hashes (Pass The Hash)

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | High |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary obtains (i.e. steals or purchases) legitimate Windows domain credential hash values to access systems within the domain that leverage the Lan Man (LM) and/or NT Lan Man (NTLM) authentication protocols.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-294](/wiki/p/weakness/CWE-294), [CWE-308](/wiki/p/weakness/CWE-308), [CWE-522](/wiki/p/weakness/CWE-522), [CWE-836](/wiki/p/weakness/CWE-836)

**ATT&CK techniques:** [T1550.002](/wiki/p/technique/T1550.002)

## Prerequisites

- The system/application is connected to the Windows domain.
- The system/application leverages the Lan Man (LM) and/or NT Lan Man (NTLM) authentication protocols.
- The adversary possesses known Windows credential hash value pairs that exist on the target domain.

## Skills required

- Low: Once an adversary obtains a known Windows credential hash value pair, leveraging it is trivial.

## Consequences

- Confidentiality, Access Control, Authentication: Gain Privileges
- Confidentiality, Authorization: Read Data
- Integrity: Modify Data

## Mitigations

- Prevent the use of Lan Man and NT Lan Man authentication on severs and apply patch KB2871997 to Windows 7 and higher systems.
- Leverage multi-factor authentication for all authentication services and prior to granting an entity access to the domain network.
- Monitor system and domain logs for abnormal credential access.
- Create a strong password policy and ensure that your system enforces this policy.
- Leverage system penetration testing and other defense in depth methods to determine vulnerable systems within a domain.

## Source

- [MITRE CAPEC CAPEC-644](https://capec.mitre.org/data/definitions/644.html)
