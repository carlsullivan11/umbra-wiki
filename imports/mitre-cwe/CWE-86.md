---
slug: weakness/CWE-86
title: "CWE-86 — Improper Neutralization of Invalid Characters in Identifiers in Web Pages"
page_type: weakness
tags: [cwe, weakness, mitre]
cwe_ids: [CWE-86]
related: [concept/cve-anatomy]
provenance: imported
import_source: mitre-cwe
import_id: CWE-86
updated_at: 2026-08-14
summary: "The product does not neutralize or incorrectly neutralizes invalid characters or byte sequences in the middle of tag names, URI schemes, and other identifiers."
sources:
  - name: MITRE CWE
    url: https://cwe.mitre.org/data/definitions/86.html
---

# CWE-86: Improper Neutralization of Invalid Characters in Identifiers in Web Pages

**MITRE CWE weakness**

| | |
|--|--|
| Kind | Weakness |
| Abstraction | Variant |
| Status | Draft |
| Likelihood of exploit | — |

## Description

The product does not neutralize or incorrectly neutralizes invalid characters or byte sequences in the middle of tag names, URI schemes, and other identifiers.

Some web browsers may remove these sequences, resulting in output that may have unintended control implications. For example, the product may attempt to remove a "javascript:" URI scheme, but a "java%00script:" URI may bypass this check and still be rendered as active javascript by some browsers, allowing XSS or other attacks.

## Common consequences

- Confidentiality, Integrity, Availability: Read Application Data, Execute Unauthorized Code or Commands

## Mitigations

**Implementation** — Use and specify an output encoding that can be handled by the downstream component that is reading the output. Common encodings include ISO-8859-1, UTF-7, and UTF-8. When an encoding is not specified, a downstream component may choose a different encoding, either by assuming a default encoding or automatically inferring which encoding is being used, which can be erroneous. When the encodings are inconsistent, the downstream component might treat some character or byte sequences as special, even if they are not special in the original encoding. Attackers might then be able to exploit this discrepancy and conduct injection attacks; they even might be able to bypass protection mechanisms that assume the original encoding is also being used by the downstream component. The problem of inconsistent output encodings often arises in web pages. If an encoding is not specified in an HTTP header, web browsers often guess about which encoding is being used. This can open up the browser to subtle XSS attacks.

**Implementation** — To help mitigate XSS attacks against the user's session cookie, set the session cookie to be HttpOnly. In browsers that support the HttpOnly feature (such as more recent versions of Internet Explorer and Firefox), this attribute can prevent the user's session cookie from being accessible to malicious client-side scripts that use document.cookie. This is not a complete solution, since HttpOnly is not supported by all browsers. More importantly, XmlHttpRequest and other powerful browser technologies provide read access to HTTP headers, including the Set-Cookie header in which the HttpOnly flag is set.

## References

- CWE page: https://cwe.mitre.org/data/definitions/86.html
- CWE list: https://cwe.mitre.org/data/index.html
