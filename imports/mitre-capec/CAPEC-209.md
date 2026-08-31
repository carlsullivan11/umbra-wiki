---
slug: attack-pattern/CAPEC-209
title: "CAPEC-209 — XSS Using MIME Type Mismatch"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-209]
cwe_ids: [CWE-20, CWE-79, CWE-646]
related: [weakness/CWE-20, weakness/CWE-79, weakness/CWE-646]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-209
updated_at: 2026-08-31
summary: "An adversary creates a file with scripting content but where the specified MIME type of the file is such that scripting is not expected. The adversary tricks the victim into accessing a URL that responds with the script file. Some browsers will detect that the specified MIME type…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/209.html
---

# CAPEC-209: XSS Using MIME Type Mismatch

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary creates a file with scripting content but where the specified MIME type of the file is such that scripting is not expected. The adversary tricks the victim into accessing a URL that responds with the script file. Some browsers will detect that the specified MIME type of the file does not match the actual type of its content and will automatically switch to using an interpreter for the real content type. If the browser does not invoke script filters before doing this, the adversary's script may run on the target unsanitized, possibly revealing the victim's cookies or executing arbitrary script in their browser.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-20](/wiki/p/weakness/CWE-20), [CWE-79](/wiki/p/weakness/CWE-79), [CWE-646](/wiki/p/weakness/CWE-646)

## Prerequisites

- The victim must follow a crafted link that references a scripting file that is mis-typed as a non-executable file.
- The victim's browser must detect the true type of a mis-labeled scripting file and invoke the appropriate script interpreter without first performing filtering on the content.

## Source

- [MITRE CAPEC CAPEC-209](https://capec.mitre.org/data/definitions/209.html)
