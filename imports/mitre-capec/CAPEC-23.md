---
slug: attack-pattern/CAPEC-23
title: "CAPEC-23 — File Content Injection"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-23]
cwe_ids: [CWE-20]
related: [weakness/CWE-20]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-23
updated_at: 2026-08-31
summary: "An adversary poisons files with a malicious payload (targeting the file systems accessible by the target software), which may be passed through by standard channels such as via email, and standard web content like PDF and multimedia files. The adversary exploits known vulnerabili…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/23.html
---

# CAPEC-23: File Content Injection

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Very High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary poisons files with a malicious payload (targeting the file systems accessible by the target software), which may be passed through by standard channels such as via email, and standard web content like PDF and multimedia files. The adversary exploits known vulnerabilities or handling routines in the target processes, in order to exploit the host's trust in executing remote content, including binary files.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-20](/wiki/p/weakness/CWE-20)

## Prerequisites

- The target software must consume files.
- The adversary must have access to modify files that the target software will consume.

## Skills required

- Medium: How to poison a file with malicious payload that will exploit a vulnerability when the file is opened. The adversary must also know how to place the file onto a system where it will be opened by an unsuspecting party, or force the file to be opened.

## Consequences

- Confidentiality, Integrity, Availability: Execute Unauthorized Commands

## Mitigations

- Design: Enforce principle of least privilege
- Design: Validate all input for content including files. Ensure that if files and remote content must be accepted that once accepted, they are placed in a sandbox type location so that lower assurance clients cannot write up to higher assurance processes (like Web server processes for example)
- Design: Execute programs with constrained privileges, so parent process does not open up further vulnerabilities. Ensure that all directories, temporary directories and files, and memory are executing with limited privileges to protect against remote execution.
- Design: Proxy communication to host, so that communications are terminated at the proxy, sanitizing the requests before forwarding to server host.
- Implementation: Virus scanning on host
- Implementation: Host integrity monitoring for critical files, directories, and processes. The goal of host integrity monitoring is to be aware when a security issue has occurred so that incident response and other forensic activities can begin.

## Source

- [MITRE CAPEC CAPEC-23](https://capec.mitre.org/data/definitions/23.html)
