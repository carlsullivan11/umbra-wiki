---
slug: attack-pattern/CAPEC-17
title: "CAPEC-17 — Using Malicious Files"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-17]
cwe_ids: [CWE-59, CWE-270, CWE-272, CWE-282, CWE-285, CWE-693, CWE-732]
mitre_ids: [T1574.005, T1574.010]
related: [weakness/CWE-59, weakness/CWE-270, weakness/CWE-272, weakness/CWE-282, weakness/CWE-285, weakness/CWE-693, weakness/CWE-732, technique/T1574.005, technique/T1574.010]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-17
updated_at: 2026-08-31
summary: "An attack of this type exploits a system's configuration that allows an adversary to either directly access an executable file, for example through shell access; or in a possible worst case allows an adversary to upload a file and then execute it. Web servers, ftp servers, and me…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/17.html
---

# CAPEC-17: Using Malicious Files

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Very High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attack of this type exploits a system's configuration that allows an adversary to either directly access an executable file, for example through shell access; or in a possible worst case allows an adversary to upload a file and then execute it. Web servers, ftp servers, and message oriented middleware systems which have many integration points are particularly vulnerable, because both the programmers and the administrators must be in synch regarding the interfaces and the correct privileges for each interface.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-59](/wiki/p/weakness/CWE-59), [CWE-270](/wiki/p/weakness/CWE-270), [CWE-272](/wiki/p/weakness/CWE-272), [CWE-282](/wiki/p/weakness/CWE-282), [CWE-285](/wiki/p/weakness/CWE-285), [CWE-693](/wiki/p/weakness/CWE-693), [CWE-732](/wiki/p/weakness/CWE-732)

**ATT&CK techniques:** [T1574.005](/wiki/p/technique/T1574.005), [T1574.010](/wiki/p/technique/T1574.010)

## Prerequisites

- System's configuration must allow an attacker to directly access executable files or upload files to execute. This means that any access control system that is supposed to mediate communications between the subject and the object is set incorrectly or assumes a benign environment.

## Skills required

- Low: To identify and execute against an over-privileged system interface

## Consequences

- Confidentiality, Integrity, Availability: Execute Unauthorized Commands
- Integrity: Modify Data
- Confidentiality: Read Data
- Confidentiality, Access Control, Authorization: Gain Privileges

## Mitigations

- Design: Enforce principle of least privilege
- Design: Run server interfaces with a non-root account and/or utilize chroot jails or other configuration techniques to constrain privileges even if attacker gains some limited access to commands.
- Implementation: Perform testing such as pen-testing and vulnerability scanning to identify directories, programs, and interfaces that grant direct access to executables.

## Source

- [MITRE CAPEC CAPEC-17](https://capec.mitre.org/data/definitions/17.html)
