---
slug: attack-pattern/CAPEC-79
title: "CAPEC-79 — Using Slashes in Alternate Encoding"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-79]
cwe_ids: [CWE-20, CWE-22, CWE-73, CWE-74, CWE-173, CWE-180, CWE-181, CWE-185, CWE-200, CWE-697, CWE-707]
related: [weakness/CWE-20, weakness/CWE-22, weakness/CWE-73, weakness/CWE-74, weakness/CWE-173, weakness/CWE-180, weakness/CWE-181, weakness/CWE-185, weakness/CWE-200, weakness/CWE-697, weakness/CWE-707]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-79
updated_at: 2026-08-31
summary: "This attack targets the encoding of the Slash characters. An adversary would try to exploit common filtering problems related to the use of the slashes characters to gain access to resources on the target host. Directory-driven systems, such as file systems and databases, typical…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/79.html
---

# CAPEC-79: Using Slashes in Alternate Encoding

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

This attack targets the encoding of the Slash characters. An adversary would try to exploit common filtering problems related to the use of the slashes characters to gain access to resources on the target host. Directory-driven systems, such as file systems and databases, typically use the slash character to indicate traversal between directories or other container components. For murky historical reasons, PCs (and, as a result, Microsoft OSs) choose to use a backslash, whereas the UNIX world typically makes use of the forward slash. The schizophrenic result is that many MS-based systems are required to understand both forms of the slash. This gives the adversary many opportunities to discover and abuse a number of common filtering problems. The goal of this pattern is to discover server software that only applies filters to one version, but not the other.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-20](/wiki/p/weakness/CWE-20), [CWE-22](/wiki/p/weakness/CWE-22), [CWE-73](/wiki/p/weakness/CWE-73), [CWE-74](/wiki/p/weakness/CWE-74), [CWE-173](/wiki/p/weakness/CWE-173), [CWE-180](/wiki/p/weakness/CWE-180), [CWE-181](/wiki/p/weakness/CWE-181), [CWE-185](/wiki/p/weakness/CWE-185), [CWE-200](/wiki/p/weakness/CWE-200), [CWE-697](/wiki/p/weakness/CWE-697), [CWE-707](/wiki/p/weakness/CWE-707)

## Prerequisites

- The application server accepts paths to locate resources.
- The application server does insufficient input data validation on the resource path requested by the user.
- The access right to resources are not set properly.

## Skills required

- Low: An adversary can try variation of the slashes characters.
- Medium: An adversary can use more sophisticated tool or script to scan a website and find a path filtering problem.

## Consequences

- Confidentiality: Read Data
- Confidentiality, Integrity, Availability: Execute Unauthorized Commands
- Confidentiality, Access Control, Authorization: Gain Privileges

## Mitigations

- Any security checks should occur after the data has been decoded and validated as correct data format. Do not repeat decoding process, if bad character are left after decoding process, treat the data as suspicious, and fail the validation process. Refer to the RFCs to safely decode URL.
- When client input is required from web-based forms, avoid using the "GET" method to submit data, as the method causes the form data to be appended to the URL and is easily manipulated. Instead, use the "POST method whenever possible.
- There are tools to scan HTTP requests to the server for valid URL such as URLScan from Microsoft (http://www.microsoft.com/technet/security/tools/urlscan.mspx)
- Be aware of the threat of alternative method of data encoding and obfuscation technique such as IP address encoding. (See related guideline section)
- Test your path decoding process against malicious input.
- In the case of path traversals, use the principle of least privilege when determining access rights to file systems. Do not allow users to access directories/files that they should not access.
- Assume all input is malicious. Create an allowlist that defines all valid input to the application based on the requirements specifications. Input that does not match against the allowlist should not be permitted to enter into the system.

## Source

- [MITRE CAPEC CAPEC-79](https://capec.mitre.org/data/definitions/79.html)
