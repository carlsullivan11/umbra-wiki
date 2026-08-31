---
slug: attack-pattern/CAPEC-86
title: "CAPEC-86 — XSS Through HTTP Headers"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-86]
cwe_ids: [CWE-80]
related: [weakness/CWE-80]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-86
updated_at: 2026-08-31
summary: "An adversary exploits web applications that generate web content, such as links in a HTML page, based on unvalidated or improperly validated data submitted by other actors. XSS in HTTP Headers attacks target the HTTP headers which are hidden from most users and may not be validat…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/86.html
---

# CAPEC-86: XSS Through HTTP Headers

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Very High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary exploits web applications that generate web content, such as links in a HTML page, based on unvalidated or improperly validated data submitted by other actors. XSS in HTTP Headers attacks target the HTTP headers which are hidden from most users and may not be validated by web applications.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-80](/wiki/p/weakness/CWE-80)

## Prerequisites

- Target software must be a client that allows scripting communication from remote hosts.

## Skills required

- Low: To achieve a redirection and use of less trusted source, an adversary can simply edit HTTP Headers that are sent to client machine.
- High: Exploiting a client side vulnerability to inject malicious scripts into the browser's executable process.

## Consequences

- Confidentiality, Integrity, Availability: Execute Unauthorized Commands
- Confidentiality: Read Data
- Confidentiality, Access Control, Authorization: Gain Privileges

## Mitigations

- Design: Use browser technologies that do not allow client side scripting.
- Design: Utilize strict type, character, and encoding enforcement
- Design: Server side developers should not proxy content via XHR or other means, if a http proxy for remote content is setup on the server side, the client's browser has no way of discerning where the data is originating from.
- Implementation: Ensure all content that is delivered to client is sanitized against an acceptable content specification.
- Implementation: Perform input validation for all remote content.
- Implementation: Perform output validation for all remote content.
- Implementation: Disable scripting languages such as JavaScript in browser
- Implementation: Session tokens for specific host

## Source

- [MITRE CAPEC CAPEC-86](https://capec.mitre.org/data/definitions/86.html)
