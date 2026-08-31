---
slug: attack-pattern/CAPEC-273
title: "CAPEC-273 — HTTP Response Smuggling"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-273]
cwe_ids: [CWE-74, CWE-436, CWE-444]
related: [weakness/CWE-74, weakness/CWE-436, weakness/CWE-444]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-273
updated_at: 2026-08-31
summary: "An adversary manipulates and injects malicious content in the form of secret unauthorized HTTP responses, into a single HTTP response from a vulnerable or compromised back-end HTTP agent (e.g., server). See CanPrecede relationships for possible consequences."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/273.html
---

# CAPEC-273: HTTP Response Smuggling

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | High |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary manipulates and injects malicious content in the form of secret unauthorized HTTP responses, into a single HTTP response from a vulnerable or compromised back-end HTTP agent (e.g., server). See CanPrecede relationships for possible consequences.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-74](/wiki/p/weakness/CWE-74), [CWE-436](/wiki/p/weakness/CWE-436), [CWE-444](/wiki/p/weakness/CWE-444)

## Prerequisites

- A vulnerable or compromised server or domain/site capable of allowing adversary to insert/inject malicious content that will appear in the server's response to target HTTP agents (e.g., proxies and users' web browsers).
- Differences in the way the two HTTP agents parse and interpret HTTP responses and its headers.
- HTTP agents running on HTTP/1.1 that allow for Keep Alive mode, Pipelined queries, and Chunked queries and responses.

## Skills required

- Medium: Detailed knowledge on HTTP protocol: request and response messages structure and usage of specific headers.
- Medium: Detailed knowledge on how specific HTTP agents receive, send, process, interpret, and parse a variety of HTTP messages and headers.
- Medium: Possess knowledge on the exact details in the discrepancies between several targeted HTTP agents in path of an HTTP message in parsing its message structure and individual headers.

## Consequences

- Confidentiality, Integrity, Availability: Execute Unauthorized Commands
- Confidentiality, Access Control, Authorization: Gain Privileges
- Integrity: Modify Data

## Mitigations

- Design: evaluate HTTP agents prior to deployment for parsing/interpretation discrepancies.
- Configuration: front-end HTTP agents notice ambiguous requests.
- Configuration: back-end HTTP agents reject ambiguous requests and close the network connection.
- Configuration: Disable reuse of back-end connections.
- Configuration: Use HTTP/2 for back-end connections.
- Configuration: Use the same web server software for front-end and back-end server.
- Implementation: Utilize a Web Application Firewall (WAF) that has built-in mitigation to detect abnormal requests/responses.
- Configuration: Prioritize Transfer-Encoding header over Content-Length, whenever an HTTP message contains both.

## Source

- [MITRE CAPEC CAPEC-273](https://capec.mitre.org/data/definitions/273.html)
