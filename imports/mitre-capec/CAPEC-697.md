---
slug: attack-pattern/CAPEC-697
title: "CAPEC-697 — DHCP Spoofing"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-697]
cwe_ids: [CWE-923]
mitre_ids: [T1557.003]
related: [weakness/CWE-923, technique/T1557.003]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-697
updated_at: 2026-08-31
summary: "An adversary masquerades as a legitimate Dynamic Host Configuration Protocol (DHCP) server by spoofing DHCP traffic, with the goal of redirecting network traffic or denying service to DHCP."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/697.html
---

# CAPEC-697: DHCP Spoofing

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | High |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary masquerades as a legitimate Dynamic Host Configuration Protocol (DHCP) server by spoofing DHCP traffic, with the goal of redirecting network traffic or denying service to DHCP.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-923](/wiki/p/weakness/CWE-923)

**ATT&CK techniques:** [T1557.003](/wiki/p/technique/T1557.003)

## Prerequisites

- The adversary must have access to a machine within the target LAN which can send DHCP offers to the target.

## Skills required

- Medium: The adversary must identify potential targets for DHCP Spoofing and craft network configurations to obtain the desired results.

## Consequences

- Confidentiality, Access Control: Read Data
- Integrity, Access Control: Modify Data, Execute Unauthorized Commands
- Availability: Resource Consumption

## Mitigations

- Design: MAC-Forced Forwarding
- Implementation: Port Security and DHCP snooping
- Implementation: Network-based Intrusion Detection Systems

## Source

- [MITRE CAPEC CAPEC-697](https://capec.mitre.org/data/definitions/697.html)
