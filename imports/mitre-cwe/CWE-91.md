---
slug: weakness/CWE-91
title: "CWE-91 — XML Injection (aka Blind XPath Injection)"
page_type: weakness
tags: [cwe, weakness, mitre]
cwe_ids: [CWE-91]
related: [concept/cve-anatomy]
provenance: imported
import_source: mitre-cwe
import_id: CWE-91
updated_at: 2026-08-14
summary: "The product does not properly neutralize special elements that are used in XML, allowing attackers to modify the syntax, content, or commands of the XML before it is processed by an end system."
sources:
  - name: MITRE CWE
    url: https://cwe.mitre.org/data/definitions/91.html
---

# CWE-91: XML Injection (aka Blind XPath Injection)

**MITRE CWE weakness**

| | |
|--|--|
| Kind | Weakness |
| Abstraction | Base |
| Status | Draft |
| Likelihood of exploit | — |

## Description

The product does not properly neutralize special elements that are used in XML, allowing attackers to modify the syntax, content, or commands of the XML before it is processed by an end system.

Within XML, special elements could include reserved words or characters such as "<", ">", """, and "&", which could then be used to add new data or modify XML syntax.

## Common consequences

- Confidentiality, Integrity, Availability: Execute Unauthorized Code or Commands, Read Application Data, Modify Application Data

## Mitigations

**Implementation** — Assume all input is malicious. Use an "accept known good" input validation strategy, i.e., use a list of acceptable inputs that strictly conform to specifications. Reject any input that does not strictly conform to specifications, or transform it into something that does. When performing input validation, consider all potentially relevant properties, including length, type of input, the full range of acceptable values, missing or extra inputs, syntax, consistency across related fields, and conformance to business rules. As an example of business rule logic, "boat" may be syntactically valid because it only contains alphanumeric characters, but it is not valid if the input is only expected to contain colors such as "red" or "blue." Do not rely exclusively on looking for malicious or malformed inputs. This is likely to miss at least one undesirable input, especially if the code's environment changes. This can give attackers enough room to bypass the intended validation. However, denylists can be useful for detecting potential attacks or determining which inputs are so malformed that they should be rejected outright.

## References

- CWE page: https://cwe.mitre.org/data/definitions/91.html
- CWE list: https://cwe.mitre.org/data/index.html
