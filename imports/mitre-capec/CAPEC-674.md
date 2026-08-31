---
slug: attack-pattern/CAPEC-674
title: "CAPEC-674 — Design for FPGA Maliciously Altered"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-674]
mitre_ids: [T1195.003]
related: [technique/T1195.003]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-674
updated_at: 2026-08-31
summary: "An adversary alters the functionality of a field-programmable gate array (FPGA) by causing an FPGA configuration memory chip reload in order to introduce a malicious function that could result in the FPGA performing or enabling malicious functions on a host system. Prior to the m…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/674.html
---

# CAPEC-674: Design for FPGA Maliciously Altered

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | High |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary alters the functionality of a field-programmable gate array (FPGA) by causing an FPGA configuration memory chip reload in order to introduce a malicious function that could result in the FPGA performing or enabling malicious functions on a host system. Prior to the memory chip reload, the adversary alters the program for the FPGA by adding a function to impact system operation.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**ATT&CK techniques:** [T1195.003](/wiki/p/technique/T1195.003)

## Prerequisites

- An adversary would need to have access to FPGA programming/configuration-related systems in a chip maker’s development environment where FPGAs can be initially configured prior to delivery to a customer or have access to such systems in a customer facility where end-user FPGA configuration/reconfiguration can be performed.

## Skills required

- High: An adversary would need to be skilled in FPGA programming in order to create/manipulate configurations in such a way that when loaded into an FPGA, the end user would be able to observe through testing all user-defined required functions but would be unaware of any additional functions the adversary may have introduced.

## Consequences

- Integrity: Alter Execution Logic

## Mitigations

- Utilize DMEA’s (Defense Microelectronics Activity) Trusted Foundry Program members for acquisition of microelectronic components.
- Ensure that each supplier performing hardware development implements comprehensive, security-focused configuration management including for FPGA programming and program uploads to FPGA chips.
- Require that provenance of COTS microelectronic components be known whenever procured.
- Conduct detailed vendor assessment before acquiring COTS hardware.

## Source

- [MITRE CAPEC CAPEC-674](https://capec.mitre.org/data/definitions/674.html)
