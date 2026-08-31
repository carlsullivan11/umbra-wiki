---
slug: attack-pattern/CAPEC-105
title: "CAPEC-105 — HTTP Request Splitting"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-105]
cwe_ids: [CWE-74, CWE-113, CWE-138, CWE-436]
related: [weakness/CWE-74, weakness/CWE-113, weakness/CWE-138, weakness/CWE-436]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-105
updated_at: 2026-08-31
summary: "An adversary abuses the flexibility and discrepancies in the parsing and interpretation of HTTP Request messages by different intermediary HTTP agents (e.g., load balancer, reverse proxy, web caching proxies, application firewalls, etc.) to split a single HTTP request into multip…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/105.html
---

# CAPEC-105: HTTP Request Splitting

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | High |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary abuses the flexibility and discrepancies in the parsing and interpretation of HTTP Request messages by different intermediary HTTP agents (e.g., load balancer, reverse proxy, web caching proxies, application firewalls, etc.) to split a single HTTP request into multiple unauthorized and malicious HTTP requests to a back-end HTTP agent (e.g., web server). See CanPrecede relationships for possible consequences.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-74](/wiki/p/weakness/CWE-74), [CWE-113](/wiki/p/weakness/CWE-113), [CWE-138](/wiki/p/weakness/CWE-138), [CWE-436](/wiki/p/weakness/CWE-436)

## Prerequisites

- An additional intermediary HTTP agent such as an application firewall or a web caching proxy between the adversary and the second agent such as a web server, that sends multiple HTTP messages over same network connection.
- Differences in the way the two HTTP agents parse and interpret HTTP requests and its headers.
- HTTP headers capable of being user-manipulated.
- HTTP agents running on HTTP/1.0 or HTTP/1.1 that allow for Keep Alive mode, Pipelined queries, and Chunked queries and responses.

## Skills required

- Medium: Detailed knowledge on HTTP protocol: request and response messages structure and usage of specific headers.
- Medium: Detailed knowledge on how specific HTTP agents receive, send, process, interpret, and parse a variety of HTTP messages and headers.
- Medium: Possess knowledge on the exact details in the discrepancies between several targeted HTTP agents in path of an HTTP message in parsing its message structure and individual headers.

## Consequences

- Confidentiality, Integrity, Availability: Execute Unauthorized Commands
- Confidentiality, Access Control, Authorization: Gain Privileges
- Confidentiality: Read Data
- Integrity: Modify Data

## Mitigations

- Design: evaluate HTTP agents prior to deployment for parsing/interpretation discrepancies.
- Configuration: front-end HTTP agents notice ambiguous requests.
- Configuration: back-end HTTP agents reject ambiguous requests and close the network connection.
- Configuration: Disable reuse of back-end connections.
- Configuration: Use HTTP/2 for back-end connections.
- Configuration: Use the same web server software for front-end and back-end server.
- Implementation: Utilize a Web Application Firewall (WAF) that has built-in mitigation to detect abnormal requests/responses.
- Configuration: Install latest vendor security patches available for both intermediary and back-end HTTP infrastructure (i.e. proxies and web servers)

## Source

- [MITRE CAPEC CAPEC-105](https://capec.mitre.org/data/definitions/105.html)
