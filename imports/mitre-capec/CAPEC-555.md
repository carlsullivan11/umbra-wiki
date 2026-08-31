---
slug: attack-pattern/CAPEC-555
title: "CAPEC-555 — Remote Services with Stolen Credentials"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-555]
cwe_ids: [CWE-262, CWE-263, CWE-294, CWE-308, CWE-309, CWE-521, CWE-522]
mitre_ids: [T1021, T1114.002, T1133]
related: [weakness/CWE-262, weakness/CWE-263, weakness/CWE-294, weakness/CWE-308, weakness/CWE-309, weakness/CWE-521, weakness/CWE-522, technique/T1021, technique/T1114.002, technique/T1133]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-555
updated_at: 2026-08-31
summary: "This pattern of attack involves an adversary that uses stolen credentials to leverage remote services such as RDP, telnet, SSH, and VNC to log into a system. Once access is gained, any number of malicious activities could be performed."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/555.html
---

# CAPEC-555: Remote Services with Stolen Credentials

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Very High |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

This pattern of attack involves an adversary that uses stolen credentials to leverage remote services such as RDP, telnet, SSH, and VNC to log into a system. Once access is gained, any number of malicious activities could be performed.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-262](/wiki/p/weakness/CWE-262), [CWE-263](/wiki/p/weakness/CWE-263), [CWE-294](/wiki/p/weakness/CWE-294), [CWE-308](/wiki/p/weakness/CWE-308), [CWE-309](/wiki/p/weakness/CWE-309), [CWE-521](/wiki/p/weakness/CWE-521), [CWE-522](/wiki/p/weakness/CWE-522)

**ATT&CK techniques:** [T1021](/wiki/p/technique/T1021), [T1114.002](/wiki/p/technique/T1114.002), [T1133](/wiki/p/technique/T1133)

## Mitigations

- Disable RDP, telnet, SSH and enable firewall rules to block such traffic. Limit users and accounts that have remote interactive login access. Remove the Local Administrators group from the list of groups allowed to login through RDP. Limit remote user permissions. Use remote desktop gateways and multifactor authentication for remote logins.

## Source

- [MITRE CAPEC CAPEC-555](https://capec.mitre.org/data/definitions/555.html)
