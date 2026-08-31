---
slug: attack-pattern/CAPEC-78
title: "CAPEC-78 — Using Escaped Slashes in Alternate Encoding"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-78]
cwe_ids: [CWE-20, CWE-22, CWE-73, CWE-74, CWE-172, CWE-173, CWE-180, CWE-181, CWE-697, CWE-707]
related: [weakness/CWE-20, weakness/CWE-22, weakness/CWE-73, weakness/CWE-74, weakness/CWE-172, weakness/CWE-173, weakness/CWE-180, weakness/CWE-181, weakness/CWE-697, weakness/CWE-707]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-78
updated_at: 2026-08-31
summary: "This attack targets the use of the backslash in alternate encoding. An adversary can provide a backslash as a leading character and causes a parser to believe that the next character is special. This is called an escape. By using that trick, the adversary tries to exploit alterna…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/78.html
---

# CAPEC-78: Using Escaped Slashes in Alternate Encoding

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

This attack targets the use of the backslash in alternate encoding. An adversary can provide a backslash as a leading character and causes a parser to believe that the next character is special. This is called an escape. By using that trick, the adversary tries to exploit alternate ways to encode the same character which leads to filter problems and opens avenues to attack.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-20](/wiki/p/weakness/CWE-20), [CWE-22](/wiki/p/weakness/CWE-22), [CWE-73](/wiki/p/weakness/CWE-73), [CWE-74](/wiki/p/weakness/CWE-74), [CWE-172](/wiki/p/weakness/CWE-172), [CWE-173](/wiki/p/weakness/CWE-173), [CWE-180](/wiki/p/weakness/CWE-180), [CWE-181](/wiki/p/weakness/CWE-181), [CWE-697](/wiki/p/weakness/CWE-697), [CWE-707](/wiki/p/weakness/CWE-707)

## Prerequisites

- The application accepts the backlash character as escape character.
- The application server does incomplete input data decoding, filtering and validation.

## Skills required

- Low: The adversary can naively try backslash character and discover that the target host uses it as escape character.
- Medium: The adversary may need deep understanding of the host target in order to exploit the vulnerability. The adversary may also use automated tools to probe for this vulnerability.

## Consequences

- Confidentiality: Read Data
- Availability: Resource Consumption
- Confidentiality, Integrity, Availability: Execute Unauthorized Commands
- Confidentiality, Access Control, Authorization: Bypass Protection Mechanism

## Mitigations

- Verify that the user-supplied data does not use backslash character to escape malicious characters.
- Assume all input is malicious. Create an allowlist that defines all valid input to the software system based on the requirements specifications. Input that does not match against the allowlist should not be permitted to enter into the system.
- Be aware of the threat of alternative method of data encoding.
- Regular expressions can be used to filter out backslash. Make sure you decode before filtering and validating the untrusted input data.
- In the case of path traversals, use the principle of least privilege when determining access rights to file systems. Do not allow users to access directories/files that they should not access.
- Any security checks should occur after the data has been decoded and validated as correct data format. Do not repeat decoding process, if bad character are left after decoding process, treat the data as suspicious, and fail the validation process.
- Avoid making decisions based on names of resources (e.g. files) if those resources can have alternate names.

## Source

- [MITRE CAPEC CAPEC-78](https://capec.mitre.org/data/definitions/78.html)
