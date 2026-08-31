---
slug: attack-pattern/CAPEC-73
title: "CAPEC-73 — User-Controlled Filename"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-73]
cwe_ids: [CWE-20, CWE-86, CWE-96, CWE-116, CWE-184, CWE-348, CWE-350, CWE-697]
related: [weakness/CWE-20, weakness/CWE-86, weakness/CWE-96, weakness/CWE-116, weakness/CWE-184, weakness/CWE-348, weakness/CWE-350, weakness/CWE-697]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-73
updated_at: 2026-08-31
summary: "An attack of this type involves an adversary inserting malicious characters (such as a XSS redirection) into a filename, directly or indirectly that is then used by the target software to generate HTML text or other potentially executable content. Many websites rely on user-gener…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/73.html
---

# CAPEC-73: User-Controlled Filename

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An attack of this type involves an adversary inserting malicious characters (such as a XSS redirection) into a filename, directly or indirectly that is then used by the target software to generate HTML text or other potentially executable content. Many websites rely on user-generated content and dynamically build resources like files, filenames, and URL links directly from user supplied data. In this attack pattern, the attacker uploads code that can execute in the client browser and/or redirect the client browser to a site that the attacker owns. All XSS attack payload variants can be used to pass and exploit these vulnerabilities.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-20](/wiki/p/weakness/CWE-20), [CWE-86](/wiki/p/weakness/CWE-86), [CWE-96](/wiki/p/weakness/CWE-96), [CWE-116](/wiki/p/weakness/CWE-116), [CWE-184](/wiki/p/weakness/CWE-184), [CWE-348](/wiki/p/weakness/CWE-348), [CWE-350](/wiki/p/weakness/CWE-350), [CWE-697](/wiki/p/weakness/CWE-697)

## Prerequisites

- The victim must trust the name and locale of user controlled filenames.

## Skills required

- Low: To achieve a redirection and use of less trusted source, an attacker can simply edit data that the host uses to build the filename
- Medium: Deploying a malicious "look-a-like" site (such as a site masquerading as a bank or online auction site) that the user enters their authentication data into.
- High: Exploiting a client side vulnerability to inject malicious scripts into the browser's executable process.

## Consequences

- Confidentiality, Access Control, Authorization: Gain Privileges
- Confidentiality, Integrity, Availability: Execute Unauthorized Commands
- Availability: Alter Execution Logic
- Confidentiality: Read Data

## Mitigations

- Design: Use browser technologies that do not allow client side scripting.
- Implementation: Ensure all content that is delivered to client is sanitized against an acceptable content specification.
- Implementation: Perform input validation for all remote content.
- Implementation: Perform output validation for all remote content.
- Implementation: Disable scripting languages such as JavaScript in browser
- Implementation: Scan dynamically generated content against validation specification

## Source

- [MITRE CAPEC CAPEC-73](https://capec.mitre.org/data/definitions/73.html)
