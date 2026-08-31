---
slug: attack-pattern/CAPEC-27
title: "CAPEC-27 — Leveraging Race Conditions via Symbolic Links"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-27]
cwe_ids: [CWE-61, CWE-367, CWE-662, CWE-667, CWE-689]
related: [weakness/CWE-61, weakness/CWE-367, weakness/CWE-662, weakness/CWE-667, weakness/CWE-689]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-27
updated_at: 2026-08-31
summary: "This attack leverages the use of symbolic links (Symlinks) in order to write to sensitive files. An attacker can create a Symlink link to a target file not otherwise accessible to them. When the privileged program tries to create a temporary file with the same name as the Symlink…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/27.html
---

# CAPEC-27: Leveraging Race Conditions via Symbolic Links

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

This attack leverages the use of symbolic links (Symlinks) in order to write to sensitive files. An attacker can create a Symlink link to a target file not otherwise accessible to them. When the privileged program tries to create a temporary file with the same name as the Symlink link, it will actually write to the target file pointed to by the attackers' Symlink link. If the attacker can insert malicious content in the temporary file they will be writing to the sensitive file by using the Symlink. The race occurs because the system checks if the temporary file exists, then creates the file. The attacker would typically create the Symlink during the interval between the check and the creation of the temporary file.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-61](/wiki/p/weakness/CWE-61), [CWE-367](/wiki/p/weakness/CWE-367), [CWE-662](/wiki/p/weakness/CWE-662), [CWE-667](/wiki/p/weakness/CWE-667), [CWE-689](/wiki/p/weakness/CWE-689)

## Prerequisites

- The attacker is able to create Symlink links on the target host.
- Tainted data from the attacker is used and copied to temporary files.
- The target host does insecure temporary file creation.

## Skills required

- Medium: This attack is sophisticated because the attacker has to overcome a few challenges such as creating symlinks on the target host during a precise timing, inserting malicious data in the temporary file and have knowledge about the temporary files created (file name and function which creates them).

## Consequences

- Integrity: Modify Data
- Confidentiality, Access Control, Authorization: Gain Privileges
- Availability: Resource Consumption

## Mitigations

- Use safe libraries when creating temporary files. For instance the standard library function mkstemp can be used to safely create temporary files. For shell scripts, the system utility mktemp does the same thing.
- Access to the directories should be restricted as to prevent attackers from manipulating the files. Denying access to a file can prevent an attacker from replacing that file with a link to a sensitive file.
- Follow the principle of least privilege when assigning access rights to files.
- Ensure good compartmentalization in the system to provide protected areas that can be trusted.

## Source

- [MITRE CAPEC CAPEC-27](https://capec.mitre.org/data/definitions/27.html)
