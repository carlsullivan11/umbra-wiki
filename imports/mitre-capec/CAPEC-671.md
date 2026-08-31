---
slug: attack-pattern/CAPEC-671
title: "CAPEC-671 — Requirements for ASIC Functionality Maliciously Altered"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-671]
mitre_ids: [T1195.003]
related: [technique/T1195.003]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-671
updated_at: 2026-08-31
summary: "An adversary with access to functional requirements for an application specific integrated circuit (ASIC), a chip designed/customized for a singular particular use, maliciously alters requirements derived from originating capability needs. In the chip manufacturing process, requi…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/671.html
---

# CAPEC-671: Requirements for ASIC Functionality Maliciously Altered

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary with access to functional requirements for an application specific integrated circuit (ASIC), a chip designed/customized for a singular particular use, maliciously alters requirements derived from originating capability needs. In the chip manufacturing process, requirements drive the chip design which, when the chip is fully manufactured, could result in an ASIC which may not meet the user’s needs, contain malicious functionality, or exhibit other anomalous behaviors thereby affecting the intended use of the ASIC.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**ATT&CK techniques:** [T1195.003](/wiki/p/technique/T1195.003)

## Prerequisites

- An adversary would need to have access to a foundry’s or chip maker’s requirements management system that stores customer requirements for ASICs, requirements upon which the design of the ASIC is based.

## Skills required

- High: An adversary would need experience in designing chips based on functional requirements in order to manipulate requirements in such a way that deviations would not be detected in subsequent stages of ASIC manufacture and where intended malicious functionality would be available to the adversary once integrated into a system and fielded.

## Consequences

- Integrity: Alter Execution Logic

## Mitigations

- Utilize DMEA’s (Defense Microelectronics Activity) Trusted Foundry Program members for acquisition of microelectronic components.
- Ensure that each supplier performing hardware development implements comprehensive, security-focused configuration management including for hardware requirements and design.
- Require that provenance of COTS microelectronic components be known whenever procured.
- Conduct detailed vendor assessment before acquiring COTS hardware.

## Source

- [MITRE CAPEC CAPEC-671](https://capec.mitre.org/data/definitions/671.html)
