---
slug: attack-pattern/CAPEC-177
title: "CAPEC-177 — Create files with the same name as files protected with a higher classification"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-177]
cwe_ids: [CWE-706]
mitre_ids: [T1036]
related: [weakness/CWE-706, technique/T1036]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-177
updated_at: 2026-08-31
summary: "An attacker exploits file location algorithms in an operating system or application by creating a file with the same name as a protected or privileged file. The attacker could manipulate the system if the attacker-created file is trusted by the operating system or an application …"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/177.html
---

# CAPEC-177: Create files with the same name as files protected with a higher classification

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Very High |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attacker exploits file location algorithms in an operating system or application by creating a file with the same name as a protected or privileged file. The attacker could manipulate the system if the attacker-created file is trusted by the operating system or an application component that attempts to load the original file. Applications often load or include external files, such as libraries or configuration files. These files should be protected against malicious manipulation. However, if the application only uses the name of the file when locating it, an attacker may be able to create a file with the same name and place it in a directory that the application will search before the directory with the legitimate file is searched. Because the attackers' file is discovered first, it would be used by the target application. This attack can be extremely destructive if the referenced file is executable and/or is granted special privileges based solely on having a particular name.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-706](/wiki/p/weakness/CWE-706)

**ATT&CK techniques:** [T1036](/wiki/p/technique/T1036)

## Prerequisites

- The target application must include external files. Most non-trivial applications meet this criterion.
- The target application does not verify that a located file is the one it was looking for through means other than the name. Many applications fail to perform checks of this type.
- The directories the target application searches to find the included file include directories writable by the attacker which are searched before the protected directory containing the actual files. It is much less common for applications to meet this criterion, but if an attacker can manipulate the application's search path (possibly by controlling environmental variables) then they can force this criterion to be met.

## Source

- [MITRE CAPEC CAPEC-177](https://capec.mitre.org/data/definitions/177.html)
