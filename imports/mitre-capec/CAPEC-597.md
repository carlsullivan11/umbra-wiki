---
slug: attack-pattern/CAPEC-597
title: "CAPEC-597 — Absolute Path Traversal"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-597]
cwe_ids: [CWE-36]
related: [weakness/CWE-36]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-597
updated_at: 2026-08-31
summary: "An adversary with access to file system resources, either directly or via application logic, will use various file absolute paths and navigation mechanisms such as '..' to extend their range of access to inappropriate areas of the file system. The goal of the adversary is to acce…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/597.html
---

# CAPEC-597: Absolute Path Traversal

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | — |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary with access to file system resources, either directly or via application logic, will use various file absolute paths and navigation mechanisms such as ".." to extend their range of access to inappropriate areas of the file system. The goal of the adversary is to access directories and files that are intended to be restricted from their access.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-36](/wiki/p/weakness/CWE-36)

## Prerequisites

- The target must leverage and access an underlying file system.

## Skills required

- Low: Simple command line attacks.
- Medium: Programming attacks.

## Consequences

- Integrity, Confidentiality, Availability: Execute Unauthorized Commands
- Integrity: Modify Data
- Confidentiality: Read Data
- Availability: Unreliable Execution

## Mitigations

- Design: Configure the access control correctly.
- Design: Enforce principle of least privilege.
- Design: Execute programs with constrained privileges, so parent process does not open up further vulnerabilities. Ensure that all directories, temporary directories and files, and memory are executing with limited privileges to protect against remote execution.
- Design: Input validation. Assume that user inputs are malicious. Utilize strict type, character, and encoding enforcement.
- Design: Proxy communication to host, so that communications are terminated at the proxy, sanitizing the requests before forwarding to server host.
- Design: Run server interfaces with a non-root account and/or utilize chroot jails or other configuration techniques to constrain privileges even if attacker gains some limited access to commands.
- Implementation: Host integrity monitoring for critical files, directories, and processes. The goal of host integrity monitoring is to be aware when a security issue has occurred so that incident response and other forensic activities can begin.
- Implementation: Perform input validation for all remote content, including remote and user-generated content.

## Source

- [MITRE CAPEC CAPEC-597](https://capec.mitre.org/data/definitions/597.html)
