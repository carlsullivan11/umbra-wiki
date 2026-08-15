---
slug: weakness/CWE-77
title: "CWE-77 — Improper Neutralization of Special Elements used in a Command ('Command Injection')"
page_type: weakness
tags: [cwe, weakness, mitre]
cwe_ids: [CWE-77]
related: [concept/cve-anatomy]
provenance: imported
import_source: mitre-cwe
import_id: CWE-77
updated_at: 2026-08-14
summary: "The product constructs all or part of a command using externally-influenced input from an upstream component, but it does not neutralize or incorrectly neutralizes special elements that could modify t"
sources:
  - name: MITRE CWE
    url: https://cwe.mitre.org/data/definitions/77.html
---

# CWE-77: Improper Neutralization of Special Elements used in a Command ('Command Injection')

**MITRE CWE weakness**

| | |
|--|--|
| Kind | Weakness |
| Abstraction | Class |
| Status | Draft |
| Likelihood of exploit | High |

## Description

The product constructs all or part of a command using externally-influenced input from an upstream component, but it does not neutralize or incorrectly neutralizes special elements that could modify the intended command when it is sent to a downstream component.

Many protocols and products have their own custom command language. While OS or shell command strings are frequently discovered and targeted, developers may not realize that these other command languages might also be vulnerable to attacks.

## Common consequences

- Integrity, Confidentiality, Availability: Execute Unauthorized Code or Commands

## Mitigations

**Architecture and Design** — If at all possible, use library calls rather than external processes to recreate the desired functionality.

**Implementation** — If possible, ensure that all external commands called from the program are statically created.

**Implementation** — Assume all input is malicious. Use an "accept known good" input validation strategy, i.e., use a list of acceptable inputs that strictly conform to specifications. Reject any input that does not strictly conform to specifications, or transform it into something that does. When performing input validation, consider all potentially relevant properties, including length, type of input, the full range of acceptable values, missing or extra inputs, syntax, consistency across related fields, and conformance to business rules. As an example of business rule logic, "boat" may be syntactically valid because it only contains alphanumeric characters, but it is not valid if the input is only expected to contain colors such as "red" or "blue." Do not rely exclusively on looking for malicious or malformed inputs. This is likely to miss at least one undesirable input, especially if the code's environment changes. This can give attackers enough room to bypass the intended validation. However, denylists can be useful for detecting potential attacks or determining which inputs are so malformed that they should be rejected outright.

**Operation** — Run time: Run time policy enforcement may be used in an allowlist fashion to prevent use of any non-sanctioned commands.

**System Configuration** — Assign permissions that prevent the user from accessing/opening privileged files.

## References

- CWE page: https://cwe.mitre.org/data/definitions/77.html
- CWE list: https://cwe.mitre.org/data/index.html
