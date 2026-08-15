---
slug: weakness/CWE-73
title: "CWE-73 — External Control of File Name or Path"
page_type: weakness
tags: [cwe, weakness, mitre]
cwe_ids: [CWE-73]
related: [concept/cve-anatomy]
provenance: imported
import_source: mitre-cwe
import_id: CWE-73
updated_at: 2026-08-14
summary: "The product allows user input to control or influence paths or file names that are used in filesystem operations."
sources:
  - name: MITRE CWE
    url: https://cwe.mitre.org/data/definitions/73.html
---

# CWE-73: External Control of File Name or Path

**MITRE CWE weakness**

| | |
|--|--|
| Kind | Weakness |
| Abstraction | Base |
| Status | Draft |
| Likelihood of exploit | High |

## Description

The product allows user input to control or influence paths or file names that are used in filesystem operations.

This could allow an attacker to access or modify system files or other files that are critical to the application. Path manipulation errors occur when the following two conditions are met: 1. An attacker can specify a path used in an operation on the filesystem. 2. By specifying the resource, the attacker gains a capability that would not otherwise be permitted. For example, the program may give the attacker the ability to overwrite the specified file or run with a configuration controlled by the attacker.

## Common consequences

- Integrity, Confidentiality: Read Files or Directories, Modify Files or Directories
- Integrity, Confidentiality, Availability: Modify Files or Directories, Execute Unauthorized Code or Commands
- Availability: DoS: Crash, Exit, or Restart, DoS: Resource Consumption (Other)

## Mitigations

**Architecture and Design** — When the set of filenames is limited or known, create a mapping from a set of fixed input values (such as numeric IDs) to the actual filenames, and reject all other inputs. For example, ID 1 could map to "inbox.txt" and ID 2 could map to "profile.txt". Features such as the ESAPI AccessReferenceMap provide this capability.

**Architecture and Design** — Run your code in a "jail" or similar sandbox environment that enforces strict boundaries between the process and the operating system. This may effectively restrict all access to files within a particular directory. Examples include the Unix chroot jail and AppArmor. In general, managed code may provide some protection. This may not be a feasible solution, and it only limits the impact to the operating system; the rest of your application may still be subject to compromise. Be careful to avoid CWE-243 and other weaknesses related to jails.

**Architecture and Design** — For any security checks that are performed on the client side, ensure that these checks are duplicated on the server side, in order to avoid CWE-602. Attackers can bypass the client-side checks by modifying values after the checks have been performed, or by changing the client to remove the client-side checks entirely. Then, these modified values would be submitted to the server.

**Implementation** — Assume all input is malicious. Use an "accept known good" input validation strategy, i.e., use a list of acceptable inputs that strictly conform to specifications. Reject any input that does not strictly conform to specifications, or transform it into something that does. When performing input validation, consider all potentially relevant properties, including length, type of input, the full range of acceptable values, missing or extra inputs, syntax, consistency across related fields, and conformance to business rules. As an example of business rule logic, "boat" may be syntactically valid because it only contains alphanumeric characters, but it is not valid if the input is only expected to contain colors such as "red" or "blue." Do not rely exclusively on looking for malicious or malformed inputs. This is likely to miss at least one undesirable input, especially if the code's environment changes. This can give attackers enough room to bypass the intended validation. However, denylists can be useful for detecting potential attacks or determining which inputs are so malformed that they should be rejected outright. When validating filenames, use stringent allowlists that limit the character set to be used. If feasible, only allow a single "." character in the filename to avoid weaknesses such as CWE-23, and exclude directory separators such as "/" to avoid CWE-36. Use a list of allowable file extensions, which will help to avoid CWE-434. Do not rely exclusively on a filtering mechanism that removes potentially dangerous characters. This is equivalent to a denylist, which may be incomplete (CWE-184). For example, filtering "/" is insufficient protection if the filesystem also supports the use of "\" as a directory separator. Another possible error could occur when the filtering is applied in a way that still produces dangerous data (CWE-182). For example, if "../" sequences are removed from the ".../...//" string in a sequential fashion, two instances of "../" would be removed from the original string, but the remaining characters would still form the "../" string.

**Implementation** — Use a built-in path canonicalization function (such as realpath() in C) that produces the canonical version of the pathname, which effectively removes ".." sequences and symbolic links (CWE-23, CWE-59).

## References

- CWE page: https://cwe.mitre.org/data/definitions/73.html
- CWE list: https://cwe.mitre.org/data/index.html
