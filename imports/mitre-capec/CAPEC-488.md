---
slug: attack-pattern/CAPEC-488
title: "CAPEC-488 — HTTP Flood"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-488]
cwe_ids: [CWE-770]
mitre_ids: [T1499.002]
related: [weakness/CWE-770, technique/T1499.002]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-488
updated_at: 2026-08-31
summary: "An adversary may execute a flooding attack using the HTTP protocol with the intent to deny legitimate users access to a service by consuming resources at the application layer such as web services and their infrastructure. These attacks use legitimate session-based HTTP GET reque…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/488.html
---

# CAPEC-488: HTTP Flood

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | — |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary may execute a flooding attack using the HTTP protocol with the intent to deny legitimate users access to a service by consuming resources at the application layer such as web services and their infrastructure. These attacks use legitimate session-based HTTP GET requests designed to consume large amounts of a server's resources. Since these are legitimate sessions this attack is very difficult to detect.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-770](/wiki/p/weakness/CWE-770)

**ATT&CK techniques:** [T1499.002](/wiki/p/technique/T1499.002)

## Prerequisites

- This type of an attack requires the ability to generate a large amount of HTTP traffic to send to a target server.

## Mitigations

- Design: Use a Web Application Firewall (WAF) to help filter out malicious traffic. This can be setup with rules to block IP addresses found in IP reputation databases, which contains lists of known bad IP addresses. Analysts should also monitor when the traffic flow becomes abnormally large, and be able to add on-the-fly rules to block malicious traffic. Special care should be taken to ensure low false positive rates in block rules and functionality should be implemented to allow a legitimate user to resume sending traffic if they have been blocked.
- Hire a third party provider to implement a Web Application Firewall (WAF) for your application. Third party providers have dedicated resources and expertise that could allow them to update rules and prevent HTTP Floods very quickly.
- Design: Use a load balancer such as nginx to prevent small scale HTTP Floods by dispersing traffic between a group of servers.
- Implementation: Make a requesting machine solve some kind of challenge before allowing them to send an HTTP request. This could be a captcha or something similar that works to deter bots.

## Source

- [MITRE CAPEC CAPEC-488](https://capec.mitre.org/data/definitions/488.html)
