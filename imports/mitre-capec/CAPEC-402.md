---
slug: attack-pattern/CAPEC-402
title: "CAPEC-402 — Bypassing ATA Password Security"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-402]
cwe_ids: [CWE-285]
related: [weakness/CWE-285]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-402
updated_at: 2026-08-31
summary: "An adversary exploits a weakness in ATA security on a drive to gain access to the information the drive contains without supplying the proper credentials. ATA Security is often employed to protect hard disk information from unauthorized access. The mechanism requires the user to …"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/402.html
---

# CAPEC-402: Bypassing ATA Password Security

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | — |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary exploits a weakness in ATA security on a drive to gain access to the information the drive contains without supplying the proper credentials. ATA Security is often employed to protect hard disk information from unauthorized access. The mechanism requires the user to type in a password before the BIOS is allowed access to drive contents. Some implementations of ATA security will accept the ATA command to update the password without the user having authenticated with the BIOS. This occurs because the security mechanism assumes the user has first authenticated via the BIOS prior to sending commands to the drive. Various methods exist for exploiting this flaw, the most common being installing the ATA protected drive into a system lacking ATA security features (a.k.a. hot swapping). Once the drive is installed into the new system the BIOS can be used to reset the drive password.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-285](/wiki/p/weakness/CWE-285)

## Prerequisites

- Access to the system containing the ATA Drive so that the drive can be physically removed from the system.

## Mitigations

- Avoid using ATA password security when possible.
- Use full disk encryption to protect the entire contents of the drive or sensitive partitions on the drive.
- Leverage third-party utilities that interface with self-encrypting drives (SEDs) to provide authentication, while relying on the SED itself for data encryption.

## Source

- [MITRE CAPEC CAPEC-402](https://capec.mitre.org/data/definitions/402.html)
