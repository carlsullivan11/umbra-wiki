---
slug: attack-pattern/CAPEC-47
title: "CAPEC-47 — Buffer Overflow via Parameter Expansion"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-47]
cwe_ids: [CWE-20, CWE-74, CWE-118, CWE-119, CWE-120, CWE-130, CWE-131, CWE-680, CWE-697]
related: [weakness/CWE-20, weakness/CWE-74, weakness/CWE-118, weakness/CWE-119, weakness/CWE-120, weakness/CWE-130, weakness/CWE-131, weakness/CWE-680, weakness/CWE-697]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-47
updated_at: 2026-08-31
summary: "In this attack, the target software is given input that the adversary knows will be modified and expanded in size during processing. This attack relies on the target software failing to anticipate that the expanded data may exceed some internal limit, thereby creating a buffer ov…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/47.html
---

# CAPEC-47: Buffer Overflow via Parameter Expansion

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

In this attack, the target software is given input that the adversary knows will be modified and expanded in size during processing. This attack relies on the target software failing to anticipate that the expanded data may exceed some internal limit, thereby creating a buffer overflow.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-20](/wiki/p/weakness/CWE-20), [CWE-74](/wiki/p/weakness/CWE-74), [CWE-118](/wiki/p/weakness/CWE-118), [CWE-119](/wiki/p/weakness/CWE-119), [CWE-120](/wiki/p/weakness/CWE-120), [CWE-130](/wiki/p/weakness/CWE-130), [CWE-131](/wiki/p/weakness/CWE-131), [CWE-680](/wiki/p/weakness/CWE-680), [CWE-697](/wiki/p/weakness/CWE-697)

## Prerequisites

- The program expands one of the parameters passed to a function with input controlled by the user, but a later function making use of the expanded parameter erroneously considers the original, not the expanded size of the parameter.
- The expanded parameter is used in the context where buffer overflow may become possible due to the incorrect understanding of the parameter size (i.e. thinking that it is smaller than it really is).

## Skills required

- High: Finding this particular buffer overflow may not be trivial. Also, stack and especially heap based buffer overflows require a lot of knowledge if the intended goal is arbitrary code execution. Not only that the adversary needs to write the shell code to accomplish their goals, but the adversary also needs to find a way to get the program execution to jump to the planted shell code. There also needs to be sufficient room for the payload. So not every buffer overflow will be exploitable, even by a skilled adversary.

## Consequences

- Confidentiality, Access Control, Authorization: Gain Privileges
- Availability: Unreliable Execution
- Integrity: Modify Data
- Confidentiality, Integrity, Availability: Execute Unauthorized Commands
- Confidentiality: Read Data

## Mitigations

- Ensure that when parameter expansion happens in the code that the assumptions used to determine the resulting size of the parameter are accurate and that the new size of the parameter is visible to the whole system

## Source

- [MITRE CAPEC CAPEC-47](https://capec.mitre.org/data/definitions/47.html)
