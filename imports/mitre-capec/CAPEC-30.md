---
slug: attack-pattern/CAPEC-30
title: "CAPEC-30 — Hijacking a Privileged Thread of Execution"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-30]
cwe_ids: [CWE-270]
mitre_ids: [T1055.003]
related: [weakness/CWE-270, technique/T1055.003]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-30
updated_at: 2026-08-31
summary: "An adversary hijacks a privileged thread of execution by injecting malicious code into a running process. By using a privleged thread to do their bidding, adversaries can evade process-based detection that would stop an attack that creates a new process. This can lead to an adver…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/30.html
---

# CAPEC-30: Hijacking a Privileged Thread of Execution

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Very High |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary hijacks a privileged thread of execution by injecting malicious code into a running process. By using a privleged thread to do their bidding, adversaries can evade process-based detection that would stop an attack that creates a new process. This can lead to an adversary gaining access to the process's memory and can also enable elevated privileges. The most common way to perform this attack is by suspending an existing thread and manipulating its memory.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-270](/wiki/p/weakness/CWE-270)

**ATT&CK techniques:** [T1055.003](/wiki/p/technique/T1055.003)

## Prerequisites

- The application in question employs a threaded model of execution with the threads operating at, or having the ability to switch to, a higher privilege level than normal users
- In order to feasibly execute this class of attacks, the adversary must have the ability to hijack a privileged thread. This ability includes, but is not limited to, modifying environment variables that affect the process the thread belongs to, or calling native OS calls that can suspend and alter process memory. This does not preclude network-based attacks, but makes them conceptually more difficult to identify and execute.

## Skills required

- High: Hijacking a thread involves knowledge of how processes and threads function on the target platform, the design of the target application as well as the ability to identify the primitives to be used or manipulated to hijack the thread.

## Consequences

- Confidentiality, Access Control, Authorization: Gain Privileges
- Confidentiality, Integrity, Availability: Execute Unauthorized Commands

## Mitigations

- Application Architects must be careful to design callback, signal, and similar asynchronous constructs such that they shed excess privilege prior to handing control to user-written (thus untrusted) code.
- Application Architects must be careful to design privileged code blocks such that upon return (successful, failed, or unpredicted) that privilege is shed prior to leaving the block/scope.

## Source

- [MITRE CAPEC CAPEC-30](https://capec.mitre.org/data/definitions/30.html)
