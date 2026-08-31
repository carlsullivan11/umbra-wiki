---
slug: attack-pattern/CAPEC-588
title: "CAPEC-588 — DOM-Based XSS"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-588]
cwe_ids: [CWE-20, CWE-79, CWE-83]
related: [weakness/CWE-20, weakness/CWE-79, weakness/CWE-83]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-588
updated_at: 2026-08-31
summary: "This type of attack is a form of Cross-Site Scripting (XSS) where a malicious script is inserted into the client-side HTML being parsed by a web browser. Content served by a vulnerable web application includes script code used to manipulate the Document Object Model (DOM). This s…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/588.html
---

# CAPEC-588: DOM-Based XSS

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Very High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

This type of attack is a form of Cross-Site Scripting (XSS) where a malicious script is inserted into the client-side HTML being parsed by a web browser. Content served by a vulnerable web application includes script code used to manipulate the Document Object Model (DOM). This script code either does not properly validate input, or does not perform proper output encoding, thus creating an opportunity for an adversary to inject a malicious script launch a XSS attack. A key distinction between other XSS attacks and DOM-based attacks is that in other XSS attacks, the malicious script runs when the vulnerable web page is initially loaded, while a DOM-based attack executes sometime after the page loads. Another distinction of DOM-based attacks is that in some cases, the malicious script is never sent to the vulnerable web server at all. An attack like this is guaranteed to bypass any server-side filtering attempts to protect users.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-20](/wiki/p/weakness/CWE-20), [CWE-79](/wiki/p/weakness/CWE-79), [CWE-83](/wiki/p/weakness/CWE-83)

## Prerequisites

- An application that leverages a client-side web browser with scripting enabled.
- An application that manipulates the DOM via client-side scripting.
- An application that failS to adequately sanitize or encode untrusted input.

## Skills required

- Medium: Requires the ability to write scripts of some complexity and to inject it through user controlled fields in the system.

## Consequences

- Confidentiality: Read Data
- Confidentiality, Authorization, Access Control: Gain Privileges
- Confidentiality, Integrity, Availability: Execute Unauthorized Commands
- Integrity: Modify Data

## Mitigations

- Use browser technologies that do not allow client-side scripting.
- Utilize proper character encoding for all output produced within client-site scripts manipulating the DOM.
- Ensure that all user-supplied input is validated before use.

## Source

- [MITRE CAPEC CAPEC-588](https://capec.mitre.org/data/definitions/588.html)
