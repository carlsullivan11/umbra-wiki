---
slug: attack-pattern/CAPEC-641
title: "CAPEC-641 — DLL Side-Loading"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-641]
cwe_ids: [CWE-706]
mitre_ids: [T1574.002]
related: [weakness/CWE-706]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-641
updated_at: 2026-08-31
summary: "An adversary places a malicious version of a Dynamic-Link Library (DLL) in the Windows Side-by-Side (WinSxS) directory to trick the operating system into loading this malicious DLL instead of a legitimate DLL. Programs specify the location of the DLLs to load via the use of WinSx…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/641.html
---

# CAPEC-641: DLL Side-Loading

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | High |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary places a malicious version of a Dynamic-Link Library (DLL) in the Windows Side-by-Side (WinSxS) directory to trick the operating system into loading this malicious DLL instead of a legitimate DLL. Programs specify the location of the DLLs to load via the use of WinSxS manifests or DLL redirection and if they aren't used then Windows searches in a predefined set of directories to locate the file. If the applications improperly specify a required DLL or WinSxS manifests aren't explicit about the characteristics of the DLL to be loaded, they can be vulnerable to side-loading.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-706](/wiki/p/weakness/CWE-706)

**ATT&CK techniques:** [T1574.002](/wiki/p/technique/T1574.002)

## Prerequisites

- The target must fail to verify the integrity of the DLL before using them.

## Skills required

- High: Trick the operating system in loading a malicious DLL instead of a legitimate DLL.

## Consequences

- Integrity: Execute Unauthorized Commands, Bypass Protection Mechanism

## Mitigations

- Prevent unknown DLLs from loading through using an allowlist policy.
- Patch installed applications as soon as new updates become available.
- Properly restrict the location of the software being used.
- Use of sxstrace.exe on Windows as well as manual inspection of the manifests.
- Require code signing and avoid using relative paths for resources.

## Mappings that no longer resolve

CAPEC 3.9 (2023-01-24) maps this pattern to `T1574.002`, which the current ATT&CK corpus does not carry — MITRE has revoked or relocated them since CAPEC was last published. The mapping is recorded here rather than dropped, because a stale cross-reference is a fact about the taxonomies, not a gap in this page.

## Source

- [MITRE CAPEC CAPEC-641](https://capec.mitre.org/data/definitions/641.html)
