---
slug: attack-pattern/CAPEC-663
title: "CAPEC-663 — Exploitation of Transient Instruction Execution"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-663]
cwe_ids: [CWE-1037, CWE-1264, CWE-1303]
related: [weakness/CWE-1037, weakness/CWE-1264, weakness/CWE-1303]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-663
updated_at: 2026-08-31
summary: "An adversary exploits a hardware design flaw in a CPU implementation of transient instruction execution to expose sensitive data and bypass/subvert access control over restricted resources. Typically, the adversary conducts a covert channel attack to target non-discarded microarc…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/663.html
---

# CAPEC-663: Exploitation of Transient Instruction Execution

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Very High |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary exploits a hardware design flaw in a CPU implementation of transient instruction execution to expose sensitive data and bypass/subvert access control over restricted resources. Typically, the adversary conducts a covert channel attack to target non-discarded microarchitectural changes caused by transient executions such as speculative execution, branch prediction, instruction pipelining, and/or out-of-order execution. The transient execution results in a series of instructions (gadgets) which construct covert channel and access/transfer the secret data.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-1037](/wiki/p/weakness/CWE-1037), [CWE-1264](/wiki/p/weakness/CWE-1264), [CWE-1303](/wiki/p/weakness/CWE-1303)

## Prerequisites

- The adversary needs at least user execution access to a system and a maliciously crafted program/application/process with unprivileged code to misuse transient instruction set execution of the CPU.

## Skills required

- High: Detailed knowledge on how various CPU architectures and microcode perform transient execution for various low-level assembly language code instructions/operations.
- High: Detailed knowledge on compiled binaries and operating system shared libraries of instruction sequences, and layout of application and OS/Kernel address spaces for data leakage.

## Consequences

- Confidentiality: Read Data
- Access Control: Bypass Protection Mechanism
- Authorization: Execute Unauthorized Commands

## Mitigations

- Implementation: DAWG (Dynamically Allocated Way Guard) - processor cache properly divided between different programs/processes that don't share resources
- Implementation: KPTI (Kernel Page-Table Isolation) to completely separate user-space and kernel space page tables
- Configuration: Architectural Design of Microcode to limit abuse of speculative execution and out-of-order execution
- Configuration: Disable SharedArrayBuffer for Web Browsers
- Configuration: Disable Copy-on-Write between Cloud VMs
- Configuration: Privilege Checks on Cache Flush Instructions
- Implementation: Non-inclusive Cache Memories to prevent Flush+Reload Attacks

## Source

- [MITRE CAPEC CAPEC-663](https://capec.mitre.org/data/definitions/663.html)
