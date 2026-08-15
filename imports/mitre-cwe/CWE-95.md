---
slug: weakness/CWE-95
title: "CWE-95 — Improper Neutralization of Directives in Dynamically Evaluated Code ('Eval Injection')"
page_type: weakness
tags: [cwe, weakness, mitre]
cwe_ids: [CWE-95]
related: [concept/cve-anatomy]
provenance: imported
import_source: mitre-cwe
import_id: CWE-95
updated_at: 2026-08-14
summary: "The product receives input from an upstream component, but it does not neutralize or incorrectly neutralizes code syntax before using the input in a dynamic evaluation call (e.g. 'eval')."
sources:
  - name: MITRE CWE
    url: https://cwe.mitre.org/data/definitions/95.html
---

# CWE-95: Improper Neutralization of Directives in Dynamically Evaluated Code ('Eval Injection')

**MITRE CWE weakness**

| | |
|--|--|
| Kind | Weakness |
| Abstraction | Variant |
| Status | Incomplete |
| Likelihood of exploit | Medium |

## Description

The product receives input from an upstream component, but it does not neutralize or incorrectly neutralizes code syntax before using the input in a dynamic evaluation call (e.g. "eval").



## Common consequences

- Confidentiality: Read Files or Directories, Read Application Data
- Access Control: Bypass Protection Mechanism
- Access Control: Gain Privileges or Assume Identity
- Integrity, Confidentiality, Availability, Other: Execute Unauthorized Code or Commands
- Non-Repudiation: Hide Activities

## Mitigations

**Architecture and Design** — If possible, refactor your code so that it does not need to use eval() at all.

**Implementation** — Assume all input is malicious. Use an "accept known good" input validation strategy, i.e., use a list of acceptable inputs that strictly conform to specifications. Reject any input that does not strictly conform to specifications, or transform it into something that does. When performing input validation, consider all potentially relevant properties, including length, type of input, the full range of acceptable values, missing or extra inputs, syntax, consistency across related fields, and conformance to business rules. As an example of business rule logic, "boat" may be syntactically valid because it only contains alphanumeric characters, but it is not valid if the input is only expected to contain colors such as "red" or "blue." Do not rely exclusively on looking for malicious or malformed inputs. This is likely to miss at least one undesirable input, especially if the code's environment changes. This can give attackers enough room to bypass the intended validation. However, denylists can be useful for detecting potential attacks or determining which inputs are so malformed that they should be rejected outright.

**Implementation** — Inputs should be decoded and canonicalized to the application's current internal representation before being validated (CWE-180, CWE-181). Make sure that your application does not inadvertently decode the same input twice (CWE-174). Such errors could be used to bypass allowlist schemes by introducing dangerous inputs after they have been checked. Use libraries such as the OWASP ESAPI Canonicalization control. Consider performing repeated canonicalization until your input does not change any more. This will avoid double-decoding and similar scenarios, but it might inadvertently modify inputs that are allowed to contain properly-encoded dangerous content.

**Implementation** — For Python programs, it is frequently encouraged to use the ast.literal_eval() function instead of eval, since it is intentionally designed to avoid executing code. However, an adversary could still cause excessive memory or stack consumption via deeply nested structures [REF-1372], so the python documentation discourages use of ast.literal_eval() on untrusted data [REF-1373].

## References

- CWE page: https://cwe.mitre.org/data/definitions/95.html
- CWE list: https://cwe.mitre.org/data/index.html
