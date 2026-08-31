---
slug: attack-pattern/CAPEC-35
title: "CAPEC-35 — Leverage Executable Code in Non-Executable Files"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-35]
cwe_ids: [CWE-59, CWE-94, CWE-95, CWE-96, CWE-97, CWE-270, CWE-272, CWE-282]
mitre_ids: [T1027.006, T1027.009, T1564.009]
related: [weakness/CWE-59, weakness/CWE-94, weakness/CWE-95, weakness/CWE-96, weakness/CWE-97, weakness/CWE-270, weakness/CWE-272, weakness/CWE-282, technique/T1027.006, technique/T1027.009, technique/T1564.009]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-35
updated_at: 2026-08-31
summary: "An attack of this type exploits a system's trust in configuration and resource files. When the executable loads the resource (such as an image file or configuration file) the attacker has modified the file to either execute malicious code directly or manipulate the target process…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/35.html
---

# CAPEC-35: Leverage Executable Code in Non-Executable Files

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Very High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attack of this type exploits a system's trust in configuration and resource files. When the executable loads the resource (such as an image file or configuration file) the attacker has modified the file to either execute malicious code directly or manipulate the target process (e.g. application server) to execute based on the malicious configuration parameters. Since systems are increasingly interrelated mashing up resources from local and remote sources the possibility of this attack occurring is high.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-59](/wiki/p/weakness/CWE-59), [CWE-94](/wiki/p/weakness/CWE-94), [CWE-95](/wiki/p/weakness/CWE-95), [CWE-96](/wiki/p/weakness/CWE-96), [CWE-97](/wiki/p/weakness/CWE-97), [CWE-270](/wiki/p/weakness/CWE-270), [CWE-272](/wiki/p/weakness/CWE-272), [CWE-282](/wiki/p/weakness/CWE-282)

**ATT&CK techniques:** [T1027.006](/wiki/p/technique/T1027.006), [T1027.009](/wiki/p/technique/T1027.009), [T1564.009](/wiki/p/technique/T1564.009)

## Prerequisites

- The attacker must have the ability to modify non-executable files consumed by the target software.

## Skills required

- Low: To identify and execute against an over-privileged system interface

## Consequences

- Confidentiality, Integrity, Availability: Execute Unauthorized Commands
- Integrity: Modify Data
- Confidentiality, Access Control, Authorization: Gain Privileges

## Mitigations

- Design: Enforce principle of least privilege
- Design: Run server interfaces with a non-root account and/or utilize chroot jails or other configuration techniques to constrain privileges even if attacker gains some limited access to commands.
- Implementation: Perform testing such as pen-testing and vulnerability scanning to identify directories, programs, and interfaces that grant direct access to executables.
- Implementation: Implement host integrity monitoring to detect any unwanted altering of configuration files.
- Implementation: Ensure that files that are not required to execute, such as configuration files, are not over-privileged, i.e. not allowed to execute.

## Source

- [MITRE CAPEC CAPEC-35](https://capec.mitre.org/data/definitions/35.html)
