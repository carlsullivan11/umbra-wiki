---
slug: attack-pattern/CAPEC-183
title: "CAPEC-183 — IMAP/SMTP Command Injection"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-183]
cwe_ids: [CWE-77]
related: [weakness/CWE-77]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-183
updated_at: 2026-08-31
summary: "An adversary exploits weaknesses in input validation on web-mail servers to execute commands on the IMAP/SMTP server. Web-mail servers often sit between the Internet and the IMAP or SMTP mail server. User requests are received by the web-mail servers which then query the back-end…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/183.html
---

# CAPEC-183: IMAP/SMTP Command Injection

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary exploits weaknesses in input validation on web-mail servers to execute commands on the IMAP/SMTP server. Web-mail servers often sit between the Internet and the IMAP or SMTP mail server. User requests are received by the web-mail servers which then query the back-end mail server for the requested information and return this response to the user. In an IMAP/SMTP command injection attack, mail-server commands are embedded in parts of the request sent to the web-mail server. If the web-mail server fails to adequately sanitize these requests, these commands are then sent to the back-end mail server when it is queried by the web-mail server, where the commands are then executed. This attack can be especially dangerous since administrators may assume that the back-end server is protected against direct Internet access and therefore may not secure it adequately against the execution of malicious commands.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-77](/wiki/p/weakness/CWE-77)

## Prerequisites

- The target environment must consist of a web-mail server that the attacker can query and a back-end mail server. The back-end mail server need not be directly accessible to the attacker.
- The web-mail server must fail to adequately sanitize fields received from users and passed on to the back-end mail server.
- The back-end mail server must not be adequately secured against receiving malicious commands from the web-mail server.

## Source

- [MITRE CAPEC CAPEC-183](https://capec.mitre.org/data/definitions/183.html)
