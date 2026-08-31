---
slug: attack-pattern/CAPEC-465
title: "CAPEC-465 — Transparent Proxy Abuse"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-465]
cwe_ids: [CWE-441]
mitre_ids: [T1090.001]
related: [weakness/CWE-441, technique/T1090.001]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-465
updated_at: 2026-08-31
summary: "A transparent proxy serves as an intermediate between the client and the internet at large. It intercepts all requests originating from the client and forwards them to the correct location. The proxy also intercepts all responses to the client and forwards these to the client. Al…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/465.html
---

# CAPEC-465: Transparent Proxy Abuse

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Medium |
| Likelihood of attack | — |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

A transparent proxy serves as an intermediate between the client and the internet at large. It intercepts all requests originating from the client and forwards them to the correct location. The proxy also intercepts all responses to the client and forwards these to the client. All of this is done in a manner transparent to the client.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-441](/wiki/p/weakness/CWE-441)

**ATT&CK techniques:** [T1090.001](/wiki/p/technique/T1090.001)

## Prerequisites

- Transparent proxy is usedVulnerable configuration of network topology involving the transparent proxy (e.g., no NAT happening between the client and the proxy)Execution of malicious Flash or Applet in the victim's browser

## Skills required

- Medium: Creating malicious Flash or Applet to open a cross-domain socket connection to a remote system

## Mitigations

- Design: Ensure that the transparent proxy uses an actual network layer IP address for routing requests. On the transparent proxy, disable the use of routing based on address information in the HTTP host header.
- Configuration: Disable in the browser the execution of Java Script, Flash, SilverLight, etc.

## Source

- [MITRE CAPEC CAPEC-465](https://capec.mitre.org/data/definitions/465.html)
