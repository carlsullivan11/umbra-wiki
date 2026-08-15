---
slug: weakness/CWE-99
title: "CWE-99 — Improper Control of Resource Identifiers ('Resource Injection')"
page_type: weakness
tags: [cwe, weakness, mitre]
cwe_ids: [CWE-99]
related: [concept/cve-anatomy]
provenance: imported
import_source: mitre-cwe
import_id: CWE-99
updated_at: 2026-08-14
summary: "The product receives input from an upstream component, but it does not restrict or incorrectly restricts the input before it is used as an identifier for a resource that may be outside the intended sp"
sources:
  - name: MITRE CWE
    url: https://cwe.mitre.org/data/definitions/99.html
---

# CWE-99: Improper Control of Resource Identifiers ('Resource Injection')

**MITRE CWE weakness**

| | |
|--|--|
| Kind | Weakness |
| Abstraction | Class |
| Status | Draft |
| Likelihood of exploit | High |

## Description

The product receives input from an upstream component, but it does not restrict or incorrectly restricts the input before it is used as an identifier for a resource that may be outside the intended sphere of control.

A resource injection issue occurs when the following two conditions are met: An attacker can specify the identifier used to access a system resource. For example, an attacker might be able to specify part of the name of a file to be opened or a port number to be used. By specifying the resource, the attacker gains a capability that would not otherwise be permitted. For example, the program may give the attacker the ability to overwrite the specified file, run with a configuration controlled by the attacker, or transmit sensitive information to a third-party server. This may enable an attacker to access or modify otherwise protected system resources.

## Common consequences

- Confidentiality, Integrity: Read Application Data, Modify Application Data, Read Files or Directories, Modify Files or Directories

## Mitigations

**Implementation** — Assume all input is malicious. Use an "accept known good" input validation strategy, i.e., use a list of acceptable inputs that strictly conform to specifications. Reject any input that does not strictly conform to specifications, or transform it into something that does. When performing input validation, consider all potentially relevant properties, including length, type of input, the full range of acceptable values, missing or extra inputs, syntax, consistency across related fields, and conformance to business rules. As an example of business rule logic, "boat" may be syntactically valid because it only contains alphanumeric characters, but it is not valid if the input is only expected to contain colors such as "red" or "blue." Do not rely exclusively on looking for malicious or malformed inputs. This is likely to miss at least one undesirable input, especially if the code's environment changes. This can give attackers enough room to bypass the intended validation. However, it can be useful for detecting potential attacks or determining which inputs are so malformed that they should be rejected outright.

## References

- CWE page: https://cwe.mitre.org/data/definitions/99.html
- CWE list: https://cwe.mitre.org/data/index.html
