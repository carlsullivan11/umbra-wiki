---
slug: weakness/CWE-15
title: "CWE-15 — External Control of System or Configuration Setting"
page_type: weakness
tags: [cwe, weakness, mitre]
cwe_ids: [CWE-15]
related: [concept/cve-anatomy]
provenance: imported
import_source: mitre-cwe
import_id: CWE-15
updated_at: 2026-08-14
summary: "One or more system settings or configuration elements can be externally controlled by a user."
sources:
  - name: MITRE CWE
    url: https://cwe.mitre.org/data/definitions/15.html
---

# CWE-15: External Control of System or Configuration Setting

**MITRE CWE weakness**

| | |
|--|--|
| Kind | Weakness |
| Abstraction | Base |
| Status | Incomplete |
| Likelihood of exploit | — |

## Description

One or more system settings or configuration elements can be externally controlled by a user.

Allowing external control of system settings can disrupt service or cause an application to behave in unexpected, and potentially malicious ways.

## Common consequences

- Other: Varies by Context

## Mitigations

**Architecture and Design** — Compartmentalize the system to have "safe" areas where trust boundaries can be unambiguously drawn. Do not allow sensitive data to go outside of the trust boundary and always be careful when interfacing with a compartment outside of the safe area. Ensure that appropriate compartmentalization is built into the system design, and the compartmentalization allows for and reinforces privilege separation functionality. Architects and designers should rely on the principle of least privilege to decide the appropriate time to use privileges and the time to drop privileges.

**Implementation** — Because setting manipulation covers a diverse set of functions, any attempt at illustrating it will inevitably be incomplete. Rather than searching for a tight-knit relationship between the functions addressed in the setting manipulation category, take a step back and consider the sorts of system values that an attacker should not be allowed to control.

**Implementation** — In general, do not allow user-provided or otherwise untrusted data to control sensitive values. The leverage that an attacker gains by controlling these values is not always immediately obvious, but do not underestimate the creativity of the attacker.

## References

- CWE page: https://cwe.mitre.org/data/definitions/15.html
- CWE list: https://cwe.mitre.org/data/index.html
