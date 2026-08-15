---
slug: weakness/CWE-20
title: "CWE-20 — Improper Input Validation"
page_type: weakness
tags: [cwe, weakness, mitre]
cwe_ids: [CWE-20]
related: [concept/cve-anatomy]
provenance: imported
import_source: mitre-cwe
import_id: CWE-20
updated_at: 2026-08-14
summary: "The product receives input or data, but it does not validate or incorrectly validates that the input has the properties that are required to process the data safely and correctly."
sources:
  - name: MITRE CWE
    url: https://cwe.mitre.org/data/definitions/20.html
---

# CWE-20: Improper Input Validation

**MITRE CWE weakness**

| | |
|--|--|
| Kind | Weakness |
| Abstraction | Class |
| Status | Stable |
| Likelihood of exploit | High |

## Description

The product receives input or data, but it does not validate or incorrectly validates that the input has the properties that are required to process the data safely and correctly.

Input validation is a frequently-used technique for checking potentially dangerous inputs in order to ensure that the inputs are safe for processing within the code, or when communicating with other components. Input can consist of: raw data - strings, numbers, parameters, file contents, etc. metadata - information about the raw data, such as headers or size Data can be simple or structured. Structured data can be composed of many nested layers, composed of combinations of metadata and raw data, with other simple or structured data. Many properties of raw data or metadata may need to be validated upon entry into the code, such as: specified quantities such as size, length, frequency, price, rate, number of operations, time, etc. implied or derived quantities, such as the actual size of a file instead of a specified size indexes, offsets, or positions into more complex data structures symbolic keys or other elements into hash tables, associative arrays, etc. well-formedness, i.e. syntactic correctness - compliance with expected syntax lexical token correctness - compliance with rules for what is treated as a token specified or derived type - the actual type of the input (or what the input appears to be) consistency - between individual data elements, between raw data and metadata, between references, etc. conformance to domain-specific rules, e.g. business logic equivalence - ensuring that equivalent inputs are treated the same authenticity, ownership, or other attestations about the input, e.g. a cryptographic signature to prove the source of the data Implied or derived properties of data must often be calculated or inferred by the code itself. Errors in deriving properties may be considered a contributing factor to improper input validation.

## Common consequences

- Availability: DoS: Crash, Exit, or Restart, DoS: Resource Consumption (CPU), DoS: Resource Consumption (Memory)
- Confidentiality: Read Memory, Read Files or Directories
- Integrity, Confidentiality, Availability: Modify Memory, Execute Unauthorized Code or Commands

## Mitigations

**Architecture and Design** — Consider using language-theoretic security (LangSec) techniques that characterize inputs using a formal language and build "recognizers" for that language. This effectively requires parsing to be a distinct layer that effectively enforces a boundary between raw input and internal data representations, instead of allowing parser code to be scattered throughout the program, where it could be subject to errors or inconsistencies that create weaknesses. [REF-1109] [REF-1110] [REF-1111]

**Architecture and Design** — Use an input validation framework such as Struts or the OWASP ESAPI Validation API. Note that using a framework does not automatically address all input validation problems; be mindful of weaknesses that could arise from misusing the framework itself (CWE-1173).

**Architecture and Design** — Understand all the potential areas where untrusted inputs can enter the product, including but not limited to: parameters or arguments, cookies, anything read from the network, environment variables, reverse DNS lookups, query results, request headers, URL components, e-mail, files, filenames, databases, and any external systems that provide data to the application. Remember that such inputs may be obtained indirectly through API calls.

**Implementation** — Assume all input is malicious. Use an "accept known good" input validation strategy, i.e., use a list of acceptable inputs that strictly conform to specifications. Reject any input that does not strictly conform to specifications, or transform it into something that does. When performing input validation, consider all potentially relevant properties, including length, type of input, the full range of acceptable values, missing or extra inputs, syntax, consistency across related fields, and conformance to business rules. As an example of business rule logic, "boat" may be syntactically valid because it only contains alphanumeric characters, but it is not valid if the input is only expected to contain colors such as "red" or "blue." Do not rely exclusively on looking for malicious or malformed inputs. This is likely to miss at least one undesirable input, especially if the code's environment changes. This can give attackers enough room to bypass the intended validation. However, denylists can be useful for detecting potential attacks or determining which inputs are so malformed that they should be rejected outright.

**Architecture and Design** — For any security checks that are performed on the client side, ensure that these checks are duplicated on the server side, in order to avoid CWE-602. Attackers can bypass the client-side checks by modifying values after the checks have been performed, or by changing the client to remove the client-side checks entirely. Then, these modified values would be submitted to the server. Even though client-side checks provide minimal benefits with respect to server-side security, they are still useful. First, they can support intrusion detection. If the server receives input that should have been rejected by the client, then it may be an indication of an attack. Second, client-side error-checking can provide helpful feedback to the user about the expectations for valid input. Third, there may be a reduction in server-side processing time for accidental input errors, although this is typically a small savings.

## References

- CWE page: https://cwe.mitre.org/data/definitions/20.html
- CWE list: https://cwe.mitre.org/data/index.html
