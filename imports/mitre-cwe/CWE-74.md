---
slug: weakness/CWE-74
title: "CWE-74 — Improper Neutralization of Special Elements in Output Used by a Downstream Component ('Injection')"
page_type: weakness
tags: [cwe, weakness, mitre]
cwe_ids: [CWE-74]
related: [concept/cve-anatomy]
provenance: imported
import_source: mitre-cwe
import_id: CWE-74
updated_at: 2026-08-14
summary: "The product constructs all or part of a command, data structure, or record using externally-influenced input from an upstream component, but it does not neutralize or incorrectly neutralizes special e"
sources:
  - name: MITRE CWE
    url: https://cwe.mitre.org/data/definitions/74.html
---

# CWE-74: Improper Neutralization of Special Elements in Output Used by a Downstream Component ('Injection')

**MITRE CWE weakness**

| | |
|--|--|
| Kind | Weakness |
| Abstraction | Class |
| Status | Incomplete |
| Likelihood of exploit | High |

## Description

The product constructs all or part of a command, data structure, or record using externally-influenced input from an upstream component, but it does not neutralize or incorrectly neutralizes special elements that could modify how it is parsed or interpreted when it is sent to a downstream component.



## Common consequences

- Confidentiality: Read Application Data
- Access Control: Bypass Protection Mechanism
- Other: Alter Execution Logic
- Integrity, Other: Other
- Non-Repudiation: Hide Activities

## Mitigations

**Requirements** — Programming languages and supporting technologies might be chosen which are not subject to these issues.

**Implementation** — Utilize an appropriate mix of allowlist and denylist parsing to filter control-plane syntax from all input.

## References

- CWE page: https://cwe.mitre.org/data/definitions/74.html
- CWE list: https://cwe.mitre.org/data/index.html
