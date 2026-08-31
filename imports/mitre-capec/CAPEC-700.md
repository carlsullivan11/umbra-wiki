---
slug: attack-pattern/CAPEC-700
title: "CAPEC-700 — Network Boundary Bridging"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-700]
mitre_ids: [T1599]
related: [technique/T1599]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-700
updated_at: 2026-08-31
summary: "An adversary which has gained elevated access to network boundary devices may use these devices to create a channel to bridge trusted and untrusted networks. Boundary devices do not necessarily have to be on the network’s edge, but rather must serve to segment portions of the tar…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/700.html
---

# CAPEC-700: Network Boundary Bridging

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary which has gained elevated access to network boundary devices may use these devices to create a channel to bridge trusted and untrusted networks. Boundary devices do not necessarily have to be on the network’s edge, but rather must serve to segment portions of the target network the adversary wishes to cross into.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**ATT&CK techniques:** [T1599](/wiki/p/technique/T1599)

## Prerequisites

- The adversary must have control of a network boundary device.

## Skills required

- Medium: The adversary must understand how to manage the target network device to create or edit policies which will bridge networks.

## Consequences

- Confidentiality, Access Control: Read Data, Bypass Protection Mechanism
- Integrity, Authorization: Alter Execution Logic, Hide Activities

## Mitigations

- Design: Ensure network devices are storing credentials in encrypted stores
- Design: Follow the principle of least privilege and restrict administrative duties to as few accounts as possible. Ensure these privileged accounts are secured with strong credentials which do not overlap with other network devices.
- Configuration: When possible, configure network boundary devices to use MFA.
- Configuration: Change the default configuration for network devices to harden their security profiles. Default configurations are often enabled with insecure features to allow ease of installation and management. However, these configurations can be easily discovered and exploited by adversaries.
- Implementation: Perform integrity checks on audit logs for network device management and review them to identify abnormalities in configurations.
- Implementation: Prevent network boundary devices from being physically accessed by unauthorized personnel to prevent tampering.

## Source

- [MITRE CAPEC CAPEC-700](https://capec.mitre.org/data/definitions/700.html)
