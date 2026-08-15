---
slug: weakness/CWE-69
title: "CWE-69 — Improper Handling of Windows ::DATA Alternate Data Stream"
page_type: weakness
tags: [cwe, weakness, mitre]
cwe_ids: [CWE-69]
related: [concept/cve-anatomy]
provenance: imported
import_source: mitre-cwe
import_id: CWE-69
updated_at: 2026-08-14
summary: "The product does not properly prevent access to, or detect usage of, alternate data streams (ADS)."
sources:
  - name: MITRE CWE
    url: https://cwe.mitre.org/data/definitions/69.html
---

# CWE-69: Improper Handling of Windows ::DATA Alternate Data Stream

**MITRE CWE weakness**

| | |
|--|--|
| Kind | Weakness |
| Abstraction | Variant |
| Status | Incomplete |
| Likelihood of exploit | — |

## Description

The product does not properly prevent access to, or detect usage of, alternate data streams (ADS).

An attacker can use an ADS to hide information about a file (e.g. size, the name of the process) from a system or file browser tools such as Windows Explorer and 'dir' at the command line utility. Alternately, the attacker might be able to bypass intended access restrictions for the associated data fork.

## Common consequences

- Access Control, Non-Repudiation, Other: Bypass Protection Mechanism, Hide Activities, Other

## Mitigations

**Implementation** — Ensure that the source code correctly parses the filename to read or write to the correct stream.

## References

- CWE page: https://cwe.mitre.org/data/definitions/69.html
- CWE list: https://cwe.mitre.org/data/index.html
