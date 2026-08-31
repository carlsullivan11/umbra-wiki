---
slug: attack-pattern/CAPEC-36
title: "CAPEC-36 — Using Unpublished Interfaces or Functionality"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-36]
cwe_ids: [CWE-306, CWE-693, CWE-695, CWE-1242]
related: [weakness/CWE-306, weakness/CWE-693, weakness/CWE-695, weakness/CWE-1242]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-36
updated_at: 2026-08-31
summary: "An adversary searches for and invokes interfaces or functionality that the target system designers did not intend to be publicly available. If interfaces fail to authenticate requests, the attacker may be able to invoke functionality they are not authorized for."
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/36.html
---

# CAPEC-36: Using Unpublished Interfaces or Functionality

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary searches for and invokes interfaces or functionality that the target system designers did not intend to be publicly available. If interfaces fail to authenticate requests, the attacker may be able to invoke functionality they are not authorized for.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-306](/wiki/p/weakness/CWE-306), [CWE-693](/wiki/p/weakness/CWE-693), [CWE-695](/wiki/p/weakness/CWE-695), [CWE-1242](/wiki/p/weakness/CWE-1242)

## Prerequisites

- The architecture under attack must publish or otherwise make available services that clients can attach to, either in an unauthenticated fashion, or having obtained an authentication token elsewhere. The service need not be 'discoverable', but in the event it isn't it must have some way of being discovered by an attacker. This might include listening on a well-known port. Ultimately, the likelihood of exploit depends on discoverability of the vulnerable service.

## Skills required

- Low: A number of web service digging tools are available for free that help discover exposed web services and their interfaces. In the event that a web service is not listed, the attacker does not need to know much more in addition to the format of web service messages that they can sniff/monitor for.

## Consequences

- Confidentiality: Read Data
- Confidentiality, Access Control, Authorization: Gain Privileges

## Mitigations

- Authenticating both services and their discovery, and protecting that authentication mechanism simply fixes the bulk of this problem. Protecting the authentication involves the standard means, including: 1) protecting the channel over which authentication occurs, 2) preventing the theft, forgery, or prediction of authentication credentials or the resultant tokens, or 3) subversion of password reset and the like.

## Source

- [MITRE CAPEC CAPEC-36](https://capec.mitre.org/data/definitions/36.html)
