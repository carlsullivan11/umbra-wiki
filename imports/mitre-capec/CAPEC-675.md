---
slug: attack-pattern/CAPEC-675
title: "CAPEC-675 — Retrieve Data from Decommissioned Devices"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-675]
cwe_ids: [CWE-1266]
mitre_ids: [T1052]
related: [weakness/CWE-1266, technique/T1052]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-675
updated_at: 2026-08-31
summary: "An adversary obtains decommissioned, recycled, or discarded systems and devices that can include an organization’s intellectual property, employee data, and other types of controlled information. Systems and devices that have reached the end of their lifecycles may be subject to …"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/675.html
---

# CAPEC-675: Retrieve Data from Decommissioned Devices

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Medium |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary obtains decommissioned, recycled, or discarded systems and devices that can include an organization’s intellectual property, employee data, and other types of controlled information. Systems and devices that have reached the end of their lifecycles may be subject to recycle or disposal where they can be exposed to adversarial attempts to retrieve information from internal memory chips and storage devices that are part of the system.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-1266](/wiki/p/weakness/CWE-1266)

**ATT&CK techniques:** [T1052](/wiki/p/technique/T1052)

## Prerequisites

- An adversary needs to have access to electronic data processing equipment being recycled or disposed of (e.g., laptops, servers) at a collection location and the ability to take control of it for the purpose of exploiting its content.

## Skills required

- High: An adversary may need the ability to mount printed circuit boards and target individual chips for exploitation.
- Medium: An adversary needs the technical skills required to extract solid state drives, hard disk drives, and other storage media to host on a compatible system or harness to gain access to digital content.

## Consequences

- Accountability: Bypass Protection Mechanism

## Mitigations

- Backup device data before erasure to retain intellectual property and inside knowledge.
- Overwrite data on device rather than deleting. Deleted data can still be recovered, even if the device trash can is emptied. Rewriting data removes any trace of the old data. Performing multiple overwrites followed by a zeroing of the device (overwriting with all zeros) is good practice.
- Use a secure erase software.
- Physically destroy the device if it is not intended to be reused. Using a specialized service to disintegrate, burn, melt or pulverize the device can be effective, but if those services are inaccessible, drilling nails or holes, or smashing the device with a hammer can be effective. Do not burn, microwave, or pour acid on a hard drive.
- Physically destroy memory and SIM cards for mobile devices not intended to be reused.
- Ensure that the user account has been terminated or switched to a new device before destroying.

## Source

- [MITRE CAPEC CAPEC-675](https://capec.mitre.org/data/definitions/675.html)
