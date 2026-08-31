---
slug: attack-pattern/CAPEC-126
title: "CAPEC-126 — Path Traversal"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-126]
cwe_ids: [CWE-22]
related: [weakness/CWE-22]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-126
updated_at: 2026-08-31
summary: "An adversary uses path manipulation methods to exploit insufficient input validation of a target to obtain access to data that should be not be retrievable by ordinary well-formed requests. A typical variety of this attack involves specifying a path to a desired file together wit…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/126.html
---

# CAPEC-126: Path Traversal

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Very High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary uses path manipulation methods to exploit insufficient input validation of a target to obtain access to data that should be not be retrievable by ordinary well-formed requests. A typical variety of this attack involves specifying a path to a desired file together with dot-dot-slash characters, resulting in the file access API or function traversing out of the intended directory structure and into the root file system. By replacing or modifying the expected path information the access function or API retrieves the file desired by the attacker. These attacks either involve the attacker providing a complete path to a targeted file or using control characters (e.g. path separators (/ or \) and/or dots (.)) to reach desired directories or files.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-22](/wiki/p/weakness/CWE-22)

## Prerequisites

- The attacker must be able to control the path that is requested of the target.
- The target must fail to adequately sanitize incoming paths

## Skills required

- Low: Simple command line attacks or to inject the malicious payload in a web page.
- Medium: Customizing attacks to bypass non trivial filters in the application.

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

- [MITRE CAPEC CAPEC-126](https://capec.mitre.org/data/definitions/126.html)
