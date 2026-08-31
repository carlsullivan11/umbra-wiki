---
slug: attack-pattern/CAPEC-88
title: "CAPEC-88 — OS Command Injection"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-88]
cwe_ids: [CWE-20, CWE-78, CWE-88, CWE-697]
related: [weakness/CWE-20, weakness/CWE-78, weakness/CWE-88, weakness/CWE-697]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-88
updated_at: 2026-08-31
summary: "In this type of an attack, an adversary injects operating system commands into existing application functions. An application that uses untrusted input to build command strings is vulnerable. An adversary can leverage OS command injection in an application to elevate privileges, …"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/88.html
---

# CAPEC-88: OS Command Injection

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

In this type of an attack, an adversary injects operating system commands into existing application functions. An application that uses untrusted input to build command strings is vulnerable. An adversary can leverage OS command injection in an application to elevate privileges, execute arbitrary commands and compromise the underlying operating system.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-20](/wiki/p/weakness/CWE-20), [CWE-78](/wiki/p/weakness/CWE-78), [CWE-88](/wiki/p/weakness/CWE-88), [CWE-697](/wiki/p/weakness/CWE-697)

## Prerequisites

- User controllable input used as part of commands to the underlying operating system.

## Skills required

- High: The attacker needs to have knowledge of not only the application to exploit but also the exact nature of commands that pertain to the target operating system. This may involve, though not always, knowledge of specific assembly commands for the platform.

## Consequences

- Confidentiality, Integrity, Availability: Execute Unauthorized Commands
- Confidentiality, Access Control, Authorization: Gain Privileges, Bypass Protection Mechanism
- Confidentiality: Read Data

## Mitigations

- Use language APIs rather than relying on passing data to the operating system shell or command line. Doing so ensures that the available protection mechanisms in the language are intact and applicable.
- Filter all incoming data to escape or remove characters or strings that can be potentially misinterpreted as operating system or shell commands
- All application processes should be run with the minimal privileges required. Also, processes must shed privileges as soon as they no longer require them.

## Source

- [MITRE CAPEC CAPEC-88](https://capec.mitre.org/data/definitions/88.html)
