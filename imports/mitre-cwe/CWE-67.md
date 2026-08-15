---
slug: weakness/CWE-67
title: "CWE-67 — Improper Handling of Windows Device Names"
page_type: weakness
tags: [cwe, weakness, mitre]
cwe_ids: [CWE-67]
related: [concept/cve-anatomy]
provenance: imported
import_source: mitre-cwe
import_id: CWE-67
updated_at: 2026-08-14
summary: "The product constructs pathnames from user input, but it does not handle or incorrectly handles a pathname containing a Windows device name such as AUX or CON. This typically leads to denial of servic"
sources:
  - name: MITRE CWE
    url: https://cwe.mitre.org/data/definitions/67.html
---

# CWE-67: Improper Handling of Windows Device Names

**MITRE CWE weakness**

| | |
|--|--|
| Kind | Weakness |
| Abstraction | Variant |
| Status | Incomplete |
| Likelihood of exploit | High |

## Description

The product constructs pathnames from user input, but it does not handle or incorrectly handles a pathname containing a Windows device name such as AUX or CON. This typically leads to denial of service or an information exposure when the application attempts to process the pathname as a regular file.

Not properly handling virtual filenames (e.g. AUX, CON, PRN, COM1, LPT1) can result in different types of vulnerabilities. In some cases an attacker can request a device via injection of a virtual filename in a URL, which may cause an error that leads to a denial of service or an error page that reveals sensitive information. A product that allows device names to bypass filtering runs the risk of an attacker injecting malicious code in a file with the name of a device.

## Common consequences

- Availability, Confidentiality, Other: DoS: Crash, Exit, or Restart, Read Application Data, Other

## Mitigations

**Implementation** — Be familiar with the device names in the operating system where your system is deployed. Check input for these device names.

## References

- CWE page: https://cwe.mitre.org/data/definitions/67.html
- CWE list: https://cwe.mitre.org/data/index.html
