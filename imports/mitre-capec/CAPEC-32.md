---
slug: attack-pattern/CAPEC-32
title: "CAPEC-32 — XSS Through HTTP Query Strings"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-32]
cwe_ids: [CWE-80]
related: [weakness/CWE-80]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-32
updated_at: 2026-08-31
summary: "An adversary embeds malicious script code in the parameters of an HTTP query string and convinces a victim to submit the HTTP request that contains the query string to a vulnerable web application. The web application then procedes to use the values parameters without properly va…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/32.html
---

# CAPEC-32: XSS Through HTTP Query Strings

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary embeds malicious script code in the parameters of an HTTP query string and convinces a victim to submit the HTTP request that contains the query string to a vulnerable web application. The web application then procedes to use the values parameters without properly validation them first and generates the HTML code that will be executed by the victim's browser.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-80](/wiki/p/weakness/CWE-80)

## Prerequisites

- Target client software must allow scripting such as JavaScript. Server software must allow display of remote generated HTML without sufficient input or output validation.

## Skills required

- Low: To place malicious payload on server via HTTP
- High: Exploiting any information gathered by HTTP Query on script host

## Consequences

- Confidentiality: Read Data
- Confidentiality, Integrity, Availability: Execute Unauthorized Commands

## Mitigations

- Design: Use browser technologies that do not allow client side scripting.
- Design: Utilize strict type, character, and encoding enforcement
- Design: Server side developers should not proxy content via XHR or other means, if a http proxy for remote content is setup on the server side, the client's browser has no way of discerning where the data is originating from.
- Implementation: Ensure all content that is delivered to client is sanitized against an acceptable content specification.
- Implementation: Perform input validation for all remote content, including remote and user-generated content
- Implementation: Perform output validation for all remote content.
- Implementation: Disable scripting languages such as JavaScript in browser
- Implementation: Session tokens for specific host

## Source

- [MITRE CAPEC CAPEC-32](https://capec.mitre.org/data/definitions/32.html)
