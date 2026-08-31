---
slug: attack-pattern/CAPEC-180
title: "CAPEC-180 — Exploiting Incorrectly Configured Access Control Security Levels"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-180]
cwe_ids: [CWE-732, CWE-1190, CWE-1191, CWE-1193, CWE-1220, CWE-1268, CWE-1280, CWE-1297, CWE-1311, CWE-1315, CWE-1318, CWE-1320, CWE-1321]
mitre_ids: [T1574.010]
related: [weakness/CWE-732, weakness/CWE-1190, weakness/CWE-1191, weakness/CWE-1193, weakness/CWE-1220, weakness/CWE-1268, weakness/CWE-1280, weakness/CWE-1297, weakness/CWE-1311, weakness/CWE-1315, weakness/CWE-1318, weakness/CWE-1320, weakness/CWE-1321, technique/T1574.010]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-180
updated_at: 2026-08-31
summary: "An attacker exploits a weakness in the configuration of access controls and is able to bypass the intended protection that these measures guard against and thereby obtain unauthorized access to the system or network. Sensitive functionality should always be protected with access …"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/180.html
---

# CAPEC-180: Exploiting Incorrectly Configured Access Control Security Levels

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker exploits a weakness in the configuration of access controls and is able to bypass the intended protection that these measures guard against and thereby obtain unauthorized access to the system or network. Sensitive functionality should always be protected with access controls. However configuring all but the most trivial access control systems can be very complicated and there are many opportunities for mistakes. If an attacker can learn of incorrectly configured access security settings, they may be able to exploit this in an attack.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-732](/wiki/p/weakness/CWE-732), [CWE-1190](/wiki/p/weakness/CWE-1190), [CWE-1191](/wiki/p/weakness/CWE-1191), [CWE-1193](/wiki/p/weakness/CWE-1193), [CWE-1220](/wiki/p/weakness/CWE-1220), [CWE-1268](/wiki/p/weakness/CWE-1268), [CWE-1280](/wiki/p/weakness/CWE-1280), [CWE-1297](/wiki/p/weakness/CWE-1297), [CWE-1311](/wiki/p/weakness/CWE-1311), [CWE-1315](/wiki/p/weakness/CWE-1315), [CWE-1318](/wiki/p/weakness/CWE-1318), [CWE-1320](/wiki/p/weakness/CWE-1320), [CWE-1321](/wiki/p/weakness/CWE-1321)

**ATT&CK techniques:** [T1574.010](/wiki/p/technique/T1574.010)

## Prerequisites

- The target must apply access controls, but incorrectly configure them. However, not all incorrect configurations can be exploited by an attacker. If the incorrect configuration applies too little security to some functionality, then the attacker may be able to exploit it if the access control would be the only thing preventing an attacker's access and it no longer does so. If the incorrect configuration applies too much security, it must prevent legitimate activity and the attacker must be able to force others to require this activity..

## Skills required

- Low: In order to discover unrestricted resources, the attacker does not need special tools or skills. They only have to observe the resources or access mechanisms invoked as each action is performed and then try and access those access mechanisms directly.

## Consequences

- Integrity: Modify Data
- Confidentiality: Read Data
- Authorization: Execute Unauthorized Commands
- Authorization: Gain Privileges
- Access Control, Authorization: Bypass Protection Mechanism
- Availability: Unreliable Execution

## Mitigations

- Design: Configure the access control correctly.

## Source

- [MITRE CAPEC CAPEC-180](https://capec.mitre.org/data/definitions/180.html)
