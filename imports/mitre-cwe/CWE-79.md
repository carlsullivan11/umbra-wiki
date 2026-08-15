---
slug: weakness/CWE-79
title: "CWE-79 — Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')"
page_type: weakness
tags: [cwe, weakness, mitre]
cwe_ids: [CWE-79]
related: [concept/cve-anatomy]
provenance: imported
import_source: mitre-cwe
import_id: CWE-79
updated_at: 2026-08-14
summary: "The product does not neutralize or incorrectly neutralizes user-controllable input before it is placed in output that is used as a web page that is served to other users."
sources:
  - name: MITRE CWE
    url: https://cwe.mitre.org/data/definitions/79.html
---

# CWE-79: Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')

**MITRE CWE weakness**

| | |
|--|--|
| Kind | Weakness |
| Abstraction | Base |
| Status | Stable |
| Likelihood of exploit | High |

## Description

The product does not neutralize or incorrectly neutralizes user-controllable input before it is placed in output that is used as a web page that is served to other users.

There are many variants of cross-site scripting, characterized by a variety of terms or involving different attack topologies. However, they all indicate the same fundamental weakness: improper neutralization of dangerous input between the adversary and a victim.

## Common consequences

- Access Control, Confidentiality: Bypass Protection Mechanism, Read Application Data
- Integrity, Confidentiality, Availability: Execute Unauthorized Code or Commands
- Confidentiality, Integrity, Availability, Access Control: Execute Unauthorized Code or Commands, Bypass Protection Mechanism, Read Application Data

## Mitigations

**Architecture and Design** — Use a vetted library or framework that does not allow this weakness to occur or provides constructs that make this weakness easier to avoid [REF-1482]. Examples of libraries and frameworks that make it easier to generate properly encoded output include Microsoft's Anti-XSS library, the OWASP ESAPI Encoding module, and Apache Wicket.

**Implementation** — Understand the context in which your data will be used and the encoding that will be expected. This is especially important when transmitting data between different components, or when generating outputs that can contain multiple encodings at the same time, such as web pages or multi-part mail messages. Study all expected communication protocols and data representations to determine the required encoding strategies. For any data that will be output to another web page, especially any data that was received from external inputs, use the appropriate encoding on all non-alphanumeric characters. Parts of the same output document may require different encodings, which will vary depending on whether the output is in the: HTML body Element attributes (such as src="XYZ") URIs JavaScript sections Cascading Style Sheets and style property etc. Note that HTML Entity Encoding is only appropriate for the HTML body. Consult the XSS Prevention Cheat Sheet [REF-724] for more details on the types of encoding and escaping that are needed.

**Architecture and Design** — Understand all the potential areas where untrusted inputs can enter your software: parameters or arguments, cookies, anything read from the network, environment variables, reverse DNS lookups, query results, request headers, URL components, e-mail, files, filenames, databases, and any external systems that provide data to the application. Remember that such inputs may be obtained indirectly through API calls.

**Architecture and Design** — For any security checks that are performed on the client side, ensure that these checks are duplicated on the server side, in order to avoid CWE-602. Attackers can bypass the client-side checks by modifying values after the checks have been performed, or by changing the client to remove the client-side checks entirely. Then, these modified values would be submitted to the server.

**Architecture and Design** — If available, use structured mechanisms that automatically enforce the separation between data and code. These mechanisms may be able to provide the relevant quoting, encoding, and validation automatically, instead of relying on the developer to provide this capability at every point where output is generated.

## References

- CWE page: https://cwe.mitre.org/data/definitions/79.html
- CWE list: https://cwe.mitre.org/data/index.html
