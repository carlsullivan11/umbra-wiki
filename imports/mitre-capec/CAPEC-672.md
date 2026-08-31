---
slug: attack-pattern/CAPEC-672
title: "CAPEC-672 — Malicious Code Implanted During Chip Programming"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-672]
mitre_ids: [T1195.003]
related: [technique/T1195.003]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-672
updated_at: 2026-08-31
summary: "During the programming step of chip manufacture, an adversary with access and necessary technical skills maliciously alters a chip’s intended program logic to produce an effect intended by the adversary when the fully manufactured chip is deployed and in operational use. Intended…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/672.html
---

# CAPEC-672: Malicious Code Implanted During Chip Programming

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

During the programming step of chip manufacture, an adversary with access and necessary technical skills maliciously alters a chip’s intended program logic to produce an effect intended by the adversary when the fully manufactured chip is deployed and in operational use. Intended effects can include the ability of the adversary to remotely control a host system to carry out malicious acts.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**ATT&CK techniques:** [T1195.003](/wiki/p/technique/T1195.003)

## Prerequisites

- An adversary would need to have access to a foundry’s or chip maker’s development/production environment where programs for specific chips are developed, managed and uploaded into targeted chips prior to distribution or sale.

## Skills required

- Medium: An adversary needs to be skilled in microprogramming, manipulation of configuration management systems, and in the operation of tools used for the uploading of programs into chips during manufacture. Uploading can be for individual chips or performed on a large scale basis.

## Consequences

- Integrity: Alter Execution Logic

## Mitigations

- Utilize DMEA’s (Defense Microelectronics Activity) Trusted Foundry Program members for acquisition of microelectronic components.
- Ensure that each supplier performing hardware development implements comprehensive, security-focused configuration management of microcode and microcode generating tools and software.
- Require that provenance of COTS microelectronic components be known whenever procured.
- Conduct detailed vendor assessment before acquiring COTS hardware.

## Source

- [MITRE CAPEC CAPEC-672](https://capec.mitre.org/data/definitions/672.html)
