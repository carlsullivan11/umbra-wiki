---
slug: attack-pattern/CAPEC-275
title: "CAPEC-275 — DNS Rebinding"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-275]
cwe_ids: [CWE-350]
related: [weakness/CWE-350]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-275
updated_at: 2026-08-31
summary: "An adversary serves content whose IP address is resolved by a DNS server that the adversary controls. After initial contact by a web browser (or similar client), the adversary changes the IP address to which its name resolves, to an address within the target organization that is …"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/275.html
---

# CAPEC-275: DNS Rebinding

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | Very High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary serves content whose IP address is resolved by a DNS server that the adversary controls. After initial contact by a web browser (or similar client), the adversary changes the IP address to which its name resolves, to an address within the target organization that is not publicly accessible. This allows the web browser to examine this internal address on behalf of the adversary.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-350](/wiki/p/weakness/CWE-350)

## Prerequisites

- The target browser must access content server from the adversary controlled DNS name. Web advertisements are often used for this purpose. The target browser must honor the TTL value returned by the adversary and re-resolve the adversary's DNS name after initial contact.

## Skills required

- Medium: Setup DNS server and the adversary's web server. Write a malicious script to allow the victim to connect to the web server.

## Consequences

- Integrity: Modify Data
- Confidentiality: Read Data
- Authorization: Execute Unauthorized Commands
- Accountability, Authentication, Authorization, Non-Repudiation: Gain Privileges
- Access Control, Authorization: Bypass Protection Mechanism

## Mitigations

- Design: IP Pinning causes browsers to record the IP address to which a given name resolves and continue using this address regardless of the TTL set in the DNS response. Unfortunately, this is incompatible with the design of some legitimate sites.
- Implementation: Reject HTTP request with a malicious Host header.
- Implementation: Employ DNS resolvers that prevent external names from resolving to internal addresses.

## Source

- [MITRE CAPEC CAPEC-275](https://capec.mitre.org/data/definitions/275.html)
