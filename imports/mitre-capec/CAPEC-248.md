---
slug: attack-pattern/CAPEC-248
title: "CAPEC-248 — Command Injection"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-248]
cwe_ids: [CWE-77]
related: [weakness/CWE-77]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-248
updated_at: 2026-08-31
summary: "An adversary looking to execute a command of their choosing, injects new items into an existing command thus modifying interpretation away from what was intended. Commands in this context are often standalone strings that are interpreted by a downstream component and cause specif…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/248.html
---

# CAPEC-248: Command Injection

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | High |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary looking to execute a command of their choosing, injects new items into an existing command thus modifying interpretation away from what was intended. Commands in this context are often standalone strings that are interpreted by a downstream component and cause specific responses. This type of attack is possible when untrusted values are used to build these command strings. Weaknesses in input validation or command construction can enable the attack and lead to successful exploitation.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-77](/wiki/p/weakness/CWE-77)

## Prerequisites

- The target application must accept input from the user and then use this input in the construction of commands to be executed. In virtually all cases, this is some form of string input that is concatenated to a constant string defined by the application to form the full command to be executed.

## Consequences

- Confidentiality, Integrity, Availability: Execute Unauthorized Commands

## Mitigations

- All user-controllable input should be validated and filtered for potentially unwanted characters. Using an allowlist for input is desired, but if use of a denylist approach is necessary, then focusing on command related terms and delimiters is necessary.
- Input should be encoded prior to use in commands to make sure command related characters are not treated as part of the command. For example, quotation characters may need to be encoded so that the application does not treat the quotation as a delimiter.
- Input should be parameterized, or restricted to data sections of a command, thus removing the chance that the input will be treated as part of the command itself.

## Source

- [MITRE CAPEC CAPEC-248](https://capec.mitre.org/data/definitions/248.html)
