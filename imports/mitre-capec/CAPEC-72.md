---
slug: attack-pattern/CAPEC-72
title: "CAPEC-72 — URL Encoding"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-72]
cwe_ids: [CWE-20, CWE-73, CWE-74, CWE-172, CWE-173, CWE-177]
related: [weakness/CWE-20, weakness/CWE-73, weakness/CWE-74, weakness/CWE-172, weakness/CWE-173, weakness/CWE-177]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-72
updated_at: 2026-08-31
summary: "This attack targets the encoding of the URL. An adversary can take advantage of the multiple way of encoding an URL and abuse the interpretation of the URL."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/72.html
---

# CAPEC-72: URL Encoding

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

This attack targets the encoding of the URL. An adversary can take advantage of the multiple way of encoding an URL and abuse the interpretation of the URL.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-20](/wiki/p/weakness/CWE-20), [CWE-73](/wiki/p/weakness/CWE-73), [CWE-74](/wiki/p/weakness/CWE-74), [CWE-172](/wiki/p/weakness/CWE-172), [CWE-173](/wiki/p/weakness/CWE-173), [CWE-177](/wiki/p/weakness/CWE-177)

## Prerequisites

- The application should accepts and decodes URL input.
- The application performs insufficient filtering/canonicalization on the URLs.

## Skills required

- Low: An adversary can try special characters in the URL and bypass the URL validation.
- Medium: The adversary may write a script to defeat the input filtering mechanism.

## Consequences

- Confidentiality: Read Data
- Availability: Resource Consumption
- Confidentiality, Integrity, Availability: Execute Unauthorized Commands
- Confidentiality, Access Control, Authorization: Gain Privileges

## Mitigations

- Refer to the RFCs to safely decode URL.
- Regular expression can be used to match safe URL patterns. However, that may discard valid URL requests if the regular expression is too restrictive.
- There are tools to scan HTTP requests to the server for valid URL such as URLScan from Microsoft (http://www.microsoft.com/technet/security/tools/urlscan.mspx).
- Any security checks should occur after the data has been decoded and validated as correct data format. Do not repeat decoding process, if bad character are left after decoding process, treat the data as suspicious, and fail the validation process.
- Assume all input is malicious. Create an allowlist that defines all valid input to the software system based on the requirements specifications. Input that does not match against the allowlist should not be permitted to enter into the system. Test your decoding process against malicious input.
- Be aware of the threat of alternative method of data encoding and obfuscation technique such as IP address encoding. (See related guideline section)
- When client input is required from web-based forms, avoid using the "GET" method to submit data, as the method causes the form data to be appended to the URL and is easily manipulated. Instead, use the "POST method whenever possible.

## Source

- [MITRE CAPEC CAPEC-72](https://capec.mitre.org/data/definitions/72.html)
