---
slug: attack-pattern/CAPEC-665
title: "CAPEC-665 — Exploitation of Thunderbolt Protection Flaws"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-665]
cwe_ids: [CWE-288, CWE-345, CWE-353, CWE-862, CWE-1188]
mitre_ids: [T1211, T1542.002, T1556]
related: [weakness/CWE-288, weakness/CWE-345, weakness/CWE-353, weakness/CWE-862, weakness/CWE-1188, technique/T1211, technique/T1542.002, technique/T1556]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-665
updated_at: 2026-08-31
summary: "An adversary leverages a firmware weakness within the Thunderbolt protocol, on a computing device to manipulate Thunderbolt controller firmware in order to exploit vulnerabilities in the implementation of authorization and verification schemes within Thunderbolt protection mechan…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/665.html
---

# CAPEC-665: Exploitation of Thunderbolt Protection Flaws

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Very High |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary leverages a firmware weakness within the Thunderbolt protocol, on a computing device to manipulate Thunderbolt controller firmware in order to exploit vulnerabilities in the implementation of authorization and verification schemes within Thunderbolt protection mechanisms. Upon gaining physical access to a target device, the adversary conducts high-level firmware manipulation of the victim Thunderbolt controller SPI (Serial Peripheral Interface) flash, through the use of a SPI Programing device and an external Thunderbolt device, typically as the target device is booting up. If successful, this allows the adversary to modify memory, subvert authentication mechanisms, spoof identities and content, and extract data and memory from the target device. Currently 7 major vulnerabilities exist within Thunderbolt protocol with 9 attack vectors as noted in the Execution Flow.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-288](/wiki/p/weakness/CWE-288), [CWE-345](/wiki/p/weakness/CWE-345), [CWE-353](/wiki/p/weakness/CWE-353), [CWE-862](/wiki/p/weakness/CWE-862), [CWE-1188](/wiki/p/weakness/CWE-1188)

**ATT&CK techniques:** [T1211](/wiki/p/technique/T1211), [T1542.002](/wiki/p/technique/T1542.002), [T1556](/wiki/p/technique/T1556)

## Prerequisites

- The adversary needs at least a few minutes of physical access to a system with an open Thunderbolt port, version 3 or lower, and an external thunderbolt device controlled by the adversary with maliciously crafted software and firmware, via an SPI Programming device, to exploit weaknesses in security protections.

## Skills required

- High: Detailed knowledge on various system motherboards, PCI Express Domain, SPI, and Thunderbolt Protocol in order to interface with internal system components via external devices.
- High: Detailed knowledge on OS/Kernel memory address space, Direct Memory Access (DMA) mapping, Input-Output Memory Management Units (IOMMUs), and vendor memory protections for data leakage.
- High: Detailed knowledge on scripting and SPI programming in order to configure and modify Thunderbolt controller firmware and software configurations.

## Consequences

- Access Control: Bypass Protection Mechanism
- Confidentiality: Read Data
- Integrity: Modify Data
- Authorization: Execute Unauthorized Commands

## Mitigations

- Implementation: Kernel Direct Memory Access Protection
- Configuration: Enable UEFI option USB Passthrough mode - Thunderbolt 3 system port operates as USB 3.1 Type C interface
- Configuration: Enable UEFI option DisplayPort mode - Thunderbolt 3 system port operates as video-only DP interface
- Configuration: Enable UEFI option Mixed USB/DisplayPort mode - Thunderbolt 3 system port operates as USB 3.1 Type C interface with support for DP mode
- Configuration: Set Security Level to SL3 for Thunderbolt 2 system port
- Configuration: Disable PCIe tunneling to set Security Level to SL3
- Configuration: Disable Boot Camp upon MacOS systems

## Source

- [MITRE CAPEC CAPEC-665](https://capec.mitre.org/data/definitions/665.html)
