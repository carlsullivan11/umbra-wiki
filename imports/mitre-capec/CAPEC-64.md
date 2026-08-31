---
slug: attack-pattern/CAPEC-64
title: "CAPEC-64 — Using Slashes and URL Encoding Combined to Bypass Validation Logic"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-64]
cwe_ids: [CWE-20, CWE-22, CWE-73, CWE-74, CWE-172, CWE-173, CWE-177, CWE-697, CWE-707]
related: [weakness/CWE-20, weakness/CWE-22, weakness/CWE-73, weakness/CWE-74, weakness/CWE-172, weakness/CWE-173, weakness/CWE-177, weakness/CWE-697, weakness/CWE-707]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-64
updated_at: 2026-08-31
summary: "This attack targets the encoding of the URL combined with the encoding of the slash characters. An attacker can take advantage of the multiple ways of encoding a URL and abuse the interpretation of the URL. A URL may contain special character that need special syntax handling in …"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/64.html
---

# CAPEC-64: Using Slashes and URL Encoding Combined to Bypass Validation Logic

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

This attack targets the encoding of the URL combined with the encoding of the slash characters. An attacker can take advantage of the multiple ways of encoding a URL and abuse the interpretation of the URL. A URL may contain special character that need special syntax handling in order to be interpreted. Special characters are represented using a percentage character followed by two digits representing the octet code of the original character (%HEX-CODE). For instance US-ASCII space character would be represented with %20. This is often referred as escaped ending or percent-encoding. Since the server decodes the URL from the requests, it may restrict the access to some URL paths by validating and filtering out the URL requests it received. An attacker will try to craft an URL with a sequence of special characters which once interpreted by the server will be equivalent to a forbidden URL. It can be difficult to protect against this attack since the URL can contain other format of encoding such as UTF-8 encoding, Unicode-encoding, etc.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-20](/wiki/p/weakness/CWE-20), [CWE-22](/wiki/p/weakness/CWE-22), [CWE-73](/wiki/p/weakness/CWE-73), [CWE-74](/wiki/p/weakness/CWE-74), [CWE-172](/wiki/p/weakness/CWE-172), [CWE-173](/wiki/p/weakness/CWE-173), [CWE-177](/wiki/p/weakness/CWE-177), [CWE-697](/wiki/p/weakness/CWE-697), [CWE-707](/wiki/p/weakness/CWE-707)

## Prerequisites

- The application accepts and decodes URL string request.
- The application performs insufficient filtering/canonicalization on the URLs.

## Skills required

- Low: An attacker can try special characters in the URL and bypass the URL validation.
- Medium: The attacker may write a script to defeat the input filtering mechanism.

## Consequences

- Availability: Resource Consumption
- Confidentiality, Integrity, Availability: Execute Unauthorized Commands
- Confidentiality: Read Data
- Confidentiality, Access Control, Authorization: Gain Privileges

## Mitigations

- Assume all input is malicious. Create an allowlist that defines all valid input to the software system based on the requirements specifications. Input that does not match against the allowlist should not be permitted to enter into the system. Test your decoding process against malicious input.
- Be aware of the threat of alternative method of data encoding and obfuscation technique such as IP address encoding.
- When client input is required from web-based forms, avoid using the "GET" method to submit data, as the method causes the form data to be appended to the URL and is easily manipulated. Instead, use the "POST method whenever possible.
- Any security checks should occur after the data has been decoded and validated as correct data format. Do not repeat decoding process, if bad character are left after decoding process, treat the data as suspicious, and fail the validation process.
- Refer to the RFCs to safely decode URL.
- Regular expression can be used to match safe URL patterns. However, that may discard valid URL requests if the regular expression is too restrictive.
- There are tools to scan HTTP requests to the server for valid URL such as URLScan from Microsoft (http://www.microsoft.com/technet/security/tools/urlscan.mspx).

## Source

- [MITRE CAPEC CAPEC-64](https://capec.mitre.org/data/definitions/64.html)
