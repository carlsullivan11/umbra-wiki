---
slug: attack-pattern/CAPEC-670
title: "CAPEC-670 — Software Development Tools Maliciously Altered"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-670]
mitre_ids: [T1127, T1195.001]
related: [technique/T1127, technique/T1195.001]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-670
updated_at: 2026-08-31
summary: "An adversary with the ability to alter tools used in a development environment causes software to be developed with maliciously modified tools. Such tools include requirements management and database tools, software design tools, configuration management tools, compilers, system …"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/670.html
---

# CAPEC-670: Software Development Tools Maliciously Altered

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary with the ability to alter tools used in a development environment causes software to be developed with maliciously modified tools. Such tools include requirements management and database tools, software design tools, configuration management tools, compilers, system build tools, and software performance testing and load testing tools. The adversary then carries out malicious acts once the software is deployed including malware infection of other systems to support further compromises.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**ATT&CK techniques:** [T1127](/wiki/p/technique/T1127), [T1195.001](/wiki/p/technique/T1195.001)

## Prerequisites

- An adversary would need to have access to a targeted developer’s development environment and in particular to tools used to design, create, test and manage software, where the adversary could ensure malicious code is included in software packages built through alteration or substitution of tools in the environment used in the development of software.

## Skills required

- High: Ability to leverage common delivery mechanisms (e.g., email attachments, removable media) to infiltrate a development environment to gain access to software development tools for the purpose of malware insertion into an existing tool or replacement of an existing tool with a maliciously altered copy.

## Consequences

- Integrity: Execute Unauthorized Commands
- Access Control: Gain Privileges
- Confidentiality: Modify Data, Read Data

## Mitigations

- Have a security concept of operations (CONOPS) for the development environment that includes: Maintaining strict security administration and configuration management of requirements management and database tools, software design tools, configuration management tools, compilers, system build tools, and software performance testing and load testing tools.
- Avoid giving elevated privileges to developers.

## Source

- [MITRE CAPEC CAPEC-670](https://capec.mitre.org/data/definitions/670.html)
