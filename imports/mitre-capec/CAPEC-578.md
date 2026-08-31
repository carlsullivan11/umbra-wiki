---
slug: attack-pattern/CAPEC-578
title: "CAPEC-578 — Disable Security Software"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-578]
cwe_ids: [CWE-284]
mitre_ids: [T1556.006, T1562.001, T1562.002, T1562.004, T1562.007, T1562.008, T1562.009]
related: [weakness/CWE-284, technique/T1556.006]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-578
updated_at: 2026-08-31
summary: "An adversary exploits a weakness in access control to disable security tools so that detection does not occur. This can take the form of killing processes, deleting registry keys so that tools do not start at run time, deleting log files, or other methods."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/578.html
---

# CAPEC-578: Disable Security Software

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Usable |
| Typical severity | Medium |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary exploits a weakness in access control to disable security tools so that detection does not occur. This can take the form of killing processes, deleting registry keys so that tools do not start at run time, deleting log files, or other methods.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-284](/wiki/p/weakness/CWE-284)

**ATT&CK techniques:** [T1556.006](/wiki/p/technique/T1556.006), [T1562.001](/wiki/p/technique/T1562.001), [T1562.002](/wiki/p/technique/T1562.002), [T1562.004](/wiki/p/technique/T1562.004), [T1562.007](/wiki/p/technique/T1562.007), [T1562.008](/wiki/p/technique/T1562.008), [T1562.009](/wiki/p/technique/T1562.009)

## Prerequisites

- The adversary must have the capability to interact with the configuration of the targeted system.

## Consequences

- Availability: Hide Activities

## Mitigations

- Ensure proper permissions are in place to prevent adversaries from altering the execution status of security tools.

## Mappings that no longer resolve

CAPEC 3.9 (2023-01-24) maps this pattern to `T1562.001`, `T1562.002`, `T1562.004`, `T1562.007`, `T1562.008`, `T1562.009`, which the current ATT&CK corpus does not carry — MITRE has revoked or relocated them since CAPEC was last published. The mapping is recorded here rather than dropped, because a stale cross-reference is a fact about the taxonomies, not a gap in this page.

## Source

- [MITRE CAPEC CAPEC-578](https://capec.mitre.org/data/definitions/578.html)
