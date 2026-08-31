---
slug: attack-pattern/CAPEC-53
title: "CAPEC-53 — Postfix, Null Terminate, and Backslash"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-53]
cwe_ids: [CWE-20, CWE-74, CWE-158, CWE-172, CWE-173, CWE-697, CWE-707]
related: [weakness/CWE-20, weakness/CWE-74, weakness/CWE-158, weakness/CWE-172, weakness/CWE-173, weakness/CWE-697, weakness/CWE-707]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-53
updated_at: 2026-08-31
summary: "If a string is passed through a filter of some kind, then a terminal NULL may not be valid. Using alternate representation of NULL allows an adversary to embed the NULL mid-string while postfixing the proper data so that the filter is avoided. One example is a filter that looks f…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/53.html
---

# CAPEC-53: Postfix, Null Terminate, and Backslash

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

If a string is passed through a filter of some kind, then a terminal NULL may not be valid. Using alternate representation of NULL allows an adversary to embed the NULL mid-string while postfixing the proper data so that the filter is avoided. One example is a filter that looks for a trailing slash character. If a string insertion is possible, but the slash must exist, an alternate encoding of NULL in mid-string may be used.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-20](/wiki/p/weakness/CWE-20), [CWE-74](/wiki/p/weakness/CWE-74), [CWE-158](/wiki/p/weakness/CWE-158), [CWE-172](/wiki/p/weakness/CWE-172), [CWE-173](/wiki/p/weakness/CWE-173), [CWE-697](/wiki/p/weakness/CWE-697), [CWE-707](/wiki/p/weakness/CWE-707)

## Prerequisites

- Null terminators are not properly handled by the filter.

## Skills required

- Medium: An adversary needs to understand alternate encodings, what the filter looks for and the data format acceptable to the target API

## Consequences

- Integrity: Modify Data
- Confidentiality: Read Data
- Confidentiality, Access Control, Authorization: Gain Privileges

## Mitigations

- Properly handle Null characters. Make sure canonicalization is properly applied. Do not pass Null characters to the underlying APIs.
- Assume all input is malicious. Create an allowlist that defines all valid input to the software system based on the requirements specifications. Input that does not match against the allowlist should not be permitted to enter into the system.

## Source

- [MITRE CAPEC CAPEC-53](https://capec.mitre.org/data/definitions/53.html)
