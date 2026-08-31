---
slug: attack-pattern/CAPEC-142
title: "CAPEC-142 — DNS Cache Poisoning"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-142]
cwe_ids: [CWE-345, CWE-346, CWE-348, CWE-349, CWE-350]
mitre_ids: [T1584.002]
related: [weakness/CWE-345, weakness/CWE-346, weakness/CWE-348, weakness/CWE-349, weakness/CWE-350, technique/T1584.002]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-142
updated_at: 2026-08-31
summary: "A domain name server translates a domain name (such as www.example.com) into an IP address that Internet hosts use to contact Internet resources. An adversary modifies a public DNS cache to cause certain names to resolve to incorrect addresses that the adversary specifies. The re…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/142.html
---

# CAPEC-142: DNS Cache Poisoning

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Draft |
| Typical severity | High |
| Likelihood of attack | High |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

A domain name server translates a domain name (such as www.example.com) into an IP address that Internet hosts use to contact Internet resources. An adversary modifies a public DNS cache to cause certain names to resolve to incorrect addresses that the adversary specifies. The result is that client applications that rely upon the targeted cache for domain name resolution will be directed not to the actual address of the specified domain name but to some other address. Adversaries can use this to herd clients to sites that install malware on the victim's computer or to masquerade as part of a Pharming attack.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-345](/wiki/p/weakness/CWE-345), [CWE-346](/wiki/p/weakness/CWE-346), [CWE-348](/wiki/p/weakness/CWE-348), [CWE-349](/wiki/p/weakness/CWE-349), [CWE-350](/wiki/p/weakness/CWE-350)

**ATT&CK techniques:** [T1584.002](/wiki/p/technique/T1584.002)

## Prerequisites

- A DNS cache must be vulnerable to some attack that allows the adversary to replace addresses in its lookup table.Client applications must trust the corrupted cashed values and utilize them for their domain name resolutions.

## Skills required

- Medium: To overwrite/modify targeted DNS cache

## Mitigations

- Configuration: Make sure your DNS servers have been updated to the latest versions
- Configuration: UNIX services like rlogin, rsh/rcp, xhost, and nfs are all susceptible to wrong information being held in a cache. Care should be taken with these services so they do not rely upon DNS caches that have been exposed to the Internet.
- Configuration: Disable client side DNS caching.

## Source

- [MITRE CAPEC CAPEC-142](https://capec.mitre.org/data/definitions/142.html)
