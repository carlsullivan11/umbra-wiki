---
slug: attack-pattern/CAPEC-95
title: "CAPEC-95 — WSDL Scanning"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-95]
cwe_ids: [CWE-538]
related: [weakness/CWE-538]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-95
updated_at: 2026-08-31
summary: "This attack targets the WSDL interface made available by a web service. The attacker may scan the WSDL interface to reveal sensitive information about invocation patterns, underlying technology implementations and associated vulnerabilities. This type of probing is carried out to…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/95.html
---

# CAPEC-95: WSDL Scanning

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

This attack targets the WSDL interface made available by a web service. The attacker may scan the WSDL interface to reveal sensitive information about invocation patterns, underlying technology implementations and associated vulnerabilities. This type of probing is carried out to perform more serious attacks (e.g. parameter tampering, malicious content injection, command injection, etc.). WSDL files provide detailed information about the services ports and bindings available to consumers. For instance, the attacker can submit special characters or malicious content to the Web service and can cause a denial of service condition or illegal access to database records. In addition, the attacker may try to guess other private methods by using the information provided in the WSDL files.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-538](/wiki/p/weakness/CWE-538)

## Prerequisites

- A client program connecting to a web service can read the WSDL to determine what functions are available on the server.
- The target host exposes vulnerable functions within its WSDL interface.

## Skills required

- Low: This attack can be as simple as reading WSDL and starting sending invalid request.
- Medium: This attack can be used to perform more sophisticated attacks (SQL injection, etc.)

## Consequences

- Confidentiality: Read Data

## Mitigations

- It is important to protect WSDL file or provide limited access to it.
- Review the functions exposed by the WSDL interface (especially if you have used a tool to generate it). Make sure that none of them is vulnerable to injection.
- Ensure the WSDL does not expose functions and APIs that were not intended to be exposed.
- Pay attention to the function naming convention (within the WSDL interface). Easy to guess function name may be an entry point for attack.
- Validate the received messages against the WSDL Schema. Incomplete solution.

## Source

- [MITRE CAPEC CAPEC-95](https://capec.mitre.org/data/definitions/95.html)
