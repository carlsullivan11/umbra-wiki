---
slug: weakness/CWE-23
title: "CWE-23 — Relative Path Traversal"
page_type: weakness
tags: [cwe, weakness, mitre]
cwe_ids: [CWE-23]
related: [concept/cve-anatomy]
provenance: imported
import_source: mitre-cwe
import_id: CWE-23
updated_at: 2026-08-14
summary: "The product uses external input to construct a pathname that should be within a restricted directory, but it does not properly neutralize sequences such as '..' that can resolve to a location that is "
sources:
  - name: MITRE CWE
    url: https://cwe.mitre.org/data/definitions/23.html
---

# CWE-23: Relative Path Traversal

**MITRE CWE weakness**

| | |
|--|--|
| Kind | Weakness |
| Abstraction | Base |
| Status | Draft |
| Likelihood of exploit | — |

## Description

The product uses external input to construct a pathname that should be within a restricted directory, but it does not properly neutralize sequences such as ".." that can resolve to a location that is outside of that directory.



## Common consequences

- Integrity, Confidentiality, Availability: Execute Unauthorized Code or Commands
- Integrity: Modify Files or Directories
- Confidentiality: Read Files or Directories
- Availability: DoS: Crash, Exit, or Restart

## Mitigations

**Implementation** — Assume all input is malicious. Use an "accept known good" input validation strategy, i.e., use a list of acceptable inputs that strictly conform to specifications. Reject any input that does not strictly conform to specifications, or transform it into something that does. When performing input validation, consider all potentially relevant properties, including length, type of input, the full range of acceptable values, missing or extra inputs, syntax, consistency across related fields, and conformance to business rules. As an example of business rule logic, "boat" may be syntactically valid because it only contains alphanumeric characters, but it is not valid if the input is only expected to contain colors such as "red" or "blue." Do not rely exclusively on looking for malicious or malformed inputs. This is likely to miss at least one undesirable input, especially if the code's environment changes. This can give attackers enough room to bypass the intended validation. However, denylists can be useful for detecting potential attacks or determining which inputs are so malformed that they should be rejected outright. When validating filenames, use stringent allowlists that limit the character set to be used. If feasible, only allow a single "." character in the filename to avoid weaknesses such as CWE-23, and exclude directory separators such as "/" to avoid CWE-36. Use a list of allowable file extensions, which will help to avoid CWE-434. Do not rely exclusively on a filtering mechanism that removes potentially dangerous characters. This is equivalent to a denylist, which may be incomplete (CWE-184). For example, filtering "/" is insufficient protection if the filesystem also supports the use of "\" as a directory separator. Another possible error could occur when the filtering is applied in a way that still produces dangerous data (CWE-182). For example, if "../" sequences are removed from the ".../...//" string in a sequential fashion, two instances of "../" would be removed from the original string, but the remaining characters would still form the "../" string.

**Implementation** — Inputs should be decoded and canonicalized to the application's current internal representation before being validated (CWE-180). Make sure that the application does not decode the same input twice (CWE-174). Such errors could be used to bypass allowlist validation schemes by introducing dangerous inputs after they have been checked. Use a built-in path canonicalization function (such as realpath() in C) that produces the canonical version of the pathname, which effectively removes ".." sequences and symbolic links (CWE-23, CWE-59). This includes: realpath() in C getCanonicalPath() in Java GetFullPath() in ASP.NET realpath() or abs_path() in Perl realpath() in PHP

**Operation** — Use an application firewall that can detect attacks against this weakness. It can be beneficial in cases in which the code cannot be fixed (because it is controlled by a third party), as an emergency prevention measure while more comprehensive software assurance measures are applied, or to provide defense in depth [REF-1481].

## References

- CWE page: https://cwe.mitre.org/data/definitions/23.html
- CWE list: https://cwe.mitre.org/data/index.html
