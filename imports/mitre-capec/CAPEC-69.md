---
slug: attack-pattern/CAPEC-69
title: "CAPEC-69 — Target Programs with Elevated Privileges"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-69]
cwe_ids: [CWE-15, CWE-250]
related: [weakness/CWE-15, weakness/CWE-250]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-69
updated_at: 2026-08-31
summary: "This attack targets programs running with elevated privileges. The adversary tries to leverage a vulnerability in the running program and get arbitrary code to execute with elevated privileges."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/69.html
---

# CAPEC-69: Target Programs with Elevated Privileges

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Very High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

This attack targets programs running with elevated privileges. The adversary tries to leverage a vulnerability in the running program and get arbitrary code to execute with elevated privileges.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-15](/wiki/p/weakness/CWE-15), [CWE-250](/wiki/p/weakness/CWE-250)

## Prerequisites

- The targeted program runs with elevated OS privileges.
- The targeted program accepts input data from the user or from another program.
- The targeted program is giving away information about itself. Before performing such attack, an eventual attacker may need to gather information about the services running on the host target. The more the host target is verbose about the services that are running (version number of application, etc.) the more information can be gather by an attacker.
- This attack often requires communicating with the host target services directly. For instance Telnet may be enough to communicate with the host target.

## Skills required

- Low: An attacker can use a tool to scan and automatically launch an attack against known issues. A tool can also repeat a sequence of instructions and try to brute force the service on the host target, an example of that would be the flooding technique.
- Medium: More advanced attack may require knowledge of the protocol spoken by the host service.

## Consequences

- Confidentiality, Integrity, Availability: Execute Unauthorized Commands
- Confidentiality, Access Control, Authorization: Gain Privileges
- Availability: Resource Consumption

## Mitigations

- Apply the principle of least privilege.
- Validate all untrusted data.
- Apply the latest patches.
- Scan your services and disable the ones which are not needed and are exposed unnecessarily. Exposing programs increases the attack surface. Only expose the services which are needed and have security mechanisms such as authentication built around them.
- Avoid revealing information about your system (e.g., version of the program) to anonymous users.
- Make sure that your program or service fail safely. What happen if the communication protocol is interrupted suddenly? What happen if a parameter is missing? Does your system have resistance and resilience to attack? Fail safely when a resource exhaustion occurs.
- If possible use a sandbox model which limits the actions that programs can take. A sandbox restricts a program to a set of privileges and commands that make it difficult or impossible for the program to cause any damage.
- Check your program for buffer overflow and format String vulnerabilities which can lead to execution of malicious code.

## Source

- [MITRE CAPEC CAPEC-69](https://capec.mitre.org/data/definitions/69.html)
