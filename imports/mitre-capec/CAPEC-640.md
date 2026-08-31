---
slug: attack-pattern/CAPEC-640
title: "CAPEC-640 — Inclusion of Code in Existing Process"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-640]
cwe_ids: [CWE-114, CWE-829]
mitre_ids: [T1505.005, T1574.006, T1574.013, T1620]
related: [weakness/CWE-114, weakness/CWE-829, technique/T1505.005, technique/T1574.006, technique/T1574.013, technique/T1620]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-640
updated_at: 2026-08-31
summary: "The adversary takes advantage of a bug in an application failing to verify the integrity of the running process to execute arbitrary code in the address space of a separate live process. The adversary could use running code in the context of another process to try to access proce…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/640.html
---

# CAPEC-640: Inclusion of Code in Existing Process

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | High |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

The adversary takes advantage of a bug in an application failing to verify the integrity of the running process to execute arbitrary code in the address space of a separate live process. The adversary could use running code in the context of another process to try to access process's memory, system/network resources, etc. The goal of this attack is to evade detection defenses and escalate privileges by masking the malicious code under an existing legitimate process. Examples of approaches include but not limited to: dynamic-link library (DLL) injection, portable executable injection, thread execution hijacking, ptrace system calls, VDSO hijacking, function hooking, reflective code loading, and more.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-114](/wiki/p/weakness/CWE-114), [CWE-829](/wiki/p/weakness/CWE-829)

**ATT&CK techniques:** [T1505.005](/wiki/p/technique/T1505.005), [T1574.006](/wiki/p/technique/T1574.006), [T1574.013](/wiki/p/technique/T1574.013), [T1620](/wiki/p/technique/T1620)

## Prerequisites

- The targeted application fails to verify the integrity of the running process that allows an adversary to execute arbitrary code.

## Skills required

- High: Knowledge of how to load malicious code into the memory space of a running process, as well as the ability to have the running process execute this code. For example, with DLL injection, the adversary must know how to load a DLL into the memory space of another running process, and cause this process to execute the code inside of the DLL.

## Consequences

- Integrity, Confidentiality: Execute Unauthorized Commands, Read Data

## Mitigations

- Prevent unknown or malicious software from loading through using an allowlist policy.
- Properly restrict the location of the software being used.
- Leverage security kernel modules providing advanced access control and process restrictions like SELinux.
- Monitor API calls like CreateRemoteThread, SuspendThread/SetThreadContext/ResumeThread, QueueUserAPC, and similar for Windows.
- Monitor API calls like ptrace system call, use of LD_PRELOAD environment variable, dlfcn dynamic linking API calls, and similar for Linux.
- Monitor API calls like SetWindowsHookEx and SetWinEventHook which install hook procedures for Windows.
- Monitor processes and command-line arguments for unknown behavior related to code injection.

## Source

- [MITRE CAPEC CAPEC-640](https://capec.mitre.org/data/definitions/640.html)
