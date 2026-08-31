---
slug: attack-pattern/CAPEC-148
title: "CAPEC-148 — Content Spoofing"
page_type: attack-pattern
tags: [capec, attack-pattern, mitre]
capec_ids: [CAPEC-148]
cwe_ids: [CWE-345]
mitre_ids: [T1491]
related: [weakness/CWE-345, technique/T1491]
provenance: imported
import_source: mitre-capec
import_id: CAPEC-148
updated_at: 2026-08-31
summary: "An adversary modifies content to make it contain something other than what the original content producer intended while keeping the apparent source of the content unchanged. The term content spoofing is most often used to describe modification of web pages hosted by a target to d…"
sources:
  - name: MITRE CAPEC
    url: https://capec.mitre.org/data/definitions/148.html
---

# CAPEC-148: Content Spoofing

**MITRE CAPEC attack pattern**

| | |
|--|--|
| Status | Stable |
| Typical severity | Medium |
| Likelihood of attack | Medium |
| Catalogue | CAPEC 3.9 (2023-01-24) |

## Description

An adversary modifies content to make it contain something other than what the original content producer intended while keeping the apparent source of the content unchanged. The term content spoofing is most often used to describe modification of web pages hosted by a target to display the adversary's content instead of the owner's content. However, any content can be spoofed, including the content of email messages, file transfers, or the content of other network communication protocols. Content can be modified at the source (e.g. modifying the source file for a web page) or in transit (e.g. intercepting and modifying a message between the sender and recipient). Usually, the adversary will attempt to hide the fact that the content has been modified, but in some cases, such as with web site defacement, this is not necessary. Content Spoofing can lead to malware exposure, financial fraud (if the content governs financial transactions), privacy violations, and other unwanted outcomes.

## Where this sits in the chain

A finding maps to a weakness (CWE), a weakness is exploited by an attack pattern (CAPEC), and an attack pattern shows up in ATT&CK as observed adversary behaviour. This page is the middle hop.

**Weaknesses exploited:** [CWE-345](/wiki/p/weakness/CWE-345)

**ATT&CK techniques:** [T1491](/wiki/p/technique/T1491)

## Prerequisites

- The target must provide content but fail to adequately protect it against modification.The adversary must have the means to alter data to which they are not authorized. If the content is to be modified in transit, the adversary must be able to intercept the targeted messages.

## Consequences

- Integrity: Modify Data

## Source

- [MITRE CAPEC CAPEC-148](https://capec.mitre.org/data/definitions/148.html)
