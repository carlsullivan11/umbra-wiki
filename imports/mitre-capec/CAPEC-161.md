---
slug: attack-pattern/CAPEC-161
title: "CAPEC-161 — Infrastructure Manipulation"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-161]
cwe_ids: [CWE-923]
related: [weakness/CWE-923]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-161
updated_at: 2026-08-31
summary: "An attacker exploits characteristics of the infrastructure of a network entity in order to perpetrate attacks or information gathering on network objects or effect a change in the ordinary information flow between network objects. Most often, this involves manipulation of the rou…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/161.html
---

# CAPEC-161: Infrastructure Manipulation

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker exploits characteristics of the infrastructure of a network entity in order to perpetrate attacks or information gathering on network objects or effect a change in the ordinary information flow between network objects. Most often, this involves manipulation of the routing of network messages so, instead of arriving at their proper destination, they are directed towards an entity of the attackers' choosing, usually a server controlled by the attacker. The victim is often unaware that their messages are not being processed correctly. For example, a targeted client may believe they are connecting to their own bank but, in fact, be connecting to a Pharming site controlled by the attacker which then collects the user's login information in order to hijack the actual bank account.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-923](/wiki/p/weakness/CWE-923)

## Prerequisites

- The targeted client must access the site via infrastructure that the attacker has co-opted and must fail to adequately verify that the communication channel is operating correctly (e.g. by verifying that they are, in fact, connected to the site they intended.)

## Source

- [MITRE CAPEC CAPEC-161](https://capec.mitre.org/data/definitions/161.html)
