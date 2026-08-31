---
slug: attack-pattern/CAPEC-178
title: "CAPEC-178 — Cross-Site Flashing"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-178]
cwe_ids: [CWE-601]
related: [weakness/CWE-601]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-178
updated_at: 2026-08-31
summary: "An attacker is able to trick the victim into executing a Flash document that passes commands or calls to a Flash player browser plugin, allowing the attacker to exploit native Flash functionality in the client browser. This attack pattern occurs where an attacker can provide a cr…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/178.html
---

# CAPEC-178: Cross-Site Flashing

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker is able to trick the victim into executing a Flash document that passes commands or calls to a Flash player browser plugin, allowing the attacker to exploit native Flash functionality in the client browser. This attack pattern occurs where an attacker can provide a crafted link to a Flash document (SWF file) which, when followed, will cause additional malicious instructions to be executed. The attacker does not need to serve or control the Flash document. The attack takes advantage of the fact that Flash files can reference external URLs. If variables that serve as URLs that the Flash application references can be controlled through parameters, then by creating a link that includes values for those parameters, an attacker can cause arbitrary content to be referenced and possibly executed by the targeted Flash application.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-601](/wiki/p/weakness/CWE-601)

## Prerequisites

- The targeted Flash application must reference external URLs and the locations thus referenced must be controllable through parameters. The Flash application must fail to sanitize such parameters against malicious manipulation. The victim must follow a crafted link created by the attacker.

## Skills required

- Medium: knowledge of Flash internals, parameters and remote referencing.

## Consequences

- Integrity: Modify Data
- Confidentiality: Read Data
- Authorization: Execute Unauthorized Commands
- Accountability, Authentication, Authorization, Non-Repudiation: Gain Privileges
- Access Control, Authorization: Bypass Protection Mechanism

## Mitigations

- Implementation: Only allow known URL to be included as remote flash movies in a flash application
- Configuration: Properly configure the crossdomain.xml file to only include the known domains that should host remote flash movies.

## Source

- [MITRE CAPEC CAPEC-178](https://capec.mitre.org/data/definitions/178.html)
