---
slug: weakness/CWE-90
title: "CWE-90 — Improper Neutralization of Special Elements used in an LDAP Query ('LDAP Injection')"
page_type: weakness
tags: [cwe, weakness, mitre]
cwe_ids: [CWE-90]
related: [concept/cve-anatomy]
provenance: imported
import_source: mitre-cwe
import_id: CWE-90
updated_at: 2026-08-14
summary: "The product constructs all or part of an LDAP query using externally-influenced input from an upstream component, but it does not neutralize or incorrectly neutralizes special elements that could modi"
sources:
  - name: MITRE CWE
    url: https://cwe.mitre.org/data/definitions/90.html
---

# CWE-90: Improper Neutralization of Special Elements used in an LDAP Query ('LDAP Injection')

**MITRE CWE weakness**

| | |
|--|--|
| Kind | Weakness |
| Abstraction | Base |
| Status | Draft |
| Likelihood of exploit | — |

## Description

The product constructs all or part of an LDAP query using externally-influenced input from an upstream component, but it does not neutralize or incorrectly neutralizes special elements that could modify the intended LDAP query when it is sent to a downstream component.



## Common consequences

- Confidentiality, Integrity, Availability: Execute Unauthorized Code or Commands, Read Application Data, Modify Application Data

## Mitigations

**Implementation** — Assume all input is malicious. Use an "accept known good" input validation strategy, i.e., use a list of acceptable inputs that strictly conform to specifications. Reject any input that does not strictly conform to specifications, or transform it into something that does. When performing input validation, consider all potentially relevant properties, including length, type of input, the full range of acceptable values, missing or extra inputs, syntax, consistency across related fields, and conformance to business rules. As an example of business rule logic, "boat" may be syntactically valid because it only contains alphanumeric characters, but it is not valid if the input is only expected to contain colors such as "red" or "blue." Do not rely exclusively on looking for malicious or malformed inputs. This is likely to miss at least one undesirable input, especially if the code's environment changes. This can give attackers enough room to bypass the intended validation. However, denylists can be useful for detecting potential attacks or determining which inputs are so malformed that they should be rejected outright.

## References

- CWE page: https://cwe.mitre.org/data/definitions/90.html
- CWE list: https://cwe.mitre.org/data/index.html
