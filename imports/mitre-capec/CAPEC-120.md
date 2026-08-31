---
slug: attack-pattern/CAPEC-120
title: "CAPEC-120 — Double Encoding"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-120]
cwe_ids: [CWE-20, CWE-74, CWE-172, CWE-173, CWE-177, CWE-181, CWE-183, CWE-184, CWE-692, CWE-697]
related: [weakness/CWE-20, weakness/CWE-74, weakness/CWE-172, weakness/CWE-173, weakness/CWE-177, weakness/CWE-181, weakness/CWE-183, weakness/CWE-184, weakness/CWE-692, weakness/CWE-697]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-120
updated_at: 2026-08-31
summary: "The adversary utilizes a repeating of the encoding process for a set of characters (that is, character encoding a character encoding of a character) to obfuscate the payload of a particular request. This may allow the adversary to bypass filters that attempt to detect illegal cha…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/120.html
---

# CAPEC-120: Double Encoding

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | Low |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

The adversary utilizes a repeating of the encoding process for a set of characters (that is, character encoding a character encoding of a character) to obfuscate the payload of a particular request. This may allow the adversary to bypass filters that attempt to detect illegal characters or strings, such as those that might be used in traversal or injection attacks. Filters may be able to catch illegal encoded strings, but may not catch doubly encoded strings. For example, a dot (.), often used in path traversal attacks and therefore often blocked by filters, could be URL encoded as %2E. However, many filters recognize this encoding and would still block the request. In a double encoding, the % in the above URL encoding would be encoded again as %25, resulting in %252E which some filters might not catch, but which could still be interpreted as a dot (.) by interpreters on the target.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-20](/wiki/p/weakness/CWE-20), [CWE-74](/wiki/p/weakness/CWE-74), [CWE-172](/wiki/p/weakness/CWE-172), [CWE-173](/wiki/p/weakness/CWE-173), [CWE-177](/wiki/p/weakness/CWE-177), [CWE-181](/wiki/p/weakness/CWE-181), [CWE-183](/wiki/p/weakness/CWE-183), [CWE-184](/wiki/p/weakness/CWE-184), [CWE-692](/wiki/p/weakness/CWE-692), [CWE-697](/wiki/p/weakness/CWE-697)

## Prerequisites

- The target's filters must fail to detect that a character has been doubly encoded but its interpreting engine must still be able to convert a doubly encoded character to an un-encoded character.
- The application accepts and decodes URL string request.
- The application performs insufficient filtering/canonicalization on the URLs.

## Mitigations

- Assume all input is malicious. Create an allowlist that defines all valid input to the software system based on the requirements specifications. Input that does not match against the allowlist should not be permitted to enter into the system. Test your decoding process against malicious input.
- Be aware of the threat of alternative method of data encoding and obfuscation technique such as IP address encoding.
- When client input is required from web-based forms, avoid using the "GET" method to submit data, as the method causes the form data to be appended to the URL and is easily manipulated. Instead, use the "POST method whenever possible.
- Any security checks should occur after the data has been decoded and validated as correct data format. Do not repeat decoding process, if bad character are left after decoding process, treat the data as suspicious, and fail the validation process.
- Refer to the RFCs to safely decode URL.
- Regular expression can be used to match safe URL patterns. However, that may discard valid URL requests if the regular expression is too restrictive.
- There are tools to scan HTTP requests to the server for valid URL such as URLScan from Microsoft (http://www.microsoft.com/technet/security/tools/urlscan.mspx).

## Source

- [MITRE CAPEC CAPEC-120](https://capec.mitre.org/data/definitions/120.html)
